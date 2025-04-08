from pathlib import Path

import r2pipe
import typer


def decompile(binary: Path, function_address: int):
    """Analyzes and decompiles a binary with Radare2 using r2pipe."""

    try:
        # 1. Open Radare2 with analysis
        r2 = r2pipe.open(str(binary))
        r2.cmd("aaa")
        r2.cmd("-AA")

        # 2. Get the function name from the address
        # afl_command = f"afl | grep '0*{hex(function_address)[2:]}' | awk '{{print $4}}'"  # Construct afl command
        # Get the function name from the address
        afl_output = r2.cmd("afl").splitlines()
        hex_address = f"{function_address:x}"
        function_name = None
        for line in afl_output:
            parts = line.split()
            if len(parts) >= 4:
                addr = parts[0].lower().lstrip("0x")  # Normalize address (remove '0x' and leading zeros)
                if addr == hex_address:  # Exact match
                    function_name = parts[3]
                    break

        if not function_name:
            r2.quit()
            print(f"No function name found for address {hex(function_address)}")
            return "Function not found in decompiler output!"

        # 3. Seek to the function and decompile
        r2.cmd(f"s {function_name}")
        decompiled_code = r2.cmd("pdd")
        r2.quit()

        return decompiled_code

    except Exception as e:
        return f"Error: {e}"


def main(
    binary_path: Path = typer.Argument(help="Path of the binary we want to decompile."),
    function_address: int = typer.Argument(help="Address of the we want to decompile."),
):
    """Take the binary path, function and decompiler with which it should be decompiled."""
    print(decompile(binary_path, function_address))


if __name__ == "__main__":
    typer.run(main)
