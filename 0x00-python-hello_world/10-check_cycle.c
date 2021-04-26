#include "lists.h"

/**
  * check_cycle - A function that checks if a linked list has a cycle in it
  * @list: The list to check
  *
  * Return: !1 if it has a cycle and 0 if it does'nt have a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *current, *head;
