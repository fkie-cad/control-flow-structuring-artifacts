# Example usage (adjust as needed):

```commandline
podman build -t revng-image .
podman run --name REVNG-C -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z --rm revng-image
```

**Decompiler Output:**

- "Function not found in decompiler output!" - If the complete output file does not contain the function or is empty
- "TimeOut" - If the subprocess terminates with a timeout
- "Error du Decompilation" - If the subprocess crashes