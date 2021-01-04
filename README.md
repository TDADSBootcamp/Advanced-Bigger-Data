## The Developer Academy
### Advanced - Bigger Data

This project uses `pipenv` to manage dependencies and virtualenvs. [Installation instructions](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

### Getting Started

- Run `pipenv install --dev` to install the dependencies. (`--dev` installs the tooling described below)
- Run `pipenv shell` to enter the virtualenv created by the previous command
- Start (or restart) VSCode to ensure changes are picked up cleanly

### Project Setup

- `Pipfile` describes the libraries and other software this project depends on
- `Pipfile.lock` records the exact versions of the dependencies in `Pipfile` (and their dependencies, and *their* dependencies, and so on) so that the exact versions can be shared
- `.pylintrc` is the pylint configuration for Google's code style
- `.style.yapf` is a code formatter configuration appropriate for the `.pylintrc`
- `.vscode` is settings for VSCode to use `pylint`, `yapf` and `unittest`

### The Code

TBC... multiple methods for loading a ~3.5GB file for simple analysis, plus annotations for memory profiling (`mprof run python python/whatever.py`)