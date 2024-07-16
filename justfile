#!/usr/bin/env just --justfile

default:
    just --list


lint_black:
    poetry run black .

lint_ruff:
    poetry run ruff check --fix .

lint_pyright:
    poetry run pyright .

# Lint files for quality & type issues (with autofix)
lint: lint_black lint_pyright lint_ruff


test_pytest:
    poetry run pytest

# Run automated tests
test: test_pytest


check: lint test
