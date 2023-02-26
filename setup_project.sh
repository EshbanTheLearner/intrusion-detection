#!/bin/bash

git clone https://github.com/jmnwong/NSL-KDD-Dataset.git

wget -O NSL-KDD-Dataset/training_attack_types.txt https://raw.githubusercontent.com/oreilly-mlsec/book-resources/master/chapter5/datasets/training_attack_types.txt

pip install -r requirements.txt