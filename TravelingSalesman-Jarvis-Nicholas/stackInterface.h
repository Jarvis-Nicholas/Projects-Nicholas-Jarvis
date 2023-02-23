/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#ifndef STACKINTERFACE 
#define STACKINTERFACE 


template<class ItemType> 
class StackInterface { 
public: 
    virtual bool isEmpty() const = 0; 
    virtual bool push(const ItemType& newEntry) = 0; 
    virtual bool pop() = 0; 
    virtual ItemType peek() const = 0; 
    virtual ~StackInterface() { } 
};  
#endif