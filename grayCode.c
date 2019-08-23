/*https://leetcode.com/problems/gray-code/*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define EXIT_SUCCESS 0
#define MEM_ALLOC_ERR 1

int *grayCode(int n);
void *allocate(size_t size);

int main()
{
	printf("Enter a non-negative integer and this program will output the "
	"associated gray code.\nGray code is a binary sequence where two "
	"successive values differ by a single bit.\n");
	char buffer[20];
	int val = 0, i = 0, length = 0, *gray;
	while(fgets(buffer, 20, stdin)[0]!='\n')
	{
		buffer[strlen(buffer)-1] = '\0';
		sscanf(buffer, "%d", &val);
		length = (int)pow(2.0, (double)val);
		gray = grayCode(val);
		for(i=0; i<length; i++)
		{
			printf("%d ", gray[i]);
		}
		printf("\n");
		free(gray);
	}
	return EXIT_SUCCESS;
}

int *grayCode(int n)
{
	/*The total size of the sequence is 2^n*/
	int i = 0, length = (int)pow(2.0, (double)n), *seq = allocate(sizeof(int)*length);
	/*Start sequence, shift right 1 then toggle the number, i,
	continue this process 2^n times*/
	for(i=0; i<length; i++)
	{
		seq[i] = i^(i>>1);
	}
	return seq;
}

void *allocate(size_t size)
{
	void *ptr = malloc(size);
	if(!ptr)/*Null pointer*/
	{
		printf("Error allocating %lu bytes\nEXITING", size);
		exit(MEM_ALLOC_ERR);
	}
	return ptr;
}