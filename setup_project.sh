#!/bin/bash

git clone https://github.com/jmnwong/NSL-KDD-Dataset.git

wget -O NSL-KDD-Dataset/training_attack_types.txt http://kdd.ics.uci.edu/databases/kddcup99/training_attack_types

pip install -r requirements.txt