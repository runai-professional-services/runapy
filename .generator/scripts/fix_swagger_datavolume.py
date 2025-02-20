import os

"""
Manual fix to old legacy 'Datavolume' model.
Issue:
Generator generates the model file name with incorrect '0' suffix
Fix:
Remove the 0 suffix from datavolume0.py, which resolves __.init__.py files. 
"""

# Files path relative to Makefile execution dir -> .generator
check_dirs = ["../runai", "../runai/models"]


def fix_data_volume_file_naming():
    for _dir in check_dirs:
        if "datavolume0.py" in os.listdir(_dir):
            print("Renaming datavolume0.py to datavolume.py")
            os.rename(
                os.path.join(_dir, "datavolume0.py"),
                os.path.join(_dir, "datavolume.py"),
            )
            print("Fixed datavolume.py")
        else:
            print("Could not find file named datavolume0.py in {}".format(_dir))


if __name__ == "__main__":
    fix_data_volume_file_naming()
