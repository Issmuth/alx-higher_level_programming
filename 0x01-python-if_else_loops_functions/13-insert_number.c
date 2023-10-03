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
	listint_t *temp, *new_node, *iterator = *head;

	if (!head || !(*head))
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	while (iterator->n < number && iterator)
	{
		temp = iterator;
		iterator = iterator->next;
	}
	new_node->next = iterator;
	temp->next = new_node;
	return (new_node);
}
