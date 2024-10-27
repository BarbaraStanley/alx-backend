#!/usr/bin/env python3

"""
A module that returns the range of indexes to return in a list
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns the index for the range of items specified
    by the page and page_size"""
    start: int = (page - 1) * page_size # since the page is 1-indexed
    end: int = page*page_size
    page_index: tuple = (start, end)
    return page_index
