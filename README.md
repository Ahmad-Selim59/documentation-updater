# Docu-Jarvis

An intelligent documentation updater that uses Claude Agent to analyze and improve documentation files in your repository. Docu-Jarvis automatically processes documentation files, suggests improvements, and creates pull requests with the changes.

## Features

- **Automated Documentation Analysis**: Processes all files in your documentation folder
- **AI-Powered Updates**: Uses Claude Agent to suggest documentation enhancements
- **Automatic PR Creation**: Creates pull requests with timestamped branches
- **Configurable**: Easy setup with environment variables
- **Async Processing**: Efficient handling of multiple documentation files

## Prerequisites

Before running Docu-Jarvis, ensure you have the following installed:

### Required Software
- **claude agent+** - deez 
- **Git** - [Download here](https://git-scm.com/downloads)
- **GitHub CLI** - [Installation guide](https://cli.github.com/manual/installation)

### Required Accounts & Access
- **Claude Agent** - deez
- **GitHub Repository Access** - The repository you want to update must be accessible
- **GitHub CLI Authentication** - Run `gh auth login` to authenticate

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GITHUB_URI` | The GitHub repository URL to clone and update | `https://github.com/user/repo.git` |
| `DOCUMENTATION_FOLDER` | The folder containing documentation files | `docs`, `documentation`, `guides` |

## Usage

Run Docu-Jarvis with the default configuration:

```bash
poetry run python src/main.py
```

### What Happens When You Run It

1. **Repository Cloning**: Downloads the specified GitHub repository to `/tmp/`
2. **Documentation Processing**: Walks through all files in the documentation folder
3. **AI Analysis**: For each file, sends it to Claude AI for analysis and improvement suggestions
4. **Change Detection**: Checks if any changes were made to the documentation
5. **Pull Request Creation**: If changes exist, creates a new branch and pull request

### Output

Docu-Jarvis will:
- Print progress messages as it processes each file
- Show any errors encountered during processing
- Create a timestamped branch (e.g., `docu-jarvis150120241430`)
- Push changes and create a pull request automatically

## Troubleshooting
