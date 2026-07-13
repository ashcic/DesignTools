#!/usr/bin/env python3
import os

def build_tree(path, prefix=""):
    """
    Recursively builds lines of a tree structure for the given path.
    Inaccessible directories are listed but not traversed.
    """
    lines = []

    try:
        entries = sorted(os.listdir(path))
    except (PermissionError, OSError) as e:
        # Path itself is not listable
        return [f"{prefix}[access denied]"]

    for idx, name in enumerate(entries):
        full_path = os.path.join(path, name)
        is_last = (idx == len(entries) - 1)
        connector = "└── " if is_last else "├── "

        if os.path.isdir(full_path):
            lines.append(f"{prefix}{connector}{name}")

            extension = "    " if is_last else "│   "
            try:
                lines.extend(build_tree(full_path, prefix + extension))
            except (PermissionError, OSError):
                # Directory exists but cannot be traversed
                lines.append(f"{prefix}{extension}└── [access denied]")
        else:
            lines.append(f"{prefix}{connector}{name}")

    return lines

def main():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    root_name = os.path.basename(root_dir) or root_dir

    tree_lines = [root_name]
    tree_lines += build_tree(root_dir)

    output_file = os.path.join(root_dir, "tree_structure.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))

    print(f"Tree structure written to: {output_file}")

if __name__ == "__main__":
    main()