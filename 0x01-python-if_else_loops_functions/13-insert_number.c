#include "lists.h"

/**
 * insert_node - inserts a number into a
 * singly linked list
 * @head: pointer to pointer of the
 * head node
 * @number: number to insert
 *
 * Return: address of the inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *new_node, *iterator = *head;

	if (!head || *head == NULL)
		return (add_nodeint_end(head, number));

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	while (iterator && iterator->n < number)
	{
		temp = iterator;
		iterator = iterator->next;
	}
	new_node->next = iterator;
	if (temp)
		temp->next = new_node;
	else
		*head = new_node;
	return (new_node);
}
