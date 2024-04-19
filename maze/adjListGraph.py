# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.m_graph = {};

        
    def addVertex(self, label:Coordinates):
        self.m_graph["{},{}".format(label.getRow(), label.getCol())] = [];


    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)
    



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        self.m_graph["{},{}".format(vert1.getRow(), vert1.getCol())].append({"coord":vert2, "wall":addWall})
        self.m_graph["{},{}".format(vert2.getRow(), vert2.getCol())].append({"coord": vert1, "wall":addWall})
        return True

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        wallUpdate : int = 0;
        vert1Neighbours : list[dict] =  self.m_graph["{},{}".format(vert1.getRow(), vert1.getCol())]
        for neigh in vert1Neighbours:
            if neigh["coord"] == vert2:
                neigh["wall"] = wallStatus
                wallUpdate = wallUpdate + 1
                
            
        vert2Neighbours : list[dict] = self.m_graph["{},{}".format(vert2.getRow(), vert2.getCol())]
        for neigh in vert2Neighbours:
            if neigh["coord"] == vert1:
                neigh["wall"] = wallStatus
                wallUpdate = wallUpdate + 1
        
        return (wallUpdate == 2)



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.hasEdge(vert1, vert2):
            vert1Neighbours : list[dict] =  self.m_graph["{},{}".format(vert1.getRow(), vert1.getCol())]
            for neigh in vert1Neighbours:
                if neigh["coord"] == vert2:
                    vert1Neighbours.remove(neigh)
            
            vert2Neighbours : list[dict] =  self.m_graph["{},{}".format(vert2.getRow(), vert2.getCol())]
            for neigh in vert2Neighbours:
                if neigh["coord"] == vert1:
                    vert2Neighbours.remove(neigh)

            return True
        return False;


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.m_graph



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # for there to be an edge, vert2 must be in vert1's list of neighbours
        vert1Neighbours : list[dict] =  self.m_graph["{},{}".format(vert1.getRow(), vert1.getCol())]
        for neigh in vert1Neighbours:
            if neigh["coord"] == vert2: 
                return True;
        return False

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.hasEdge(vert1, vert2):
            vert1Neighbours : list[dict] =  self.m_graph["{},{}".format(vert1.getRow(), vert1.getCol())]
            for neigh in vert1Neighbours:
                if neigh["coord"] == vert2:
                    return neigh["wall"]
        else:
            return False
        
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        labelNeighbours : list[dict] = self.m_graph["{},{}".format(label.getRow(), label.getCol())]
        neighboursCoordinates : list[Coordinates] = [];
        for neigh in labelNeighbours:
            neighboursCoordinates.append(neigh["coord"])
        return neighboursCoordinates    
