#!/bin/bash
# https://www.kaggle.com/datasets/daiearth22/applewatch

# @todo ensure we are in the right folder before this scripts. Should be from root of repo.

curl -L -o applewatch.zip\
  https://www.kaggle.com/api/v1/datasets/download/daiearth22/applewatch

mv applewatch.zip infra/local_env/local_data/raw/
