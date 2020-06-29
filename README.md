# kaggle-to-github
A python script which downloads kernels and datasets from kaggle and pushes them to your new/exisiting git repository.

# Prerequisites
  - Along with python, we need to install **kaggle** using below command
```sh
pip install kaggle
```
  - Next, go to **My Account** on kaggle and click on **Create new API token**
  - Move this **kaggle.json** to *C:\Users\username\\.kaggle\\*

# Setup
  - Copy this [config.ini](https://github.com/dhruvkalia13/kaggle-to-github/blob/master/config.ini) to your repo and update below fields
```sh
[kaggle]
username=dhruvkalia
repos=salinity-temp-polynomial-regression,salinity-temp-simple-linear-regression
datasets=sohier/calcofi
dataset_output_path=./input/water/

[git]
repo=https://github.com/dhruvkalia13/test.git
```
  - Run the [kaggle_to_github.py](https://github.com/dhruvkalia13/kaggle-to-github/blob/master/kaggle_to_github.py) at the root of your project and enjoy the show!
>If the dir is not a git repo, it will run **git init** and will add the git remote url before making a push.

![alt text](https://github.com/dhruvkalia13/kaggle-to-github/blob/master/screen-capture.png)

# Key notes
  - The dataset should not be more than [100mb](https://help.github.com/en/github/managing-large-files/conditions-for-large-files) (zip), otherwise it won't be pushed to git
  - All the changes in the repo will be pushed along with the downloaded datasets and kernels
  - Since, we are using configparser, it won't work below Python 3
