#include<stdio.h>

void DijkshatraAlgo(int Graph[10][10], int size, int start) {
    int cost[10][10], distance[10], prev[10];
    int visitedNodes[10], counter, min_distance, nextNode, i, j;

    // FOR COST GRAPH CREATION
    for(i = 0; i < size; i++) {
        for(j = 0; j < size; j++) {
            if (Graph[i][j] == 0) {
                cost[i][j] = 9999;
            } else {
                cost[i][j] = Graph[i][j];
            }
        }
    }

    // FOR DISTANCE ARRAY
    for(i = 0; i < size; i++) {
        distance[i] = cost[start][i];  
        prev[i] = start;  
        visitedNodes[i] = 0; 
    }

    distance[start] = 0;  
    visitedNodes[start] = 1;  
    counter = 1;  

    // MAIN LOGIC
    while (counter < size - 1) {

        // COMPARING WITH MIN DISTANCE
        min_distance = 9999;
        for(i = 0; i < size; i++) {
            if (distance[i] < min_distance && !visitedNodes[i]) {
                min_distance = distance[i];
                nextNode = i;
            }
        }

        visitedNodes[nextNode] = 1;
        for(i = 0; i < size; i++) {
            if (!visitedNodes[i]) {
                if (min_distance + cost[nextNode] < distance[i]) {
                    distance[i] = min_distance + cost[nextNode][i];
                    prev[i] = nextNode;
                }
            }
            counter++;
        }

        for(i = 0; i < size; i++) {
            if (i != size) {
                printf("Distance from source to %d: %d", i, distance[i]);
            }
        }
    }
}

int main() {
    int size, start;
    printf("Enter the number of vertices: ");
    scanf("%d", &size);
    int Graph[10][10];
    printf("Enter the adjacency matrix: ");
    for(int i=0; i<size; i++) {
        for(int j=0; j<size; j++) {
            scanf("%d", &Graph[i][j]);
        }
    }
    printf("Enter the starting node: ");
    scanf("%d", &start);
    DijkstraAlgorithm(Graph, size, start);
}