#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the linked list
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *previous = NULL;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (current == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	new_node->next = current;

	if (previous == NULL)
		*head = new_node;
	else
		previous->next = new_node;
	return (new_node);
}
