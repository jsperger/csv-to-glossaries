# Reference Guide to acronym-gloss-entries.csv

This is a tiny script with strict formatting requirements. Don't do things like include commas in your entries or latex commands.

# Columns

*  [ ] label: the entry that will be used for commands involving the acronym e.g. \gls{label}
*  [ ] short: the acronym
*  [ ] long: the full phrase
*  [ ] shortplural (*optional*): the plural form for the acronym. If omitted the short form is pluralized by adding an *s* e.g. MLE becomes MLEs
* [ ] longplural (*optional*): the plural form for the phrase. If omitted the phrase is pluralized by adding an *s* to the last word of the phrase
* [ ] category (*optional*): category that can be used for grouping and sorting.
