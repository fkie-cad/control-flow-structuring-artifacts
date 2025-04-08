# Example usage (adjust as needed):

```commandline
podman build -t radare-image .
podman run --name RADARE -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z --rm radare-image 
```

**Decompiler Output:**

- "Function not found in decompiler output!" - If the complete output file does not contain the function or is empty
- "TimeOut" - If the subprocess terminates with a timeout
- "Error during Decompilation" - If the subprocess crashes