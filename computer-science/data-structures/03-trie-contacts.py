from typing import Dict, List


class Node:
    def __init__(self, letter: str, name: str = "") -> None:
        self.name = name
        self.letter = letter

        self.children: List[Node] = []

    @property
    def is_empty(self):
        return len(self.name) == 0

    def __str__(self) -> str:
        if self.name:
            return f"Node(\"{self.name}\")"
        return f"Node('{self.letter}')"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.letter)


class ContactList:
    def __init__(self) -> None:
        self.dictionary: Dict[str, Node] = {}

    def _build_tree_for_name(self, name: str) -> Node:
        initial = name[0]

        if len(name) == 1:
            node = Node(name, name)
            return node

        if initial in self.dictionary:
            parent_node = self.dictionary[initial]
        else:
            parent_node: Node = Node(name[0])

        last_node = parent_node
        for i, letter in enumerate(name[1:]):
            if i == len(name) - 2:
                node = Node(letter, name)
            else:
                node = Node(letter)
            try:
                last_node = list(filter(lambda n: n.letter ==
                                        letter, last_node.children))[0]
            except IndexError:
                last_node.children.append(node)
                last_node = node

        return parent_node

    def add(self, name: str):
        if not name:
            return

        initial = name[0]

        self.dictionary[initial] = self._build_tree_for_name(name)


contact_list = ContactList()
contact_list.add("ed")
contact_list.add("eddie")
contact_list.add("eddie")
contact_list.add("edward")
contact_list.add("edwina")
pass
