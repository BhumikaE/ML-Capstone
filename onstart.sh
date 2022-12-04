#!/bin/bash
# This file is run on instance start. Output in ./onstart.log

curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -

sudo apt-get install -y nodejs

pip install jupyterlab-git

conda install -c conda-forge jupyterlab-git

pip install transformers==4.4.2

pip install tokenizers==0.10.3

git clone https://github.com/BhumikaE/ML-Capstone.git
