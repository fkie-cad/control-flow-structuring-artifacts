# Example usage (adjust as needed):

```commandline
podman build -t angr-image .
podman run --name <NAME> -e SCRIPT_NAME="<script.py>" -v /path/to/your/shared/folder:/shared_volume:Z angr-image
```

**Decompiler Output:**

- "No decompilation Output!" - If angr does not crash, but the decompiler output is None
- "TimeOut" - If the subprocess terminates with a timeout
- "Error during Decompilation" - If the subprocess crashes

For SAILR:

```commandline
podman run --name SAILR -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z -e SCRIPT_NAME="decompile_sailr.py" --rm  angr-image
```

For DREAM:

```commandline
podman run --name DREAM -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z -e SCRIPT_NAME="decompile_dream.py" --rm  angr-image
```

For Phoenix:

```commandline
podman run --name PHOENIX -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z -e SCRIPT_NAME="decompile_phoenix.py" --rm  angr-image
```