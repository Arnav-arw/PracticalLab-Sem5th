#include<stdio.h>

int findPositionViaBinarySearch(int arr[], int size, int key) {
    int low = 0, high = size - 1, mid;
    while (low <= high) {
        mid = (low + high)/2;
        if (arr[mid] == key) {
            return mid + 1;
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
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
    printf("Enter a number to search via binary search: ");
    scanf("%d", &num);
    printf("Position of %d is %d \n", num, findPositionViaBinarySearch(arr, n, num));
}