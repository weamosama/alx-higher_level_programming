#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *insert_node - Inserts a number into a sorted singly linked list.
 *@head: Pointer to the head of the list.
 *@number: The number to be inserted
 *Return: The address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *c;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	c = *head;

	while (c->next != NULL && c->next->n < number)
		c = c->next;

	new_node->next = c->next;
	c->next = new_node;

	return (new_node);
}
