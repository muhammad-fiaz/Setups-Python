from setuptools import setup, find_packages

VERSION = "0.0.2"  # Version of your package
DESCRIPTION = 'Setups: Dynamically generate setup.py for Python projects.'

# Reading the long description from README.md if exists
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        LONG_DESCRIPTION = fh.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION  # Fallback to DESCRIPTION if README.md is missing

setup(
    name="setups",  # Name of your package
    version=VERSION,  # Package version
    author="Muhammad Fiaz",  # Author name
    author_email="contact@muhammadfiaz.com",  # Author's email
    description=DESCRIPTION,  # Short description
    long_description=LONG_DESCRIPTION,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/muhammad-fiaz/setups-python",  # URL to the project's GitHub page
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[  # List of classifiers to categorize your package
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[  # Dependencies needed to run the package
        'click',  # For creating command-line interfaces
        'setuptools',  # For packaging the project
        'twine',  # For uploading the package to PyPI
        'wheel',  # Add wheel to create binary distributions
    ],
    setup_requires=['pytest-runner'],  # For running tests during installation
    tests_require=['pytest'],  # Dependencies for running tests
    license='MIT',  # License for the project
    project_urls={  # Additional URLs related to your project
        'Source Code': 'https://github.com/muhammad-fiaz/setups-python',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/setups-python/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/setups-python#readme',
    },
    entry_points={  # CLI Entry Point
        'console_scripts': [
            'setup = setups.cli:generate_setup',  # This links 'setup' command to generate_setup function
        ],
    },
)

# Guide for the user after installation
print("""
**************************************************
Installation Complete!

Once you've installed the package, you can now use the 'setup' command to generate setup.py for your Python project.

Usage:
    setup <project_name>

This will ask you a series of questions to generate a setup.py file for your project. Once the setup.py is generated:

🎉 Here's what you need to do next to upload your package to PyPI:

Step 1: Create the Distribution
--------------------------------
Run the following commands to build the distribution:

    python setup.py sdist bdist_wheel

This creates both source (.tar.gz) and wheel (.whl) distributions in the dist/ folder.

Step 2: Upload to PyPI
-----------------------
Once you've built the distribution, upload it to PyPI with the following:

    twine upload dist/*

This will prompt you for your PyPI credentials and upload your package.

You're all set to share your package with the world! 🚀

 -------------------
 | _______________ |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|__
|         [_____] []|  \__
L___________________J     \ \___\/
 ___________________      /\\
/###################\\    (__)

Thank you for using our tool. For more details on usage, please refer to the documentation:
https://github.com/muhammad-fiaz/setups-python#usage

**************************************************
""")

