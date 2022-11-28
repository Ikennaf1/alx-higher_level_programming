#include "lists.h"

/**
 * check_cycle - Checks if a list has a cycle
 * @list: The given list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	int result = 0;
	listint_t *temp = list;

	while (temp->next != NULL)
	{
		if (temp->next == list)
		{
			result = 1;
			break;
		}
		temp = temp->next;
	}
	return (result);
}
