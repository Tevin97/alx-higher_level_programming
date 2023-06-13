#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: A pointer to a PyObject that represents a Python list object
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyObject *obj;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
