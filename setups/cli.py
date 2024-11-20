import sys

import click

from setups.help import print_help

# Define a comprehensive list of valid licenses from GitHub
VALID_LICENSES = [
    'MIT', 'Apache-2.0', 'GPL-3.0', 'LGPL-3.0', 'BSD-2-Clause', 'BSD-3-Clause',
    'CC0-1.0', 'MPL-2.0', 'EPL-2.0', 'AGPL-3.0', 'MIT-0', 'ISC', 'Unlicense'
]

# Define available classifiers for easier reference
DEFAULT_CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT",
    "Operating System :: OS Independent"
]

@click.command(help="Generate a complete setup.py and README.md file for a new Python project.")
@click.argument("project_name", required=False)
@click.option('--help', '-h', is_flag=True, help="Show this message and exit.")
def generate_setup(project_name, help):
    if help:
        print_help()
    else:
        if not project_name:
            click.echo("Error: Missing argument 'PROJECT_NAME'.")
            click.echo(generate_setup.get_help(click.Context(generate_setup)))
            return

        """
        Generate a complete setup.py and README.md file for a new Python project, asking the user for all details dynamically.
        """
        click.echo("Generating setup.py and README.md...")

        # Asking for required details
        version = click.prompt("Version (e.g., 0.1.0)", type=str, default="0.1.0")
        description = click.prompt("Short project description (optional)", type=str, default="")
        long_description = click.prompt("Long description (optional, use content from your README.md)", type=str, default="")

        # Author info now optional
        author = click.prompt("Author name (optional)", type=str, default="")
        author_email = click.prompt("Author email (optional)", type=str, default="")

        # Asking for license selection by index
        click.echo("Select a license:")
        for idx, license in enumerate(VALID_LICENSES):
            click.echo(f"{idx}. {license}")
        license_idx = click.prompt("License (Enter the index number)", type=int, default=0)
        license_type = VALID_LICENSES[license_idx]

        python_version = click.prompt("Minimum Python version required (e.g., 3.8)", type=str, default="3.8")

        # Optional fields with defaults if left empty
        dependencies = click.prompt("Comma-separated list of dependencies (leave empty for none)", default="", type=str)
        dependencies = [dep.strip() for dep in dependencies.split(",") if dep.strip()]

        test_dependencies = click.prompt("Comma-separated list of test dependencies (leave empty for none)", default="",
                                         type=str)
        test_dependencies = [dep.strip() for dep in test_dependencies.split(",") if dep.strip()]

        # URLs now optional
        project_url = click.prompt("Project URL (optional)", type=str, default="")
        bug_tracker_url = click.prompt("Bug tracker URL (optional)", type=str, default="")
        documentation_url = click.prompt("Documentation URL (optional)", type=str, default="")

        # Ask if the user wants to specify classifiers
        click.echo("Would you like to specify 'Development Status', 'Intended Audience', and 'Programming Language'?")
        use_classifiers = click.confirm("Specify classifiers?", default=False)

        classifiers = DEFAULT_CLASSIFIERS
        if use_classifiers:
            # Development Status
            development_status = click.prompt("Select 'Development Status' (e.g., 1 - Planning, 2 - Pre-Alpha, etc.)", type=str, default="5 - Production/Stable")
            classifiers[0] = f"Development Status :: {development_status}"

            # Intended Audience
            audience = click.prompt("Select 'Intended Audience' (e.g., Developers, Education, etc.)", type=str, default="Developers")
            classifiers[1] = f"Intended Audience :: {audience}"

            # Programming Language
            language = click.prompt("Select 'Programming Language' (e.g., Python :: 3)", type=str, default="Python :: 3")
            classifiers[2] = f"Programming Language :: {language}"

        # Prepare the content for the README.md file
        readme_content = f"# {project_name}\n\n{long_description if long_description else 'Project description'}\n"

        # Prepare the content for the setup.py file
        setup_content = f"""
    from setuptools import setup, find_packages
    
    VERSION = "{version}"  # Version of your package
    DESCRIPTION = '{description if description else "Project description"}'  # Short description
    
    # Long description of the project (can be pulled from README.md)
    LONG_DESCRIPTION = '''{long_description if long_description else 'Detailed project description from README.md'}''' 
    
    setup(
        name="{project_name}",  # Name of your package
        version=VERSION,  # Package version
        author="{author if author else ''}",  # Author name
        author_email="{author_email if author_email else ''}",  # Author's email
        description=DESCRIPTION,  # Short description
        long_description=LONG_DESCRIPTION,  # Detailed description from README.md
        long_description_content_type="text/markdown",  # Format of the long description
        url="{project_url if project_url else ''}",  # URL to the project's GitHub page
        packages=find_packages(),  # Automatically find all packages in the directory
        classifiers={classifiers},  # List of classifiers to categorize your package
        python_requires=">={python_version}",  # Minimum Python version required
        install_requires={dependencies},  # List of dependencies
        setup_requires=["pytest-runner"],  # For running tests during installation
        extras_require={{'test': {test_dependencies}}},
        license="{license_type}",  # License under which the project is released
        project_urls={{  # Additional URLs related to your project
            "Source Code": "{project_url}" 
            "Bug Tracker": "{bug_tracker_url}" 
            "Documentation": "{documentation_url}"
        }},
    )
    """

        # Create the README.md and setup.py files in the current directory
        with open("README.md", "w") as readme_file:
            readme_file.write(readme_content)

        with open("setup.py", "w") as setup_file:
            setup_file.write(setup_content)

        print(f"README.md and setup.py have been successfully generated for project '{project_name}'.")

if __name__ == "__main__":
    generate_setup()