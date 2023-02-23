/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#include "arrayQueue.h"

template<class ItemType> 
ArrayQueue<ItemType>::ArrayQueue(){
    frontIndex = -0;
    backIndex = DEFAULT_CAPACITY - 1;
    itemCount = 0;
}

template<class ItemType> 
bool ArrayQueue<ItemType>::isEmpty() const{
    return itemCount == 0;
}

template<class ItemType> 
bool ArrayQueue<ItemType>::enqueue(const ItemType& newEntry){
    bool canNQ = itemCount < DEFAULT_CAPACITY;

    if (canNQ){
        backIndex = (backIndex + 1) % DEFAULT_CAPACITY;
        items[backIndex] = newEntry;
        itemCount++;
    } 

    return canNQ;
}

template<class ItemType> 
bool ArrayQueue<ItemType>::dequeue(){
    bool canDQ = !isEmpty();

    if (canDQ){
        frontIndex = (frontIndex + 1) % DEFAULT_CAPACITY;
        itemCount--;
    }

    return canDQ;
}

template<class ItemType> 
ItemType ArrayQueue<ItemType>::peekFront() const{
    bool canPeek = !isEmpty();
    
    if (canPeek){
        return items[frontIndex];
    }
    else{
        throw "empty queue";
    }
} 