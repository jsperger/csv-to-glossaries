import csv
import sys
import os

def read_csv(input_file):
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
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
        entry.append(f"\\{command}{{{label}}}{{")

        keys = list(row.keys())[2:]  # Exclude the first two keys: 'command' and 'label'
        key_value_pairs = []
        for key in keys:
            value = row[key]
            if ',' in value:
                value = f'{{{value}}}'  # Enclose the value in braces if it contains a comma
            key_value_pairs.append(f"  {{{key}}} = {{{value}}}")

        entry.append(",\n".join(key_value_pairs))
        entry.append("}")

        tex_entries.append("\n".join(entry))

    return "\n".join(tex_entries)

if __name__ == '__main__':
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

    print(f"Tex file created at {output_file}")
