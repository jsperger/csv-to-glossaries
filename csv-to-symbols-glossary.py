
import csv
import argparse
import os

def write_tex_entry(writer, label, symbol, description, sort_prefix):
    # Only escape the backslash if it's not a part of a LaTeX command
    if not symbol.startswith('\\'):
        symbol = symbol.replace("\\", "\\\\")
    writer.write("\\newglossaryentry{" + label.strip() + "}{\n")
    writer.write("  category = {symbol},\n")
    writer.write(f"  name = {{\\ensuremath{{{symbol}}}}},\n")  # Updated line
    writer.write("  description = {" + description.strip() + "},\n")
    writer.write("  sort = {" + sort_prefix.strip() + "-" + label.strip() + "}\n")  # No trailing comma
    writer.write("}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to a TeX file for glossaries-extra package.")
    parser.add_argument("input_csv", help="Path to the input CSV file.")
    parser.add_argument("--output_tex", help="Optional path to the output TeX file.")
    
    args = parser.parse_args()
    input_csv = args.input_csv
    output_tex = args.output_tex if args.output_tex else os.path.splitext(input_csv)[0] + ".tex"

    with open(input_csv, 'r', encoding='utf-8-sig') as csv_file:  # Handle BOM
        csv_reader = csv.DictReader(csv_file)
        
        with open(output_tex, 'w') as tex_file:
            tex_file.write("% Symbol Glossary Entries\n")
            tex_file.write("% Automatically generated from '" + os.path.basename(input_csv) + "'\n")
            tex_file.write("% Do not manually edit\n\n")
            
            for row in csv_reader:
                write_tex_entry(tex_file, row['label'], row['symbol'], row['description'], row['sort-prefix'])

    print(f"TeX file created at {output_tex}")

if __name__ == "__main__":
    main()
