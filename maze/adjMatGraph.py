# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.m_graph = []
        self.m_coordinates = {}
        self.index = 0
        self.m_indexToCoordinates = {}


    def addVertex(self, label:Coordinates):
        for eachVertex in self.m_graph:
            eachVertex.append(0)
        
        self.m_coordinates["{},{}".format(label.getRow(), label.getCol())] = self.index
        self.m_indexToCoordinates[self.index] = label
        self.index = self.index + 1
        self.m_graph.append([0 for _ in range(len(self.m_graph)+1)])


    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        weight : int = 2 if addWall else 1;
        vert1Index : int = self.m_coordinates["{},{}".format(vert1.getRow(), vert1.getCol())]
        vert2Index : int = self.m_coordinates["{},{}".format(vert2.getRow(), vert2.getCol())]
        self.m_graph[vert1Index][vert2Index] = weight;
        self.m_graph[vert2Index][vert1Index] = weight;

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        weight : int = 2 if wallStatus else 1;
        vert1Index : int = self.m_coordinates["{},{}".format(vert1.getRow(), vert1.getCol())]
        vert2Index : int = self.m_coordinates["{},{}".format(vert2.getRow(), vert2.getCol())]
        self.m_graph[vert1Index][vert2Index] = weight
        self.m_graph[vert2Index][vert1Index] = weight



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        vert1Index : int = self.m_coordinates["{},{}".format(vert1.getRow(), vert1.getCol())]
        vert2Index : int = self.m_coordinates["{},{}".format(vert2.getRow(), vert2.getCol())]
        self.m_graph[vert1Index][vert2Index] = 0
        self.m_graph[vert2Index][vert1Index] = 0


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.m_coordinates
        


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        vert1Index : int = self.m_coordinates["{},{}".format(vert1.getRow(), vert1.getCol())]
        vert2Index : int = self.m_coordinates["{},{}".format(vert2.getRow(), vert2.getCol())]
        return (self.m_graph[vert1Index][vert2Index] == 1) or (self.m_graph[vert1Index][vert2Index] == 2)



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        vert1Index : int = self.m_coordinates["{},{}".format(vert1.getRow(), vert1.getCol())]
        vert2Index : int = self.m_coordinates["{},{}".format(vert2.getRow(), vert2.getCol())]
        return (self.m_graph[vert1Index][vert2Index] == 2)



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        labelIndex = self.m_coordinates["{},{}".format(label.getRow(), label.getCol())]
        neighbours = []
        labelRow = self.m_graph[labelIndex]
        for i in range(len(labelRow)):
            if(len(neighbours) == 4):
                break
            if labelRow[i] == 1 or labelRow[i] == 2:
                neighbours.append(self.m_indexToCoordinates[i])
        return neighbours

        
