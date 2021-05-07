class directedGraph:

    """
    Class for a directed graph
    """
    def __init__(self, head = None):
        """
        Instantiates a directed graph
        :param head: a node object (the first object)
        """
        self.head = head

    def getHead(self):
        return self.head

    def setHead(self, head):

        self.head = head

class node:

    def __init__(self, values):
        """
        Initiates a node object
        :param values: a object of values which shall be stored in this node, e.g. an object of class Point
        """
        self.values = values
        self.allSuccessor = []
        self.successor = None

    def getValues(self):
        return self.values

    def addSuccessor(self, successor):
        """
        Adds an successor to the node
        :param successor: a node object
        :return: --
        """

        # if the added element is the first element added, save it as the immediate successor
        if len(self.allSuccessor) == 0:
            self.successor = successor

        self.successor.append(successor)

    def addMultipleSuccessors(self, successors):
        """
        Adds multiple successors to the list of successors
        :param successors: list of nodes
        :return: --
        """

        # if added elements are the first elements added, save the first element of the list
        # as the immediate successor
        if len(self.allSuccessor) == 0 and len(successors) > 0:
            self.successor = successors[0]

        self.allSuccessor.extend(successors)

    def getSuccessor(self):
        """
        :return: returns the next successor of the node
        """
        return self.successor

    def getAllSuccessors(self):
        """
        :return: returns the list of all successors
        """
        return self.allSuccessor

