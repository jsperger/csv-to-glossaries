import csv
import os

def convert_csv_to_tex(input_file):
    # Determine the output file name based on the input file name
    output_file = os.path.join(os.path.dirname(input_file),
                               os.path.splitext(os.path.basename(input_file))[0] + '.tex')

    # Write the header comments to the output file
    with open(output_file, 'w') as f:
        f.write("% This file was automatically generated.\n")
        f.write("% Do not manually edit this file.\n")
        f.write("% Instead edit the csv and rerun the script.\n\n")

    # Initialize a flag for the header row
    header_row = True
    header = []

    # Open the CSV file and read it row by row
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(output_file, 'a') as tex_file:  # Open the tex file in append mode
            for row in csv_reader:
                # Handle the header row
                if header_row:
                    header = row
                    header_row = False
                    continue

                # Start the \\newglossaryentry with the label from the first column
                tex_file.write(f"\\newglossaryentry{{{row[0]}}}{{\n")

                # Loop through the rest of the columns to add the corresponding fields
                for i in range(1, len(row)):
                    tex_file.write(f"  {header[i]} = {{{row[i]}}},\n")

                # Close the \\newglossaryentry
                tex_file.write("}\n")

if __name__ == "__main__":
    # Check for command-line argument
    if len(os.sys.argv) != 2:
        print("Usage: python script.py <input_file.csv>")
        os.sys.exit(1)

    input_file = os.sys.argv[1]
    convert_csv_to_tex(input_file)
