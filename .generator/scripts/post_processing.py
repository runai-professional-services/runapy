"""
Process the generated client package folder and fix the following conditions:

1. Put None in lines where the field has no value: for example: "timeout_seconds = ,"
2. Fix lowercase true and false to True and False
3. Change any single quote in double quote string
4. Add missing commas after None in parameter lists
"""

import os
import re
import sys

import fix_swagger_datavolume


def fix_line(line: str) -> str:
    if line is None or not line:
        return ""

    # Fix single quotes
    if "'" in line:
        # Handle enum value lists
        if "must be one of enum values" in line:
            line = re.sub(
                r'must be one of enum values \((.*?)\)"',
                lambda m: "must be one of enum values ("
                + m.group(1).replace("'", '"').replace(", ", ", ")
                + ')"',
                line,
            )
        # Handle JSON strings
        elif '"description"' in line or '"status"' in line:
            line = re.sub(r"'(\{.*?\})'", r"\1", line)
        # Handle datetime format strings
        elif '"%Y-%m' in line:
            line = re.sub(r"'([^']*%[YmdHMS][^']*)'", r'"\1"', line)
        # Handle general strings with embedded quotes
        else:
            line = re.sub(r"'([^']*)'([^']*)'([^']*)'", r'"\1\'\2\'\3"', line)

    # Fix empty assignments to None
    if "=" in line:
        # Handle empty assignments and null values, preserving terminators
        line = re.sub(
            r"=\s*(?:null\b|[,\n)]|$)",
            lambda m: (
                f"= None{m.group()[0]}"
                if m.group()[0:1] in {",", chr(10), ")"}
                else (
                    "= None,"
                    if not line.rstrip().endswith(")")
                    and not line.rstrip().endswith(",")
                    and not line.rstrip().endswith("None")
                    else "= None"
                )
            ),
            line,
        )

        # Add missing commas after None in parameter lists
        if "None" in line and not line.strip().endswith(")"):
            line = re.sub(r"None\s*$", "None,", line)

    # Fix boolean values
    if "true" in line or "false" in line:
        line = re.sub(r"\btrue\b(?=\s*[,}\]])", "True", line)
        line = re.sub(r"\bfalse\b(?=\s*[,}\]])", "False", line)

    return line


def process_file(file_path: str) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        modified_lines = []
        changes_made = False

        for line_num, line in enumerate(content.splitlines(), 1):
            fixed_line = fix_line(line)
            if fixed_line != line:
                changes_made = True
            modified_lines.append(fixed_line)

        if changes_made:
            modified_content = "\n".join(modified_lines)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print(f"Fixed {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}", file=sys.stderr)
        raise


def main():
    """Main function to process all Python files in the client directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_dir}")

    # Go up two levels from scripts/ to project root
    project_root = os.path.normpath(os.path.join(script_dir, "../.."))
    print(f"Project root: {project_root}")

    # Process only test files in the test directory
    test_dir = os.path.join(project_root, "test")
    if not os.path.exists(test_dir):
        print(f"Error: Test directory not found at {test_dir}", file=sys.stderr)
        sys.exit(1)

    # Process all Python files in the test directory
    processed_files = 0
    for file in os.listdir(test_dir):
        if file.endswith(".py") and file.startswith("test_"):
            file_path = os.path.join(test_dir, file)
            try:
                process_file(file_path)
                processed_files += 1
            except Exception as e:
                print(f"Failed to process {file_path}: {str(e)}", file=sys.stderr)

    print(f"\nProcessed {processed_files} test files")

    print(f"\nRunning manual post_processing fixes")
    fix_swagger_datavolume.fix_data_volume_file_naming()


if __name__ == "__main__":
    main()
