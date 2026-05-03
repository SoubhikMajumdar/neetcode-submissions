class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10**6 + 1
        self.data = [False] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.data[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.data[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.data[key]