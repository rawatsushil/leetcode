"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
"""


class Bucket:
    def __init__(self):
        self.bucket_list = []

    def get(self, key):
        for i in range(len(self.bucket_list)):
            if self.bucket_list[i][0] == key:
                return self.bucket_list[i][1]
        return -1

    def update(self, key, value):
        found = False
        for i in range(len(self.bucket_list)):
            if self.bucket_list[i][0] == key:
                self.bucket_list[i][1] = value
                found = True
                break
        if not found:
            self.bucket_list.append([key, value])

    def remove(self, key):
        for i, kv in enumerate(self.bucket_list):
            if key == kv[0]:
                del self.bucket_list[i]


class MyHashMap:
    def __init__(self):
        self.hash_number = 2039
        self.list = [Bucket() for i in range(self.hash_number)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.hash_number
        self.list[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.hash_number
        return self.list[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.hash_number
        self.list[hash_key].remove(key)

