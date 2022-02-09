#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int arr[1001] = {0,};
	int num = 0;

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &arr[i]);
	}

	for (int j = 0; j < num; j++) {
		for (int i = 1; i < num; i++) {
			if (arr[i - 1] > arr[i]) {
				int temp = arr[i];
				arr[i] = arr[i - 1];
				arr[i - 1] = temp;
			}

		}
	}
	for (int i = 0; i < num; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}