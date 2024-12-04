class Document:
    """represents a document in a cloud-based document editing and sharing system"""

    def __init__(self, creator_id: int, name: str, contents: str):
        self.name = name
        self.contents = contents
        self.creator_id = creator_id
        self.shared_user_ids = set()

    def share_with_user(self, user_id: int):
        """adds a user to the set of users with document access"""
        self.shared_user_ids.add(user_id)

    def unshare_with_user(self, user_id: int):
        """removes a user from the set of users with document access"""
        self.shared_user_ids.remove(user_id)

    def user_ids_with_access(self) -> set:
        """returns a set of all users with document access """
        return {self.creator_id} | self.shared_user_ids


class NoDocumentError(Exception):
    pass
