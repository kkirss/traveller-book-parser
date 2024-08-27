#!/usr/bin/env just --justfile

default:
    just --list


lint_black:
    poetry run black .

lint_ruff:
    poetry run ruff check --fix .

lint_pyright:
    poetry run pyright .

lint_schema_gen:
    poetry run traveller-book-parser schema all

# Lint files for quality & type issues (with autofix)
lint: lint_black lint_pyright lint_ruff lint_schema_gen


test_pytest:
    poetry run pytest

test_pytest_snapshots:
    poetry run pytest --snapshot-update

# Run automated tests
test: test_pytest

# Run automated tests and update snapshots
test_update: test_pytest_snapshots


check: lint test

check_update: lint test_update
