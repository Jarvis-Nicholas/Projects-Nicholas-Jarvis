/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#include "graph.h"

//Constructor
template<class LabelType>
Graph<LabelType>::Graph(){
    numVertices = 0;
    numEdges = 0;
}

//Getter Label Index (Only use after verticeIsKnown is true)
template<class LabelType>
int Graph<LabelType>::getVerticeIndex(LabelType item) const{
    for(int i = 0; i < numVertices; i++){
        if(item == knownVertices[i]){
            return i;
        }
    }

    //Error message in case function is used without checking verticeIsKnown first
    throw "Confirm that vertice exists before finding index\n";
}

//Getter Label is known
template<class LabelType>
bool Graph<LabelType>::verticeIsKnown(LabelType item) const{
    for(int i = 0; i < numVertices; i++){
        if(item == knownVertices[i]){
            return 1;
        }
    }
    return 0;
}

//Delete Vertice Helper
template<class LabelType>
void Graph<LabelType>::deleteVerticeHelper(int index){

    //Make iterator
    std::vector<std::vector<int>>::iterator rowRemoval;

    //Set iterator
    rowRemoval = adjacencyMatrix.begin();

    //Deletes entire row
    adjacencyMatrix.erase(rowRemoval + index);

    //Delete entire column
    for(int i = 0; i < adjacencyMatrix.size(); i++){
        adjacencyMatrix[i].erase(adjacencyMatrix[i].begin() + index);
    }

    //Decrement
    knownVertices.erase(knownVertices.begin() + index);
    numVertices--;
}

//Getter Vertices
template<class LabelType>
int Graph<LabelType>::getNumVertices() const{
    return numVertices;
}

//Getter Edges
template<class LabelType>
int Graph<LabelType>::getNumEdges() const{
    return numEdges;
}

//Getter Vertice Names
template<class LabelType>
LabelType Graph<LabelType>::getKnownVertices(int index) const{
    return knownVertices[index];
}

//Getter Weight
template<class LabelType>
int Graph<LabelType>::getEdgeWeight(LabelType start, LabelType end) const{

    //Find Indexes
    int startIndex = getVerticeIndex(start);
    int endIndex = getVerticeIndex(end);
    
    //Return exact location
    return adjacencyMatrix[startIndex][endIndex];
}

//Add
template<class LabelType>
bool Graph<LabelType>::add(LabelType start, LabelType end, int edgeWeight){
    
    //Cannot create edge of city heading to itself
    if(start != end){

        //Start not kown
        if(!verticeIsKnown(start)){
            knownVertices.push_back(start);
            numVertices = knownVertices.size();

            //Resize
            adjacencyMatrix.resize(numVertices);
            for(int i = 0; i < numVertices; i++){

                //Adjust subsection to numVertices and fill elements with 0
                adjacencyMatrix[i].resize(numVertices, 0);
            }
        }

        //End not known
        if(!verticeIsKnown(end)){
            knownVertices.push_back(end);
            numVertices = knownVertices.size();

            //Resize
            adjacencyMatrix.resize(numVertices);
            for(int i = 0; i < numVertices; i++){

                //Adjust subsection to numVertices and fill elements with 0
                adjacencyMatrix[i].resize(numVertices, 0);
            }
        }

        //Get Indexes
        int startIndex = getVerticeIndex(start);
        int endIndex = getVerticeIndex(end);

        //Undirected so both ways are the same
        adjacencyMatrix[startIndex][endIndex] = edgeWeight;
        adjacencyMatrix[endIndex][startIndex] = edgeWeight;
    
        //Increment
        numEdges++;
        
        return 1;
    }
    else{
        return 0;
    }
}

//Remove
template<class LabelType>
bool Graph<LabelType>::remove(LabelType start, LabelType end){

    //Vertices exist
    if(verticeIsKnown(start) && verticeIsKnown(end)){
       
        int startIndex = getVerticeIndex(start);
        int endIndex = getVerticeIndex(end);

        //User wants entire vertice deleted
        if(start == end){

            //Decrement Edges that will be lost
            for(int i = 0; i < numVertices; i++){

                //Value that is not junk
                if(adjacencyMatrix[startIndex][i] != 0){
                    numEdges--;
                }
            }
            //Delete Vertice
            deleteVerticeHelper(startIndex);

            return 1;
        }

        //Edge is empty (denoted by 0)
        if(adjacencyMatrix[startIndex][endIndex] == 0){
            return 0;
        }

        bool deleteStart = 1;
        bool deleteEnd = 1;

        //Nullify desired element
        adjacencyMatrix[startIndex][endIndex] = 0;

        //Check if either vertices need to be deleted
        for(int i = 0; i < numVertices; i++){

            //Value that is not junk
            if(adjacencyMatrix[startIndex][i] != 0){
                deleteStart = 0;
            }

            //Value that is not junk
            if(adjacencyMatrix[i][endIndex] != 0){
                deleteEnd = 0;
            }
        }

        //Start is empty
        if(deleteStart == 1){
            deleteVerticeHelper(startIndex);
        }

        //End is empty
        if(deleteEnd == 1){
            deleteVerticeHelper(endIndex);
        }

        //Decrement
        numEdges--; 

        return 1;
    }

    //Vertices don't exist
    return 0;
}

template<class LabelType>
bool Graph<LabelType>::checkDiscovered(LabelType item, std::vector<LabelType> isDiscovered){
    for(int i = 0; i < isDiscovered.size(); i++){
        if(item == isDiscovered[i]){
            return 1;
        }
    }
    return 0;
}


//Depth Traversal
template<class LabelType>
void Graph<LabelType>::depthFirstTraversal(LabelType start, void visit(LabelType&)){
    
    //Determines if node has been visited yet or not
    std::vector<LabelType> isDiscovered;
    
    //Default function (used for printing in driver)
    //Prints the starting node
    visit(start);

    //Make stack
    LinkedStack<LabelType> stack;
    stack.push(start);

    //Mark as visited
    isDiscovered.push_back(start);

    //Go until everything is explored
    while(stack.isEmpty() == 0){

        LabelType current = stack.peek();
        int currentIndex = getVerticeIndex(current);

        for(int i = 0; i < numVertices; i++){

            LabelType next = knownVertices.at(i);
            int edgeValue = adjacencyMatrix[currentIndex][i];

            //New Discovery
            if(checkDiscovered(next, isDiscovered) == 0 && edgeValue != 0){
                
                //Mark new node (possibly print data)
                visit(next);

                //Mark as visited
                isDiscovered.push_back(next);

                //Add to stack
                stack.push(next);
            }
            //End of the road
            else if(i == numVertices - 1){
                stack.pop();
            }
        }
    }
}


//Breadth Traversal
template<class LabelType>
void Graph<LabelType>::breadthFirstTraversal(LabelType start, void visit(LabelType&)){

    //Determines if node has been visited yet or not
    std::vector<LabelType> isDiscovered;

    //Default function (used for printing in driver)
    //Prints the starting node
    visit(start);

    //Make Queue
    ArrayQueue<LabelType> queue;
    queue.enqueue(start);
    
    //Mark as visitied
    isDiscovered.push_back(start);

    //Go until everything is explored
    while(queue.isEmpty() == 0){

        //Get front of queue
        LabelType current = queue.peekFront();
        int currentIndex = getVerticeIndex(current);

        //Remove front of queue
        queue.dequeue();

        for(int i = 0; i < numVertices; i++){

            LabelType next = knownVertices.at(i);
            int edgeValue = adjacencyMatrix[currentIndex][i];

            //Next one hasn't been visited yet and is not junk
            if(checkDiscovered(next, isDiscovered) == 0 && edgeValue != 0){

                //Mark new node (possibly print data)
                visit(next);

                //Mark as visited
                isDiscovered.push_back(next);

                //Add to queue
                queue.enqueue(next);
            }
        }
    }
}

//Destructor
template<class LabelType>
Graph<LabelType>::~Graph(){}