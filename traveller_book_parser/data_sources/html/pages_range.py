Range = tuple[int, int]
RangeList = list[Range]


def get_pages_range_list(pages: str) -> RangeList:
    """Get a list of page ranges from a string.

    Example:
    -------
    >>> get_pages_range_list("1")
    [(1, 1)]
    >>> get_pages_range_list("1-3")
    [(1, 3)]
    >>> get_pages_range_list("1-3,5")
    [(1, 3), (5, 5)]
    """
    pages_range_list = []
    for range_str in pages.split(","):
        if "-" in range_str:
            start_str, end_str = range_str.split("-")
        else:
            start_str = end_str = range_str

        pages_range_list.append((int(start_str), int(end_str)))

    return pages_range_list
