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
        self.nodes = [] if head is None else [head]

    def getAllNodes(self):
        return self.nodes

    def setAllnodes(self, allNodes):
        """
        replaces all nodes with the given list of nodes
        :param allNodes: list of nodes
        :type: list[node]
        :return: --
        """
        self.nodes = allNodes


    def addNode(self, node):
        """
        appends a node to the list of all nodes
        :param node: a node object
        :return: --
        """
        self.nodes.append(node)

    def getHead(self):
        return self.head

    def setHead(self, head):
        """
        Sets the head of the directed graph
        :param head: a node object
        :return: --
        """

        self.nodes.insert(0, head)
        self.head = head

    def __copy__(self):

        newGraph = directedGraph()
        newGraph.setAllnodes(self.getAllNodes())
        return newGraph

    def copy(self):
        return self.__copy__()

class node:

    def __init__(self, value, successor = None):
        """
        Initiates a node object
        :param values: a object of values which shall be stored in this node, e.g. an object of class Point
        :param successor: direct successor of this node
        """
        self.value = value
        self.successor = successor
        self.allSuccessor = [] if successor is None else [successor]

    def getValue(self):
        return self.value

    def setSuccessor(self, index, value):
        """
        Replaces a successor
        :param index: at which place the successor shall be replaced
        :param value: with which value the successor shall be replaced
        :return: --
        """
        self.allSuccessor[index] = value

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

    def removeSuccessor(self, successor):
        """
        Removes a successor from the list of successors.
        If the to be removed successor is the direct successor, a new direct successor is set
        :param successor: successor object which is to be removed
        :type: node
        :return: --
        """

        if self.allSuccessor.index(successor) == 0:
            if len(self.allSuccessor) > 2:
                self.successor = self.allSuccessor[1]
            else:
                self.successor = None

        self.allSuccessor.remove(successor)

    def removeMultipleSuccessors(self, indexes):
        """
        Removes multiple successors
        :param indexes: list of indexes
        :type: int
        :return: --
        """

        self.allSuccessor = [self.allSuccessor[i] for i in range(len(self.allSuccessor)) if i not in indexes]

    def getSuccessor(self):
        """
        :return: returns the next successor of the node
        """
        return self.successor

    def getAllSuccessor(self):
        """
        :return: returns the list of all successors
        """
        return self.allSuccessor

    def __copy__(self):
        newNode = node(self.value)
        newNode.addMultipleSuccessors(self.allSuccessor)
        return newNode