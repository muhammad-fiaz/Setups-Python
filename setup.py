from setuptools import setup, find_packages

VERSION = "0.0.1"  # Version of your package
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
    url="https://github.com/muhammad-fiaz/setups",  # URL to the project's GitHub page
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
    ],
    setup_requires=['pytest-runner'],  # For running tests during installation
    tests_require=['pytest'],  # Dependencies for running tests
    license='MIT',  # License for the project
    project_urls={  # Additional URLs related to your project
        'Source Code': 'https://github.com/muhammad-fiaz/setups',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/setups/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/setups#readme',
    },
    entry_points={  # CLI Entry Point
        'console_scripts': [
            'setup = setups.cli:generate_setup',  # This links 'setup' command to generate_setup function
        ],
    },
)
