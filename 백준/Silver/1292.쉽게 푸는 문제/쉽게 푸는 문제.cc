#include <stdio.h>

int calcStrange(int n) {
	int i = 1, j = 1, sum = 0;

	while (n--) {
		sum += i;

		if (i == j) {
			i++;
			j = 0;
		}
		j++;
	}

	return sum;
}

int main(void) {
	int a, b;
	
	scanf("%d %d", &a, &b);

	printf("%d", calcStrange(b)- calcStrange(a - 1));

	return 0;
}