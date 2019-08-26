# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:12:21 2018

@author: Mallory
"""

class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next