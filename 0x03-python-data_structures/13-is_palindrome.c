#include "lists.h"

/**
 * is_palindrome - Detects if list is a palindrome
 * @head: The list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int nums[] 
	if (*head == NULL)
		return (1);
}

/**
 * reverse_list - Reverses a linked list
 * @head: The list
 * Return: The reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *new_list;

	if (*head->next != NULL)
		reverse_list(&(*head->next));
	new_list = *head;
	*new_list->next = *head->next;
	return (&new_list);
}
