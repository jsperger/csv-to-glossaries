#!/usr/bin/env bash

# Check for command-line argument
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <input_file.csv>"
  exit 1
fi

# Get the input filename
input_file="$1"
output_file="$(dirname "$input_file")/$(basename "$input_file" .csv).tex"

# Write the header comments to the output file
printf "%% This file was automatically generated.\n" > "$output_file"
printf "%% Do not manually edit this file.\n" >> "$output_file"
printf "%% Instead edit the csv and rerun the script.\n\n" >> "$output_file"

# Initialize a flag for the header row
header_row=1

# Read the CSV file line by line
while IFS=',' read -ra line_array; do
  # Handle the header row
  if [[ $header_row -eq 1 ]]; then
    header=("${line_array[@]}")
    header_row=0
    continue
  fi

  # Start the \newglossaryentry with the label from the first column
  printf "\\\newglossaryentry{%s}{\n" "${line_array[0]}" >> "$output_file"

  # Loop through the rest of the columns to add the corresponding fields
  for ((i=1; i<${#line_array[@]}; i++)); do
    printf "  %s={%s}" "${header[i]}" "${line_array[i]}" >> "$output_file"

    # Add a comma unless this is the last entry
    if [[ $i -lt $((${#line_array[@]} - 1)) ]]; then
      printf ",\n" >> "$output_file"
    else
      printf "\n" >> "$output_file"
    fi
  done

  printf "}\n\n" >> "$output_file"

done < "$input_file"

echo "TeX file created: $outputfile"
