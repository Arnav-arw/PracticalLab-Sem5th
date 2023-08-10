#include<stdio.h>

int findPositionViaLinearSearch(int arr[], int size, int key) {
    for (int i = 0; i <= size; i++) {
        if (arr[i] == key) {
            return i +1;
        }
    }
    return -1;
}

int main() {
    int n;
    printf("Enter no of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements in a array: \n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int num=0;
    printf("Enter a number to search via linear search: ");
    scanf("%d", &num);
    printf("Position of %d is %d \n", num, findPositionViaLinearSearch(arr, n, num));
}

