import os
import platform

def configure_paths():
    system = platform.system().lower()
    base_path = os.path.dirname(__file__)
    binary_path = os.path.join(base_path, 'bin', system)

    if system == 'linux' or system == 'darwin':
        os.environ['LD_LIBRARY_PATH'] = binary_path + ':' + os.environ.get('LD_LIBRARY_PATH', '')
    elif system == 'windows':
        os.environ['PATH'] = binary_path + ';' + os.environ.get('PATH', '')

configure_paths()
