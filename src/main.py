import os
import subprocess

from config.env_vars import DOCUMENTATION_FOLDER, GITHUB_URI

FOLDER = ""


def claude_agent_processor(doc: str) -> None:
    pass


def process_documentation() -> None:
    documentation_path = os.path.join(FOLDER, DOCUMENTATION_FOLDER)

    if not os.path.exists(documentation_path):
        raise FileNotFoundError(f"Documentation folder not found: {documentation_path}")

    for root, _, files in os.walk(documentation_path):
        for file in files:
            file_path = os.path.join(root, file)
            claude_agent_processor(file_path)


def clone_repo() -> None:
    global FOLDER

    repo_name = GITHUB_URI.rstrip("/").split("/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    FOLDER = os.path.join("/tmp", repo_name)

    if os.path.exists(FOLDER):
        subprocess.run(["rm", "-rf", FOLDER], check=True)

    subprocess.run(["git", "clone", GITHUB_URI, FOLDER], check=True)
    print("repo cloned successfully")


def main() -> None:
    clone_repo()
    process_documentation()


if __name__ == "__main__":
    main()
