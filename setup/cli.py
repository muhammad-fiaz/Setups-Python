import click
import os

# Define a comprehensive list of valid licenses from GitHub
VALID_LICENSES = [
    'MIT', 'Apache-2.0', 'GPL-3.0', 'LGPL-3.0', 'BSD-2-Clause', 'BSD-3-Clause',
    'CC0-1.0', 'MPL-2.0', 'EPL-2.0', 'AGPL-3.0', 'MIT-0', 'ISC', 'Unlicense'
]

# Define available classifiers for easier reference
CLASSIFIERS = {
    "Development Status": [
        "1 - Planning", "2 - Pre-Alpha", "3 - Alpha", "4 - Beta", "5 - Production/Stable"
    ],
    "Intended Audience": [
        "Developers", "End Users/Desktop", "Education", "Science/Research", "System Administrators"
    ],
    "Programming Language": [
        "Python :: 3", "Python :: 3.8", "Python :: 3.9", "Python :: 3.10", "Python :: 3.11"
    ],
    "License": [
        "OSI Approved :: MIT License", "OSI Approved :: Apache Software License", "OSI Approved :: GPL License"
    ],
}

@click.command()
@click.argument("project_name")
def generate_setup(project_name):
    """
    Generate a complete setup.py file for a new Python project, asking the user for all details dynamically.
    """
    click.echo("Generating setup.py...")

    # Asking for required details with default values and handling backspace
    version = click.prompt("Version (e.g., 0.1.0)", type=str, default="0.1.0")
    description = click.prompt("Short project description", type=str)
    long_description = click.prompt("Long description (use content from your README.md)", type=str)
    author = click.prompt("Author name", type=str)
    author_email = click.prompt("Author email", type=str)

    # Handle license validation with retries
    while True:
        license_type = click.prompt("License type (e.g., MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, etc.)",
                                    type=str, default="MIT")
        if license_type in VALID_LICENSES:
            break
        else:
            click.echo(
                f"Invalid license type '{license_type}'. Please choose one of the valid licenses: {', '.join(VALID_LICENSES)}")

    python_version = click.prompt("Minimum Python version required (e.g., 3.8)", type=str, default="3.8")

    # Optional fields with defaults if left empty
    dependencies = click.prompt("Comma-separated list of dependencies (leave empty for none)", default="", type=str)
    dependencies = [dep.strip() for dep in dependencies.split(",") if dep.strip()]

    test_dependencies = click.prompt("Comma-separated list of test dependencies (leave empty for none)", default="",
                                     type=str)
    test_dependencies = [dep.strip() for dep in test_dependencies.split(",") if dep.strip()]

    # Asking for URLs
    project_url = click.prompt("Project URL (e.g., GitHub URL)", type=str)
    bug_tracker_url = click.prompt("Bug tracker URL", type=str)
    documentation_url = click.prompt("Documentation URL", type=str)

    # Asking for classifiers (optional but recommended)
    click.echo("Select 'Development Status' (e.g., 1 - Planning, 5 - Production/Stable):")
    development_status = click.prompt(
        "Development Status", type=click.Choice(CLASSIFIERS["Development Status"]), default="1 - Planning"
    )

    click.echo("Select 'Intended Audience' (e.g., Developers, End Users/Desktop):")
    audience = click.prompt(
        "Intended Audience", type=click.Choice(CLASSIFIERS["Intended Audience"]), default="Developers"
    )

    click.echo("Select 'Programming Language' (e.g., Python 3.8, Python 3.9):")
    language = click.prompt(
        "Programming Language", type=click.Choice(CLASSIFIERS["Programming Language"]), default="Python :: 3.8"
    )

    # Prepare the content for the setup.py file
    setup_content = f"""
from setuptools import setup, find_packages

VERSION = "{version}"  # Version of your package
DESCRIPTION = '{description}'  # Short description

# Long description of the project (can be pulled from README.md)
LONG_DESCRIPTION = '''{long_description}'''

setup(
    name="{project_name}",  # Name of your package
    version=VERSION,  # Package version
    author="{author}",  # Author name
    author_email="{author_email}",  # Author's email
    description=DESCRIPTION,  # Short description
    long_description=LONG_DESCRIPTION,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of the long description
    url="{project_url}",  # URL to the project's GitHub page
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[  # List of classifiers to categorize your package
        "Development Status :: {development_status}",
        "Intended Audience :: {audience}",
        "Programming Language :: {language}",
        "License :: OSI Approved :: {license_type}",
        "Operating System :: OS Independent",
    ],
    python_requires=">={python_version}",  # Minimum Python version required
    install_requires={dependencies},  # List of dependencies
    setup_requires=["pytest-runner"],  # For running tests during installation
    tests_require={test_dependencies},  # Specify dependencies needed for running tests
    license="{license_type}",  # License under which the project is released
    project_urls={{  # Additional URLs related to your project
        "Source Code": "{project_url}",
        "Bug Tracker": "{bug_tracker_url}",
        "Documentation": "{documentation_url}",
    }},
)

"""

    # Ensure the project folder exists, and create the setup.py file
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    with open(f"{project_name}/setup.py", "w") as f:
        f.write(setup_content)

    print(f"setup.py has been successfully generated for project '{project_name}'.")

if __name__ == "__main__":
    generate_setup()
