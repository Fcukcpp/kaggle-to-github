from configparser import ConfigParser
import os


def git_init(is_local_get_repo, git_repo):
    if is_local_get_repo:
        if os.system("git pull") != 0:
            print("Error while pulling from git...")
            exit()
    else:
        if os.system("git clone %s " % git_repo) != 0:
            print("Error while cloning repo %s..." % git_repo)
            exit()


def kaggle_download(kaggle_username, kaggle_dataset_output, kaggle_repo_list, kaggle_dataset_list):
    kaggle_repos = kaggle_repo_list.split(",")
    kaggle_datasets = kaggle_dataset_list.split(",")
    for kaggle_dataset in kaggle_datasets:
        if os.system("kaggle datasets download %s -p %s --force" % (kaggle_dataset, kaggle_dataset_output)) != 0:
            print("Error while downloading %s..." % kaggle_dataset)
            exit()
    for kaggle_repo in kaggle_repos:
        if os.system("kaggle kernels pull %s/%s" % (kaggle_username, kaggle_repo)) != 0:
            print("Error while downloading %s" % kaggle_repo)
            exit()


def git_commit_push(is_local_get_repo, git_repo):
    if os.system("git stage --all") == 0 and os.system('git commit -m "Added notebooks/datasets"') == 0:
        if is_local_get_repo is False:
            if os.system("git remote add origin %s" % git_repo) != 0:
                print("Error while adding remote %s" % git_repo)
                exit()
        if os.system("git push") == 0:
            print("Push Successful")
        else:
            print("Error in pushing...")
        exit()

def main():
    is_local_get_repo = False if os.system("git -C ./ rev-parse") != 0 else True
    parser = ConfigParser()
    parser.read('config.ini')

    kaggle_dataset_output = parser.get('kaggle', 'dataset_output_path')
    kaggle_username = parser.get('kaggle', 'username')
    kaggle_repo_list = parser.get('kaggle', 'repos')
    kaggle_dataset_list = parser.get('kaggle', 'datasets')
    git_repo = parser.get('git', 'repo')

    git_init(is_local_get_repo, git_repo)
    kaggle_download(kaggle_username, kaggle_dataset_output, kaggle_repo_list, kaggle_dataset_list)
    git_commit_push(is_local_get_repo, git_repo)

if __name__ == "__main__":
    main()