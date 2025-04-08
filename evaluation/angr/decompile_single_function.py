import datetime
import json
import logging
from pathlib import Path
from typing import Literal

import angr
import typer


def _get_angr_dec_options(param_string):
    opt_candidates = [o for o in angr.analyses.decompiler.decompilation_options.options if o.param == param_string]
    if not opt_candidates:
        return None

    return opt_candidates[0]


def get_decompiler_options(decompiler: Literal["SAILR", "DREAM", "Phoenix"]):
    match decompiler:
        case "SAILR":
            return None
        case "DREAM":
            return [
                (_get_angr_dec_options("structurer_cls"), "DREAM"),
                (_get_angr_dec_options("largest_successor_tree_outside_loop"), False),
                (_get_angr_dec_options("simplify_switches"), False),
            ]
        case "Phoenix":
            return [
                (_get_angr_dec_options("structurer_cls"), "Phoenix"),
                (_get_angr_dec_options("largest_successor_tree_outside_loop"), False),
                (_get_angr_dec_options("simplify_switches"), False),
            ]


def decompile(binary: Path, function_address: int, options):
    # Get the "angr" logger
    l = logging.getLogger("angr")
    l.setLevel(logging.ERROR)  # Set the desired logging level
    # Create a file handler
    fh = logging.FileHandler("angr.log", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    # Add the handler to the "angr" logger
    l.addHandler(fh)
    l.propagate = False

    start_time = datetime.datetime.now()
    proj = angr.Project(binary, auto_load_libs=False)
    cfg = proj.analyses.CFG(show_progressbar=False, normalize=True, data_references=True)
    # cfg = proj.analyse.CFGFast(normalize=True, resolve_indirect_jumps=True, data_references=True) # dogbolt
    proj.analyses.CompleteCallingConventions(cfg=cfg, recover_variables=True, analyze_callsites=True)

    state = proj.factory.blank_state(addr=function_address)
    function = state.addr

    # decompile_SAILR = proj.analyses.Decompiler(function, cfg=cfg, kb=cfg.kb, options=None)
    decompiler_output = proj.analyses.Decompiler(function, cfg=cfg.model, options=options)
    end_time = datetime.datetime.now()

    fh.close()

    return decompiler_output, str((end_time - start_time).total_seconds())


def main(
    binary_path: Path = typer.Argument(help="Path of the binary we want to decompile."),
    function_address: int = typer.Argument(help="Address of the we want to decompile."),
    decompiler: str = typer.Argument(help="The decompiler we want to use."),
):
    """Take the binary path, function and decompiler with which it should be decompiled."""
    assert decompiler in {"SAILR", "DREAM", "Phoenix"}, "We do not know the decompiler"
    result, time = decompile(binary_path, function_address, get_decompiler_options(decompiler))
    if result.codegen is None:
        code = "No decompilation Output!"
    else:
        code = result.codegen.text

    print(json.dumps({"decompiler_output": code, "time": time}))


if __name__ == "__main__":
    typer.run(main)
