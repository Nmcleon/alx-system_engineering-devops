#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - runs an infinite loop for testing
 *
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point for program
 *
 * Return: always 0
 */
int main(void)
{
	int count = 0, pid = 0;

	while (i)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i--;
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
