/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#include "stackNode.h"

//Constructors
template<class ItemType>
Node<ItemType>:: Node() : next(nullptr){}

template<class ItemType>
Node<ItemType>::Node(const ItemType& anItem) : item(anItem), next(nullptr){} 

template<class ItemType>
Node<ItemType>::Node(const ItemType& anItem, Node<ItemType>* nextNodePtr):item(anItem), next(nextNodePtr){} 

//Setters
template<class ItemType>
void Node<ItemType>::setItem(const ItemType& anItem){
    item = anItem;
}

template<class ItemType>
void Node<ItemType>::setNext(Node<ItemType>* nextNodePtr){
    next = nextNodePtr;
}

//Getters
template<class ItemType>
ItemType Node<ItemType>::getItem() const{
    return item;
}

template<class ItemType>
Node<ItemType>* Node<ItemType>::getNext() const{
    return next;
}