#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *rev_head = NULL, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	if (fast != NULL)
		slow = slow->next;

	rev_head = prev;
	while (rev_head != NULL && slow != NULL)
	{
		if (rev_head->n != slow->n)
			return (0);
		rev_head = rev_head->next;
		slow = slow->next;
	}

	return (1);
}
