#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int profit;
    int weight;
    float ratio;
} Item;

void sortByRatio(Item *items, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (items[i].ratio < items[j].ratio) {
                Item temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
    }
}

float fractionalKnapsack(Item *items, int n, int capacity) {
    sortByRatio(items, n);
    float totalProfit = 0.0;
    int currentWeight = 0;

    for (int i = 0; i < n; i++) {
        if (currentWeight + items[i].weight <= capacity) {
            totalProfit += items[i].profit;
            currentWeight += items[i].weight;
        } else {
            float fraction = (float)(capacity - currentWeight) / items[i].weight;
            totalProfit += items[i].profit * fraction;
            break;
        }
    }

    return totalProfit;
}

int main() {
    int n, capacity;

    printf("Enter the number of objects: ");
    scanf("%d", &n);

    Item *items = (Item *)malloc(n * sizeof(Item));

    printf("Enter the profits and weights:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &items[i].profit, &items[i].weight);
        items[i].ratio = (float)items[i].profit / items[i].weight;
    }

    printf("Enter the capacity of the knapsack: ");
    scanf("%d", &capacity);

    float maxProfit = fractionalKnapsack(items, n, capacity);

    printf("The maximum profit is: %f\n", maxProfit);
}
