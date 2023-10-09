#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_list - reverses a list
 * @head: pointer to the head node
 * of the list to reverse
 *
 * Return: pointer to the new head
 * node of reversed list
 */

void reverse_list(listint_t **head)
{
	listint_t *iterator = *head, *next = NULL, *prev = NULL;

	while (iterator)
	{
		next = iterator->next;
		iterator->next = prev;
		prev = iterator;
		iterator = next;
	}
	*head = prev;
}

/**
 * get_size - counts number of nodes.
 * @head: pointer to the head node
 *
 * Return: size of list
 */

int get_size(listint_t *head)
{
	listint_t *iterator = head;
	int count = 0;

	while (iterator)
	{
		count++;
		iterator = iterator->next;
	}
	return (count);
}

/**
 * dup_list - duplicates the list
 * @head: head node pointer
 *
 * Return: pointer to the new head of duplicated list
 */

listint_t *dup_list(listint_t *head)
{
	listint_t *iterator = head, *dup_head;

	dup_head = NULL;
	while (iterator)
	{
		add_nodeint_end(&dup_head, iterator->n);
		iterator = iterator->next;
	}
	return (dup_head);
}
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to pointer to head node
 *
 * Return: 1 if palindrome 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *last = NULL, *once = *head,
		  *twice = *head, *temp = *head;

	if (!(*head) || !(*head)->next)
		return (1);

	while (1)
	{
		twice = twice->next->next;
		if (!twice)
		{
			last = once->next;
			break;
		}
		if (!twice->next)
		{
			last = once->next->next;
			break;
		}
		once = once->next;
	}
	reverse_list(&last);

	while (last && temp)
	{
		if (last->n == temp->n)
		{
			last = last->next;
			temp = temp->next;
		} else
			return (0);
	}
	if (!last)
		return (1);

	return (0);
}
