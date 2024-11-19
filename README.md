# Setups Python

**Setups Python** is a Python CLI tool to dynamically generate `setup.py` for Python projects. This tool allows you to configure important project details, such as dependencies, license types, classifiers, and more, through a simple command-line interface.

## Features

- Automatically generate a `setup.py` file for your Python project.
- Configure project version, description, license, dependencies, and more.
- Choose from a wide range of open-source licenses.
- Customize the setup process with URLs, classifiers, and other metadata.

## Installation

You can install `setups` from PyPI using pip:

```bash
pip install setups
```

## Usage

To generate a `setup.py` for your project, use the following command:

```bash
setup new <project_name>
```

You'll be prompted for the following information:

- Project version
- Short and long descriptions
- Author name and email
- License type (MIT, GPL, etc.)
- Minimum Python version required
- List of dependencies and test dependencies
- Project URL, bug tracker URL, and documentation URL
- Classifiers for the project

## Example

```bash
$ setup new my-awesome-project
Version (e.g., 0.1.0): 0.1.0
Short project description: A cool project
Long description (use content from your README.md): This project is amazing.
Author name: John Doe
Author email: johndoe@example.com
License type (MIT, GPL-3.0, etc.): MIT
Minimum Python version required (e.g., 3.8): 3.8
Comma-separated list of dependencies (leave empty for none): numpy, requests
Comma-separated list of test dependencies (leave empty for none): pytest
Project URL (e.g., GitHub URL): https://github.com/johndoe/my-awesome-project
Bug tracker URL: https://github.com/johndoe/my-awesome-project/issues
Documentation URL: https://github.com/johndoe/my-awesome-project/wiki
Comma-separated list of classifiers: Development Status :: 5 - Production/Stable, Intended Audience :: Developers
```

## License

MIT License. See the [LICENSE](LICENSE) file for more details.