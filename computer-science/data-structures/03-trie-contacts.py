# solution for the 'contacts' problem
# @see: https://www.hackerrank.com/challenges/contacts/problem
# based on https://www.hackerrank.com/challenges/contacts/editorial

from functools import reduce
from typing import Dict


class Node:
    def __init__(self) -> None:
        self.end = False
        self.count = 0
        self.children: Dict[str, Node] = {}


class ContactList:
    def __init__(self) -> None:
        self.root = Node()

    def add(self, name: str):
        if not name:
            return

        current_node: Node = self.root
        for letter in name:
            if not letter in current_node.children:
                current_node.children[letter] = Node()
            current_node = current_node.children[letter]
            current_node.count += 1

    def find(self, prefix: str):
        if not prefix:
            return 0

        current_node = self.root

        current_node = reduce(
            lambda current_node, letter: current_node and current_node.children.get(letter), prefix, current_node)

        if current_node is None:
            # there is no path that encodes this whole prefix
            return 0
        else:
            # the number of nodes bellow this node is the time it was traversed
            # **considering that there is no repeated "add" operations**
            return current_node.count


contact_list = ContactList()
contact_list.add("ed")
contact_list.add("eddie")
contact_list.add("eddie")
contact_list.add("edward")
contact_list.add("edwina")

assert(contact_list.find("ed") == 5)
assert(contact_list.find("ew") == 0)
