<h1 align="center">
 Setups Python
</h1>
<p align="center">
    <img src="https://img.shields.io/pypi/v/setups.svg" alt="PyPI Version">
<img src="https://img.shields.io/github/license/muhammad-fiaz/setups-python.svg" alt="License Badge">
    <img src="https://img.shields.io/pypi/pyversions/setups.svg" alt="Python Version">
    <img src="https://img.shields.io/pypi/dm/setups.svg" alt="Downloads">
    <img src="https://img.shields.io/github/issues-pr/muhammad-fiaz/setups-python.svg" alt="PRs">
    <img src="https://img.shields.io/github/issues/muhammad-fiaz/setups-python.svg" alt="Issues">
    <img src="https://img.shields.io/github/contributors/muhammad-fiaz/setups-python.svg" alt="Contributors">
<img src="https://img.shields.io/github/last-commit/muhammad-fiaz/setups-python" alt="Last Commit"> 
<img src="https://img.shields.io/github/commit-activity/m/muhammad-fiaz/setups-python.svg" alt="Commit Activity">
    <img src="https://img.shields.io/github/license/muhammad-fiaz/setups-python.svg" alt="License Badge">
 <a href="https://github.com/muhammad-fiaz/Setups-Python/actions/workflows/github-code-scanning/codeql">
    <img src="https://github.com/muhammad-fiaz/Setups-Python/actions/workflows/github-code-scanning/codeql/badge.svg" alt="CodeQL Badge">
</a>

   <a href="https://github.com/sponsors/muhammad-fiaz">
    <img src="https://img.shields.io/badge/sponsor-muhammad--fiaz-ff69b4" alt="Sponsor" />
  </a>
</p>

**Setups Python** is a Python CLI tool to generate a `setup.py` file for your Python project dynamically. It prompts the user for key project details like dependencies, license types, and classifiers.

## Features

- Generate a `setup.py` with interactive prompts
- Supports common open-source licenses
- Define project metadata including dependencies, version, and URLs
- Integrate with PyPI and other tools seamlessly

## Installation

```bash
pip install setups
```

## Usage

To create a `setup.py` file for your new project:

```bash
setup <project_name>
```

## Example

```bash
$ setup my-awesome-project_name
Version (e.g., 0.1.0): 0.1.0
Short project description: An awesome project
License type: MIT
Minimum Python version required: 3.8
Dependencies: numpy, requests
```

## Contributing

We welcome contributions! Fork the repository, create a feature branch, and submit a pull request. Please follow the steps below:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to your fork: `git push origin feature-name`
5. Submit a pull request

## Code of Conduct

By participating in this project, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT License. See the [LICENSE](LICENSE) file for more details.
