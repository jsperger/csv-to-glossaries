import csv
import sys
import os

def read_csv(input_file):
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if not all(column in reader.fieldnames for column in ["command", "label", "short", "long"]):
            print("Error: CSV must contain 'command', 'label', 'short', and 'long' columns.")
            sys.exit(1)
        rows = [row for row in reader]
    return rows

def generate_tex(rows):
    tex_entries = []
    tex_entries.append("% This file was automatically generated.")
    tex_entries.append("% Do not manually edit this file.")
    tex_entries.append("% Instead edit the csv and rerun the script.")
    tex_entries.append("")

    for row in rows:
        entry = []
        command = row['command']
        label = row['label']
        short = row['short']
        long_desc = row['long']

        if ',' in long_desc:
            long_desc = f'{{{long_desc}}}'  # Enclose the value in braces if it contains a comma

        entry.append(f"\\{command}{{{label}}}{{{short}}}{{{long_desc}}}")

        tex_entries.append("\n".join(entry))

    return "\n".join(tex_entries)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file.csv> [output_file.tex]")
        sys.exit(1)

    input_file = sys.argv[1]

    # Check if the output file is provided
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        base_name, _ = os.path.splitext(input_file)
        output_file = f"{base_name}.tex"

    rows = read_csv(input_file)
    tex_content = generate_tex(rows)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(tex_content)

    print(f"TeX file created at {output_file}")
