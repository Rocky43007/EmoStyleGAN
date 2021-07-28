#!/usr/bin/env bash

#SBATCH --job-name=emo_stylegan    # Job name
#SBATCH --gres=gpu:16 
#SBATCH --time=196:00:00     
#SBATCH --cpus-per-task=40
#SBATCH --pty /bin/bash 
#SBATCH -l
#SBATCH --output=./sbatch-logs   # Standard output and error log
module load anaconda3
source activate stylegan
module load gcc
module load cuda/11.1.1
cd stylegan

python -c "print('Test')"
#python train.py --outdir=../training_runs --data=../wikiart_256_7.zip --gpus=8
