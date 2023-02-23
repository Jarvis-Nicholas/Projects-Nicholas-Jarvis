/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#ifndef ARRAY_QUEUE 
#define ARRAY_QUEUE

#include "queueInterface.h"

template<class ItemType> 
class ArrayQueue: public QueueInterface<ItemType> {
protected:
    static const int DEFAULT_CAPACITY = 100;
    int frontIndex, backIndex, itemCount;
    ItemType items[DEFAULT_CAPACITY - 1];
public: 
    //Constructor
    ArrayQueue();

    //Utility
    bool isEmpty() const; 
    bool enqueue(const ItemType& newEntry); 
    bool dequeue(); 
    ItemType peekFront() const; 

    //Destructor
    ~ArrayQueue() { } 
};  
#include "arrayQueue.cpp"
#endif