/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#ifndef LINKEDSTACK_H
#define LINKEDSTACK_H

#include <vector>
#include "stackInterface.h"
#include "stackNode.h"

template<class ItemType>
class LinkedStack: public StackInterface<ItemType> {
private:
    Node<ItemType>* top;
    
public:

    //Constructor
    LinkedStack();

    //Interface
    bool isEmpty() const;
    bool push(const ItemType& newEntry);
    bool pop();
    ItemType peek() const;
};

#include "linkedStack.cpp"
#endif