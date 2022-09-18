import os
from pathlib import Path

def is_valid_path(path):
    if path is None:
        return False
    
    if path == '':
        return True

    obj = Path(path)
    if not obj.exists():
        os.mkdir(path)
    else:
        print(f"{path} exists already")
    return True


def build_full_filename(target_path, filename):
    filename = os.path.join(target_path, filename)

def write_data_in_file(data, filename, target_path=""):
    """
    Writes `data into` `filename`.
    `filename` lives in `target_path`
    """
    if not is_valid_path(target_path):
        print(f"Error while validating target path {target_path}")
        return

    filename = build_full_filename(target_path, filename)

    # file = f"{target_path}{filename}"
    with open(filename, 'w') as openfile:
        openfile.write(data)