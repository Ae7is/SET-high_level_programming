#include "lists.h"

/**
 * get_middle - finds the middle node of a linked list using
 * slow/fast pointers
 * @head: pointer to the head of the list
 * Return: pointer to the middle node
 */
listint_t *get_middle(listint_t *head)
{
	listint_t *slow;
	listint_t *fast;

	slow = head;
	fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list to reverse
 * Return: pointer to the new head (old tail) of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev;
	listint_t *current;
	listint_t *next_node;

	prev = NULL;
	current = head;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle;
	listint_t *second_half;
	listint_t *first_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	middle = get_middle(*head);
	second_half = reverse_list(middle);
	first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
