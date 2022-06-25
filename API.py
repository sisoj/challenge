from email.policy import default
from hashlib import md5
from collections import defaultdict

#storing of the nodes in a hashmap
#this hashmap since using the id as a key, will give us the unique number of keys, also the max len of the val in hashmap is going to be the most frequent unique id
class API:
    def __init__(self):
        self.hashmap = defaultdict(list)
        self.salt = 'salt'


    def getFirstNode(self, id):
        return self.hashmap[md5(id+self.salt)][0]


    def insertChildren(self, parentNode, childId):
        val = Node(childId)
        key = md5(childId+self.salt)

        self.hashmap[key].append(val)
        parentNode.children.append(val)
        return


    def findNumberOfUniqueNodes(self, id):
        return len(self.hashmap.keys())

    def findMostCommon(self):
        found, freq = -1, 0
        for key in self.hashmap.keys():
            if len(self.hashmap[key])>freq:
                found = key
                freq = len(self.hashmap[key])
        return self.hashmap[found][0].id

#more general algorithm using DFS starting with a node as source
#using discovered as a set as to not visit the same node twice

    def findNumberOfUnique(self, nodeId):
        key = md5(nodeId+self.salt)
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]

        ids = set()
        seen = set()
        self.__helper(node, ids, seen)
        return len(ids)


    def __helper(self, curr, ids ,seen):
        ids.add(curr.id)
        seen.add(curr)


        for child in curr.children:
            if child not in seen:
                self.__helper(child, ids, seen)


    def findMostFrequent(self, nodeId):
        key = md5(nodeId+self.salt)
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]

        ids = defaultdict(lambda:0)
        seen = set()
        self.__helper2(node, ids, seen)
        
        freq, mostfreq = 0, None
        for key in ids:
            if ids[key]>freq:
                freq = ids[key]
                mostfreq = key
        
        return mostfreq




    def __helper2(self, curr, ids ,seen):
        ids[curr]+=1
        seen.add(curr)


        for child in curr.children:
            if child not in seen:
                self.__helper(child, ids, seen)



class Node:
    def __init__(self, id):
        self.id = id
        self.children = []






















