# Python Scripts for creating glossary entries from a csv

Python scripts for creating glossary `.tex` for the latex `glossaries-extra` package based on a
`.csv` input. There are currently two scripts:
1. `csv-to-glossary.py`
2. `csv-to-symbols-glossary.py`

These are both rough and ready, with strict input formatting requirements, minimal warnings,
and nonexistent error handling.

# General (non-symbolic) Glossary

The csv to glossary script is meant to accomodate more flexible use cases. There are two required columns,
but the script can handle an arbitrary number of columns (be aware that `glossaries-extra` has a limitation on the number of options
at time of writing). After the first two columns, the columns are assumed to specify key-value pairs.
The key name is taken from the header, while the value is taken from the entry.
The key names must match the desired glossaries-extra option.

## Columns
### Required
*  [ ] command: the command to use e.g. newacronym or newglossaryentry. Do not include the backslash.
*  [ ] label: the entry that will be used for commands involving the acronym e.g. \gls{label}

### Additional columns
For example, if the command is newglossaryentry:
*  [ ] name: the name of the thing
*  [ ] description: description of the thing

For example, if the command is newacronym:
*  [ ] short: the acronym
*  [ ] long: the full phrase
*  [ ] shortplural (*optional*): the plural form for the acronym. If omitted the short form is pluralized by adding an *s* e.g. MLE becomes MLEs
* [ ] longplural (*optional*): the plural form for the phrase. If omitted the phrase is pluralized by adding an *s* to the last word of the phrase
* [ ] category (*optional*): category that can be used for grouping and sorting.


The resulting entries look like:
```tex
\<command>{<label>}{
  <additional column 1> = {<row column 1 entry>},
  ...
  <last additional column> = {<row column entry>}
}

```

# Commas in entries

Commas in an entry must be enquoted with double quotes `"foo"`

# Symbols Glossary

The csv for the symbols glossary has a set structure with columns named `label`, `symbol`, `description`, and `sort-prefix`.
The symbol entry should be in the form of a command e.g. `\pi` not `pi`. The script automatically wraps all symbols in `\ensuremath`
so that they can be used outside of a math environment e.g. `\gls{foo}` and not `$\gls{foo}`.
The script creates a `sort` key-value where the value is given by concatenating the `sort-prefix` and `label` column entries separated by a dash

The result is:

```tex
\newglossaryentry{<label>}{
  category = {symbol},
  name = \ensuremath{<symbol>},
  description = {<description>},
  sort = {<sort-prefix>-<label>}
}
```

# Usage

1. Clone the repository into your directory of choice.
2. In the terminal run the command with the target csv `python ./csv-to-glossary.py input.csv`
3. You may optionally specify the output file name.
You should include the full path when specifying the output file name.
Ex: `python ./csv-to-glossary.py input.csv /path/to/output.tex`
