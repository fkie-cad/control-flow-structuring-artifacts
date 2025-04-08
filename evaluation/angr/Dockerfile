FROM opensuse/tumbleweed

# Install system dependencies needed for Python, Angr, and other tools
RUN zypper -n update && \
    zypper -n install -y python3 python3-pip gcc make git

# Create a directory for the decompiler tools
RUN mkdir /decompiler

# Set the working directory inside the container
WORKDIR /decompiler

RUN python3 -m venv /venv

# Activate the virtual environment (important!)
ENV PATH="/venv/bin:$PATH"

# Install Angr and its dependencies
RUN pip3 install --upgrade pip && \
    pip3 install angr && \
    pip3 install typer && \
    pip3 install tqdm

# Set an environment variable for the script name
ENV SCRIPT_NAME=decompile_sailr.py

# Copy entrypoint.sh to the image
COPY entrypoint.sh /decompiler/
RUN chmod +x /decompiler/entrypoint.sh

# Copy the Python script from the shared folder to the container
COPY decompile_single_function.py /decompiler/
COPY decompile_angr.py /decompiler/

# Set the entry point to run the entrypoint.sh script
ENTRYPOINT ["/decompiler/entrypoint.sh"]

# Define the shared volume (assuming it's mounted at /shared_volume)
VOLUME /shared_volume
