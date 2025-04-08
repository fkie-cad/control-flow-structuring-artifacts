# Example usage (adjust as needed):

```commandline
podman build -t retdec-image .
podman run --name RETDEC -v <PATH_TO_EVALUATION_FOLDR_IN_ARTIFACTS>:/shared_volume:Z --rm retdec-image
```

**Decompiler Output:**

- "Function not found in decompiler output!" - Could not find function
- "TimeOut" - If the subprocess terminates with a timeout
- "Error du Decompilation" - If the subprocess crashes