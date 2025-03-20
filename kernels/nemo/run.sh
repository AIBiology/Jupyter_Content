#!/usr/bin/bash

module load apptainer

apptainer exec -B /lustre/fs0/bsc4892:/bsc4892 /lustre/fs0/bsc4892/share/containers/nemo.sif python3 -m ipykernel "$@"
