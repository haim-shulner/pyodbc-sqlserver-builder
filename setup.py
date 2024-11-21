from setuptools import setup, find_packages

setup(
    name="pyodbc_package",
    version="0.1.0",
    description="pyodbc package with embedded ODBC drivers",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "pyodbc_package": ["bin/linux/*", "bin/windows/*", "bin/macos/*"]
    },
    install_requires=["pyodbc"],
)
