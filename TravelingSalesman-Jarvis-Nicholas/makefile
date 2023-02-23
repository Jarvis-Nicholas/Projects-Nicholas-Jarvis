tsp: driver.o
	g++ driver.o -o tsp

driver.o: driver.cpp stackNode.h linkedStack.h graph.h arrayQueue.h
	g++ -c driver.cpp

clean:
	rm *.o tsp