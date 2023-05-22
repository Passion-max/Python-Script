import os
from pathlib import Path

def get_directory_structure(root_path):
    structure = []

    for root, dirs, files in os.walk(root_path):
        level = root.replace(str(root_path), '').count(os.sep)
        indent = '  ' * level
        structure.append(f"{indent}{Path(root).name}/")

        for file in files:
            sub_indent = '  ' * (level + 1)
            structure.append(f"{sub_indent}{file}")

    return structure

def save_structure_to_txt(structure, output_file):
    with open(output_file, 'w') as txt_file:
        for line in structure:
            txt_file.write(f"{line}\n")

def main():
    input_path = r"C:\dev\htdocs\ets"
    output_file = r"project_structure.txt"

    if os.path.exists(input_path) and os.path.isdir(input_path):
        directory_structure = get_directory_structure(Path(input_path))
        save_structure_to_txt(directory_structure, output_file)
        print(f"Directory structure saved to {output_file}")
    else:
        print("Invalid directory path. Please check the path and try again.")

if __name__ == "__main__":
    main()
