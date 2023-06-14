#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	const char *typeName = NULL;
	Py_ssize_t size;
	Py_ssize_t i;

	size = PyList_Size(p);

	if (!PyList_Check(p))
	{
		printf("Invalid Python list object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the list = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyBytes_Check(p))
	{
		printf("Invalid Python bytes object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size > 10)
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
