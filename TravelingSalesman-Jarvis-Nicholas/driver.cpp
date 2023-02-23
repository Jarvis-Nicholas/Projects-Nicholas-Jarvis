/*
Author: Nicholas Jarvis
Homwork 7: Graphs
Date: 11/28/2022
*/

#include <iostream>
#include <fstream>
#include <algorithm>
#include "graph.h"


template<class LabelType>
void readInput(Graph<LabelType>& cities);

template<class LabelType>
void outputSolutions(Graph<LabelType>& cities, std::vector<LabelType> cityNames);

template<class LabelType>
double getTotalDistance(Graph<LabelType>& cities, std::vector<LabelType> cityNames);

template<class LabelType>
void displayRoute(std::vector<LabelType>& route, double distance, double gas, std::ofstream& file);


int main(){

    //Make graph
    Graph<std::string> cities;

    //Save points / edges to graph
    readInput(cities);

    //Save city names for displaying later
    std::vector<std::string> cityNames;
    
    for(int i = 0; i < cities.getNumVertices(); i++){
        cityNames.push_back(cities.getKnownVertices(i));
    }

    //Run all routes and save to file
    outputSolutions(cities, cityNames);

    return 0;
}

template<class LabelType>
void readInput(Graph<LabelType>& cities){
    std::string cityOne, cityTwo;
    int distance;

    //Read input file
    std::ifstream file;
    file.open("input.txt");

    if(file.is_open()){

        //Read input
        while(file >> cityOne >> cityTwo >> distance){
            cities.add(cityOne, cityTwo, distance);
        }

        //Close
        file.close();
    }
    else{
        //Error message
        std::cout << "Sorry, could not open input.txt for reading\n";  
    }
}

template<class LabelType>
void outputSolutions(Graph<LabelType>& cities, std::vector<LabelType> cityNames){
   
    //Will track the best route
    std::vector<LabelType> bestRoute;

    //Final Answer Variables
    double smallestDistance = 0;
    double smallestGas = 0;

    //Open output file
    std::ofstream file;
    file.open("output.txt");

    if(file.is_open()){

        //Do once for at least one route
        do{

            //Random pathway starts at Reno
            if(cityNames[0] == "Reno"){

                //Get travelled distance
                double totalDistance = getTotalDistance(cities, cityNames);

                //How much gas needed to cover distance
                double gasGallonsToBuy = totalDistance / 40;

                //Display Route
                displayRoute(cityNames, totalDistance, gasGallonsToBuy, file);

                //(Determine best route)
                //New best route OR first run
                if(totalDistance < smallestDistance || smallestDistance == 0){

                    //Save best route
                    bestRoute = cityNames;

                    //Save distance
                    smallestDistance = totalDistance;

                    //Save gas
                    smallestGas = gasGallonsToBuy;
                }
            }
        }
        //Scrambles the order to test a new route AND Reno is the start
        while(std::next_permutation(cityNames.begin(), cityNames.end()));


        //Display best route
        file << "\n--------------------------------------------------------------\n";
        file << "                      Best Route:\n\n";

        displayRoute(bestRoute, smallestDistance, smallestGas, file);

        //Close file
        file.close();
    }
    else{
        //Error message
        std::cout << "Sorry, could not open output.txt for writing\n";  
    }
}

template<class LabelType>
double getTotalDistance(Graph<LabelType>& cities, std::vector<LabelType> cityNames){
    double totalDistance = 0;

    for(int i = 0; i < cityNames.size(); i++){

        //At last destination
        if(i + 1 == cityNames.size()){
                    
            //Travel from end to starting place
            totalDistance += cities.getEdgeWeight(cityNames[i], cityNames[0]);
        }
        else{

            //Travel to next
            totalDistance += cities.getEdgeWeight(cityNames[i], cityNames[i + 1]);
        }
    }
    return totalDistance;
}

template<class LabelType>
void displayRoute(std::vector<LabelType>& route, double distance, double gas, std::ofstream& file){

    //File Output
    for(int i = 0; i < route.size(); i++){

        //Last one so return to starting city
        if(i == route.size() - 1){
            file << route[i] << " to " << route[0] << "\n";
        }
        //Normal
        else{
            file << route[i] << " to ";
        }
    }
    
    //Final data
    file << "Total Distance Travelled: " << distance << ", and Total Gallons Used: " << gas << "\n\n";
}