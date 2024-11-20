

def usage_instructions():
    print(r"""
Quick Start Guide:
------------------
To create a `setup.py` file for your project, use:

    setup <project_name>

For help, use:

    setup --help or setup -h

This will provide details on usage and options for generating the `setup.py` file.
""")


def build_and_publish_steps():
    print(r"""
🚀 Steps to Build and Publish Your Package on PyPI 🚀

Step 1: Build Your Distribution
------------------------------
Use the following command to build both source (`.tar.gz`) and wheel (`.whl`) distributions:

    python setup.py sdist bdist_wheel
             or
    python -m build

This will generate your package files in the `dist/` directory.

Step 2: Upload to PyPI
----------------------
Upload your package using `twine`:

    twine upload dist/*

You’ll be prompted for your PyPI credentials. Once uploaded, your package will be live for everyone to use!
""")


def testing_and_validation():
    print(r"""
🧪 Testing and Validation 🧪

1. **Install the Package Locally**
   Test your package installation:

       pip install .

2. **Editable Installation for Development**
   Use this to test changes to your package without reinstalling:

       pip install -e .

3. **Run Tests**
   Use `pytest` for testing your code:

       pytest

4. **Check Package Metadata**
   Validate the correctness of your metadata using `twine`:

       twine check dist/*

5. **Clean Build Artifacts**
   Remove previously generated build files:

       python setup.py clean --all
""")


def additional_build_commands():
    print(r"""
📦 Additional Build Commands 📦

1. **Generate Only Source Distribution**:
       python setup.py sdist

2. **Generate Only Wheel Distribution**:
       python setup.py bdist_wheel

3. **Use `python -m build` (Recommended)**:
       python -m build

   This method automatically handles both source and wheel distributions efficiently.
""")


def print_footer():
    print(r"""
Helpful Resources:
-------------------
👉 [GitHub: setups-python Documentation](https://github.com/muhammad-fiaz/setups-python#usage)

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

Thank you for choosing our tool! 😊
**************************************************
""")


def print_help():
    usage_instructions()
    build_and_publish_steps()
    testing_and_validation()
    additional_build_commands()
    print_footer()

