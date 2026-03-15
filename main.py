import os
import sys

DB_FILE = "data.db"

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedListStore:
    def __init__(self):
        self.head = None

    def set(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

def append_to_log(key, value):
    with open(DB_FILE, "a") as f:
        f.write(key + "\t" + value + "\n")

def load_from_log(store):
    if not os.path.exists(DB_FILE):
        return

    with open(DB_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                store.set(parts[0], parts[1])

def main():
    store = LinkedListStore()
    load_from_log(store)

    while True:
        command = input()

        if command == "EXIT":
            break

        parts = command.split(" ", 2)

        if parts[0] == "SET":
            key = parts[1]
            value = parts[2]

            store.set(key, value)
            append_to_log(key, value)

            print("OK")

        elif parts[0] == "GET":
            key = parts[1]
            value = store.get(key)

            if value is not None:
                print(value)
            else:
                print("")

if __name__ == "__main__":
    main()
    

