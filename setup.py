import os
import setuptools
from setuptools.command.install import install
import subprocess
import sys
import platform

# Determine platform
system = platform.system().lower()  # 'linux' or 'darwin' (macOS)

# Define the version of unixODBC that we're using
UNIXODBC_VERSION = "2.3.12"

# Construct the version tag based on the platform and unixODBC version
PACKAGE_VERSION = f"0.1.1+unixodbc{UNIXODBC_VERSION}.{system}"

class CustomInstallCommand(install):
    def run(self):
        # Run the default installation
        install.run(self)

        # Run the custom unixODBC build script
        build_script_path = os.path.join(os.path.dirname(__file__), 'unixodbc_wrapper', 'build_unixodbc.py')
        subprocess.run([sys.executable, build_script_path], check=True)

setuptools.setup(
    name="unixodbc-pyodbc-wrapper",
    version=PACKAGE_VERSION,
    author="Your Name",
    author_email="your_email@example.com",
    description="A package to install unixODBC and pyodbc for MS SQL use with Python (Linux and macOS)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
