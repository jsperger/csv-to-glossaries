# A Python Script for creating glossary entries from a csv

This is a tiny script with strict formatting requirements to convert a
csv of glossary items into a tex file with the entries formatted for the
glossaries package.

Don't do things like include commas in your entries or latex commands.

# Columns
### Required
*  [ ] command: the command to use e.g. newacronym or newglossaryentry. Do not include the backslash.
*  [ ] label: the entry that will be used for commands involving the acronym e.g. \gls{label}

### Optional
Optional columns are assumed to specify key-value pairs for the entry in a row.
The key name is taken from the header, while the value is taken from the entry.
The key names must match the desired glossaries-extra option.

For example, if the command is newacronym:
*  [ ] short: the acronym
*  [ ] long: the full phrase
*  [ ] shortplural (*optional*): the plural form for the acronym. If omitted the short form is pluralized by adding an *s* e.g. MLE becomes MLEs
* [ ] longplural (*optional*): the plural form for the phrase. If omitted the phrase is pluralized by adding an *s* to the last word of the phrase
* [ ] category (*optional*): category that can be used for grouping and sorting.


While if the command is newglossaryentry
*  [ ] name: the name of the thing
*  [ ] description: description of the thing

# Usage

1. Clone the repository into your directory of choice.
2. In the terminal run the command with the target csv `python ./csv-to-glossary.py input.csv`
3. You may optionally specify the output file name.
You should include the full path when specifying the output file name.
Ex: `python ./csv-to-glossary.py input.csv /path/to/output.tex`
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      