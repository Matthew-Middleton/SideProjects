/*https://leetcode.com/problems/rotate-image/*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define EXIT_SUCCESS 0

/*Reads input from stdin and returns a number*/
int input(void);
/*Populates an array of size n with random integers*/
void popArr(int n, int *image);
/*Rotates an array by -pi/2*/
void rotateCounter(int n, int *image);
/*Swaps the elements in an array*/
void swap(int pos1, int pos2, int *arr);
/*Prints an array of integers of size n*/
void printArr(int n, int *image);

int main()
{
	char buffer[20];
	int val = 0;
	printf("Enter the size for the nxn matrix:\n");
	fgets(buffer, 20, stdin);
	val = strlen(buffer);
	buffer[strlen(buffer)-1] = '\0';
	sscanf(buffer, "%d", &val);
	int image[val][val];
	popArr(val, *image);
	printArr(val, *image);
	printf("\n\n");
	rotateCounter(val, *image);
	printArr(val, *image);
	return EXIT_SUCCESS;
}

void popArr(int n, int *image)
{
	int i = 0, j = 0;
	srandom(time(NULL));
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
		{
			//image[i][j] = random()%100;
			*(image+(i*n+j)*sizeof(int)) = random()%100;
		}
	}
}
/*Start by swapping each element in the array (x,y) with (y,x),
then swap each element in the row started and the ends until
they converge at the middle*/
void rotateCounter(int n, int *image)
{
	int i = 0, j = 0, left = 0, right = n-1;
	/*Swap each element in the array, (x,y) with (y,x) and vice-versa*/
	for(i=0; i<n; i++)
	{
		for(j=0; j<i; j++)
		{
			swap(i*n+j, j*n+i, image);
		}
	}
	/*Swap each element in the row going in from the endpoints,
	converging at the center*/
	for(; left<right; left++, right--)
	{
		for(i=0; i<n; i++)
		{
			swap(i*n+left, i*n+right, image);
		}
	}
}

void swap(int pos1, int pos2, int *arr)
{
	int temp = *(arr+pos1*sizeof(int));
	*(arr+pos1*sizeof(int)) = *(arr+pos2*sizeof(int));
	*(arr+pos2*sizeof(int)) = temp;
}

void printArr(int n, int *image)
{
	int i = 0, j = 0;
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
		{
			printf("%d ", *(image+(i*n+j)*sizeof(int)));
		}
		printf("\n");
	}
}