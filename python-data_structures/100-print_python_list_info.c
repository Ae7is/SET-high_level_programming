#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: PyObject pointer to a Python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size;
	Py_ssize_t i;
	const char *type_name;

	list = (PyListObject *)p;
	size = Py_SIZE(list);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type_name = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
