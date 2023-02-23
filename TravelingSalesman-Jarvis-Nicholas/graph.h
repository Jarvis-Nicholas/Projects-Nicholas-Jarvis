/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include "graphInterface.h"
#include "linkedStack.h"
#include "arrayQueue.h"


template<class LabelType>
class Graph: public GraphInterface<LabelType>{
    int numVertices;
    int numEdges;

    //2D vector. Not an array so that any sizing may be used (possibly more than just 5 cities)
    //Contains edges
    std::vector<std::vector<int>> adjacencyMatrix;

    //Contains all known vertices
    std::vector<LabelType> knownVertices;

    //Gets Label Index for Matrix
    int getVerticeIndex(LabelType) const;

    //Checks if vertice is already known
    bool verticeIsKnown(LabelType) const;

    //Delete vertice rows and columns
    void deleteVerticeHelper(int);

    //Used for Traversal
    bool checkDiscovered(LabelType item, std::vector<LabelType> isDiscovered);

public:
    //Constructor
    Graph();

    //Attribute Getters
    int getNumVertices() const;
    int getNumEdges() const; 
    LabelType getKnownVertices(int) const;

    //Non-Attribute Getters
    int getEdgeWeight(LabelType start, LabelType end) const; 

    //Utility
    bool add(LabelType start, LabelType end, int edgeWeight);
    bool remove(LabelType start, LabelType end);

    //Traversals
    void depthFirstTraversal(LabelType start, void visit(LabelType&)); 
    void breadthFirstTraversal(LabelType start, void visit(LabelType&)); 

    //Destructor
    ~Graph();
};

#include "graph.cpp"
#endif