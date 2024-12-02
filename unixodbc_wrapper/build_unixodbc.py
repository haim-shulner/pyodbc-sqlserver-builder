import os
import platform
import subprocess
import sys

UNIXODBC_URL = "http://www.unixodbc.org/unixODBC-2.3.12.tar.gz"
INSTALL_DIR = os.path.join(os.path.dirname(__file__), 'unixodbc_install')

def download_and_build_unixodbc():
    os.makedirs(INSTALL_DIR, exist_ok=True)
    tar_file = os.path.join(INSTALL_DIR, "unixODBC-2.3.12.tar.gz")

    # Download unixODBC
    subprocess.run(["curl", "-L", UNIXODBC_URL, "-o", tar_file], check=True)

    # Extract
    subprocess.run(["tar", "-xvf", tar_file, "-C", INSTALL_DIR], check=True)

    # Change directory to source folder
    source_dir = os.path.join(INSTALL_DIR, "unixODBC-2.3.12")
    os.chdir(source_dir)

    # Configure, compile, and install
    subprocess.run(["./configure", f"--prefix={INSTALL_DIR}"], check=True)
    subprocess.run(["make"], check=True)
    subprocess.run(["make", "install"], check=True)

    print("unixODBC installed successfully.")

def install_pyodbc():
    # Use pip to install pyodbc, providing environment variables so it can find unixODBC
    env = os.environ.copy()
    env["CFLAGS"] = f"-I{INSTALL_DIR}/include"
    env["LDFLAGS"] = f"-L{INSTALL_DIR}/lib"
    subprocess.run([sys.executable, "-m", "pip", "install", "pyodbc"], check=True, env=env)

if __name__ == "__main__":
    download_and_build_unixodbc()
    install_pyodbc()
