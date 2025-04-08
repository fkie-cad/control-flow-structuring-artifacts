FROM opensuse/tumbleweed

# Install system dependencies needed for Python, Angr, and other tools
RUN zypper -n update && \
    zypper -n install -y python3 python3-pip python3-tqdm gcc make git xz curl

# Create a directory for the decompiler tools
RUN mkdir /decompiler

# Set the working directory inside the container
WORKDIR /decompiler

# install revng
RUN curl -L -s https://rev.ng/downloads/revng-distributable/master/install.sh -o install.sh
RUN bash install.sh

# Copy entrypoint.sh to the image
COPY entrypoint.sh /decompiler/revng
RUN chmod +x /decompiler/revng/entrypoint.sh


WORKDIR /decompiler/revng

# Copy the Script from the shared folder to the container
COPY decompile_revng_c.py /decompiler/revng
COPY decompile_revng_c.sh /decompiler/revng
RUN chmod +x /decompiler/revng/decompile_revng_c.sh

# Set the entry point to run the entrypoint.sh script
ENTRYPOINT ["/decompiler/revng/entrypoint.sh"]

# Define the shared volume (assuming it's mounted at /shared_volume)
VOLUME /shared_volume
