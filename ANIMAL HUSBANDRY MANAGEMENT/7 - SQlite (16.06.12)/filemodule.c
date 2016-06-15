#include "python.h" 

static PyObject* file_save(PyObject *self, PyObject *args)
{
	FILE *fptr = fopen("output.txt", "w");
    const char* str=NULL;

    if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
         return NULL; 

	fprintf(fptr, "%s\n", str);
	fclose(fptr);

    return Py_BuildValue("i", strlen(str));
}

static PyMethodDef FileMethods[] = {
{"save", file_save, METH_VARARGS,
 "count a string length."},
 {NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 

static struct PyModuleDef filemodule = {
    PyModuleDef_HEAD_INIT,
    "file",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,FileMethods
};

PyMODINIT_FUNC
PyInit_file(void)
{
    return PyModule_Create(&filemodule);
}
