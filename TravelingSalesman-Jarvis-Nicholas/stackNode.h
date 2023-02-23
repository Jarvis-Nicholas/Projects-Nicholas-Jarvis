/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#ifndef STACKNODE_H
#define STACKNODE_H

template<class ItemType>
class Node{
    ItemType item;
    Node<ItemType>* next;
    
public:
    //Constructors
    Node();
    Node(const ItemType& anItem);
    Node(const ItemType& anItem, Node<ItemType>* nextNodePtr);

    //Setters
    void setItem(const ItemType& anItem);
    void setNext(Node<ItemType>* nextNodePtr);

    //Getters
    ItemType getItem() const;
    Node<ItemType>* getNext() const;
};

#include "stackNode.cpp"
#endif