import enum


class OutputType(str, enum.Enum):
    """Type of output (e.g. stdout or file)."""

    stdout = "stdout"
    file = "file"
