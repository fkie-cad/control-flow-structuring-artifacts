FROM opensuse/tumbleweed

# Install system dependencies needed for Python, Angr, and other tools
RUN zypper -n update && \
    zypper -n install -y python3 python3-pip gcc make git xz gawk patch ninja meson python311-typer

# Create a directory for the decompiler tools
RUN mkdir /decompiler

# Set the working directory inside the container
WORKDIR /decompiler

# install radare2
RUN git clone https://github.com/radareorg/radare2
WORKDIR /decompiler/radare2
RUN sys/install.sh
RUN r2pm -U
RUN r2pm -ci r2dec
RUN python3 -m venv .venv
ENV PATH=".venv/bin:$PATH"
RUN pip install r2pipe typer tqdm


# Copy entrypoint.sh to the image
COPY entrypoint.sh /decompiler/radare2
RUN chmod +x /decompiler/radare2/entrypoint.sh


WORKDIR /decompiler/radare2

# Copy the Script from the shared folder to the container
COPY decompile_radare.py /decompiler/radare2
COPY decompile_single_function.py /decompiler/radare2

# Set the entry point to run the entrypoint.sh script
ENTRYPOINT ["/decompiler/radare2/entrypoint.sh"]

# Define the shared volume (assuming it's mounted at /shared_volume)
VOLUME /shared_volume
