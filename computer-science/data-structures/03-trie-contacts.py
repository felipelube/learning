class Node:
    def __init__(self) -> None:
        self.end = False
        self.children = {}


class ContactList:
    def __init__(self) -> None:
        self.root = Node()

    def add(self, name: str):
        if not name:
            return

        current_node = self.root
        for letter in name:
            if not letter in current_node.children:
                current_node.children[letter] = Node()
            current_node = current_node.children[letter]

        current_node.end = True


contact_list = ContactList()
contact_list.add("ed")
contact_list.add("eddie")
contact_list.add("eddie")
contact_list.add("edward")
contact_list.add("edwina")
pass
