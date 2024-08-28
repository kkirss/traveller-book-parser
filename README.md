# traveller-book-parser

## What

Parse Traveller books into other formats.

*By books, we mean any piece of writing related to traveller or a similar RPG system
 (e.g. rulebooks, content books, roll tables, etc.).*

## Why

Why do we need to parse books?

This is because most books are copyrighted.
Distributing the content of these books without explicit permission is illegal.
It's pretty safe to assume that there are going to be publishers who won't allow free distribution of their content, for obvious reasons.

**NB: This project only contains descriptions of books, not the content within.
To get the content, you need to purchase the original books.**

### Publishers

As a show of goodwill, we want to explicitly ask publishers if they are okay with this script supporting parsing their content.

Here's a list of publishers who have said that this is fine:
* Stellagama Publishing
* Mongoose Publishing

*Feel free to open an issue if you are a publisher and interested in this.*

### Free distribution

Some publishers might allow free distribution of their content.
This is definitely an avenue to look into.

Stellagama Publishing specifically has shown interest in this.

## How

We distinctly separate parsing of books from outputting content.
This allows for greater flexibility:
* Parsing code doesn't need to know how the content will be used.
* Outputting code doesn't need to know how the content was parsed.

### Parsing books

First, we convert the content within books into a machine-readable format, in the form of "Traveller objects".

TODO: Document the traveller object formats.

#### Book descriptions

The code that runs is identical for all books.
This makes it easier to add new books.

To account for differences between books, there are 'book description' files.
These are JSON files describing the book (see `book_descriptions` folder for examples).

### Outputting book content

TODO: This is not implemented yet.

After parsing the books, we output the parsed objects into various formats. 

## Usage

### Requirements

1. [Python 3.11+](https://www.python.org/downloads/)
2. [Poetry](https://python-poetry.org/docs/)
3. [Java](https://www.java.com/en/download/)
    * This is used by [Tabula](https://tabula.technology/) to extract tables from PDFs.
4. pdftohtml (version 4.x) from [XpdfReader](https://www.xpdfreader.com/download.html)
    * This is used to convert PDFs to HTML. To then be parsed further.
    * <details>
        <summary>Installing pdftohtml:</summary>

        * It's available in package managers under the name `xpdf-tools` (e.g. in Scoop).
        * It is pre-packaged with some Linux distributions (e.g. Ubuntu).
        * You can [download it here](https://www.xpdfreader.com/download.html) 
           (under "Download the Xpdf command line tools").

        Note: If `pdftohtml` is not globally installed,
         you can set `PDF_TO_HTML_EXECUTABLE` env var to the location of the executable.
 
    </details>

Note: The code is tested on Windows 11.
 But it should work fine on Linux and possibly Mac.

### Running

1. Clone this repository.
2. Install dependencies using poetry: `poetry install`
3. Run the CLI to see available commands: `poetry run traveller-book-parser`
   * You can also run `poetry shell` to start a new sub-shell. And then run the CLI with `traveller-book-parser`.

There is a `cli.ps1` PowerShell script that does everything above (passing any arguments to the CLI).

### Configuration

The script can be configured using environment variables.
(You can create a `.env` file in the root directory to set these as well.)

See `traveller_book_parser/settings/settings.py` for a list of all settings.

You can also run:
```shell
traveller-book-parser schema Settings
```
This will dump the JSON schema of the `Settings` model (by default to `/data/output/schema/Settings.json`).

## Contributing

This project is open to contributions.
Feel free to open an issue or pull request.

## Development

Install [just](https://github.com/casey/just?tab=readme-ov-file#installation) to run utility commands.

### Linting

To run linters, run:
```shell
just lint
```

### Testing

To run tests, run:
```shell
just test
```

To run tests and update snapshots, run:
```shell
just test_update
```
