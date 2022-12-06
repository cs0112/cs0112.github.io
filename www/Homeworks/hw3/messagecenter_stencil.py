class Message:
    def __init__(self, from_user: str, to_user: str, contents: str):
        self.from_user = from_user
        self.to_user = to_user
        self.contents = contents
        self.read = False

    def mark_read(self):
        self.read = True


class MessageCenter:

    def __init__(self):
        pass

    def add_user_to_group(self, group: str, user: str):
        pass

    def add_direct_message(self, from_user: str, to_user: str, contents: str):
        pass

    def add_group_message(self, from_user: str, group: str, contents: str):
        pass

    def next_message(self, to_user: str) -> Message:
        pass

    def message_history(self, user1: str, user2: str) -> list:
        pass
