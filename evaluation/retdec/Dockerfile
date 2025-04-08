FROM opensuse/tumbleweed

# Install system dependencies needed for Python, Angr, and other tools
RUN zypper -n update && \
    zypper -n install -y python3 python3-pip python3-tqdm gcc make git xz gawk binutils wget

# Create a directory for the decompiler tools
RUN mkdir /decompiler

# Set the working directory inside the container
WORKDIR /decompiler

# install radare2
RUN wget https://github.com/avast/retdec/releases/download/v5.0/RetDec-v5.0-Linux-Release.tar.xz
RUN mkdir retdec
RUN tar -xf RetDec-v5.0-Linux-Release.tar.xz -C retdec/
RUN rm RetDec-v5.0-Linux-Release.tar.xz


WORKDIR /decompiler/retdec

# Copy entrypoint.sh to the image
COPY entrypoint.sh /decompiler/retdec
RUN chmod +x /decompiler/retdec/entrypoint.sh

# Copy the Script from the shared folder to the container
COPY decompile_retdec.py /decompiler/retdec

# Set the entry point to run the entrypoint.sh script
ENTRYPOINT ["/decompiler/retdec/entrypoint.sh"]

# Define the shared volume (assuming it's mounted at /shared_volume)
VOLUME /shared_volume
