"""

The file should be executed before running the openapi-cli generate command.
Issue:
Generating the client with these existing directories causes conflicts.
openapi-cli does not have override flag.
Fix:
The script removes 'runai' 'tests' and 'test' directories before re-generating them.
TODO: revaluate if file can be removed for another solution
"""

import os
import shutil

# Files path relative to Makefile execution dir -> .generator
dirs = ["../runai", "../test", "../tests"]


def main():
    for _dir in dirs:
        if not os.path.isdir(_dir):
            print("Skipping {} folder, already deleted".format(_dir))
            continue
        # delete dir
        try:
            shutil.rmtree(_dir)
            print("Removed {} folder".format(_dir))
        except Exception as e:
            print("Failed to remove {} folder: {}".format(_dir, e))


if __name__ == "__main__":
    main()
