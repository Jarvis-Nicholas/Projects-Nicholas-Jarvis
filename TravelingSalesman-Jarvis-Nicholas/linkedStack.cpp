/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#include "linkedStack.h"

//Constructor
template<class ItemType> 
LinkedStack<ItemType>::LinkedStack(){
    //Nullify top
    top = NULL;
}

template<class ItemType>
bool LinkedStack<ItemType>::isEmpty() const{
    return top == NULL;
}

template<class ItemType>
bool LinkedStack<ItemType>::push(const ItemType& newEntry){
    Node<ItemType>* temp = new Node<ItemType>();

        //Computer has no more memory (very unlikely)
        if(!temp){
            std::cout << "\nNo more memory storage available!!\n";
            return 0;
        }
        else{
            //Make temp node
            Node<ItemType>* temp = new Node<ItemType>();

            //Save data into temp
            temp->setItem(newEntry);

            //Point temp to top
            temp->setNext(top);

            //Make temp the new top
            top = temp;
            
            return 1;
        }
}

template<class ItemType>
bool LinkedStack<ItemType>::pop(){
    //Make temp node
    Node<ItemType>* temp = new Node<ItemType>();

        //Error due to being empty
        if(isEmpty()){
            std::cout << "\nNo items to remove!\n";
            return 0;
        }
        else{
            temp = top;
            top = top->getNext();

                //Nullify
                temp = nullptr;

                //Free up Memory Location
                 delete temp;  

            return 1;         
        }
}

template<class ItemType>
ItemType LinkedStack<ItemType>::peek() const{

    bool canPeek = !isEmpty();

     if(canPeek){
        return top->getItem();;
     }
     //Empty stack
     else{
        throw "empty stack";
     }
}