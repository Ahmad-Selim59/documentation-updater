import os
import subprocess

from config.env_vars import GITHUB_URI

FOLDER = ""


def clone_repo():
    global FOLDER

    repo_name = GITHUB_URI.rstrip("/").split("/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    FOLDER = os.path.join("/tmp", repo_name)

    if os.path.exists(FOLDER):
        subprocess.run(["rm", "-rf", FOLDER], check=True)

    subprocess.run(["git", "clone", GITHUB_URI, FOLDER], check=True)
    print("repo cloned successfully")


def main():
    clone_repo()


if __name__ == "__main__":
    main()
