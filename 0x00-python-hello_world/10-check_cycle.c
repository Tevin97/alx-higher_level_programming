#include "lists.h"

/*
 * check_cycle: Checks if a singly linked list contains a cycle.
 * @list: A pointer to the head of the linked list.
 * Return: 1 if list contains, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
