#include "python.h" 

static PyObject* file_save(PyObject *self, PyObject *args)
{
	FILE *fptr = fopen("output.txt", "w");
    const char* str=NULL;

    if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 

	fprintf(fptr, "%s\n", str);
	fclose(fptr);

    return Py_BuildValue("i", strlen(str));
}

static PyMethodDef FileMethods[] = {
{"save", file_save, METH_VARARGS,
 "count a string length."},
 {NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 

static struct PyModuleDef filemodule = {
    PyModuleDef_HEAD_INIT,
    "file",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,FileMethods
};

PyMODINIT_FUNC
PyInit_file(void)
{
    return PyModule_Create(&filemodule);
}
