from dataclasses import dataclass

@dataclass
class BDRItem:
    title: str
    year: int
    contributor: list[str]
    subject: list[str]
    abstract: str
    notes: str


def most_common_subject(data: dict[str, list[BDRItem]], collection: str) -> list[str]:
    """
    Find the most common subject in a collection.
    
    :param data: Dictionary of collection names to lists of BDRItems
    :param collection: Name of the collection to analyze
    :return: A list of the most common subject(s)
    """
    pass


def year_after(data: dict[str, list[BDRItem]], collection: str, year: int) -> list[BDRItem]:
    """
    Find all items published after the given year.
    
    :param data: Dictionary of collection names to lists of BDRItems
    :param collection: Name of the collection to analyze
    :param year: The year to filter by
    :return: List of BDRItems published after the given year
    """
    pass


def top_contributor(data: dict[str, list[BDRItem]], collection: str, position: str) -> list[str]:
    """
    Find the top contributor in a collection.
    
    :param data: Dictionary of collection names to lists of BDRItems
    :param collection: Name of the collection to analyze
    :return: A list of the name(s) of the top contributor
    """
    pass

