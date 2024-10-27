#!/usr/bin/env python3

"""
A module that to get paginated data from a file
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_content = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(page_content):
            return []
        else:
            return page_content[start: end]
    
def index_range(page: int, page_size: int) -> tuple:
    """Returns the index for the range of items specified
    by the page and page_size"""
    
    start: int = (page - 1) * page_size # since the page is 1-indexed
    end: int = page*page_size
    page_index: tuple = (start, end)
    return page_index