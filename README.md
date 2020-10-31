# compileGA
Simple script that makes pretty PDF of form submissions

## About
The main purpose of the script is to load a csv-file, ususally generated from Google Form responses, and compile them using `pdflatex`, given this is installed on the machine.

Comes in handy when preparing papers to General Assemblies.

## Usage
The "parameters" are hardwritten to the string, but can easily be forked and fixed locally. In order for the script to work, the csv file must be on the form

| Timestamp | E-mail | Name | Case number | Suggestion type | Original text | New text | Reasoning |
|:---------:|--------|------|-------------|-----------------|---------------|----------|-----------|
| ...       | ...    | ...  | ...         | ...             | ...           | ...      | ...       |
| ...       | ...    | ...  | ...         | ...             | ...           | ...      | ...       |

That is, with column titles, and data for at least 8 columns. Works of course for arbitarily long columns.
