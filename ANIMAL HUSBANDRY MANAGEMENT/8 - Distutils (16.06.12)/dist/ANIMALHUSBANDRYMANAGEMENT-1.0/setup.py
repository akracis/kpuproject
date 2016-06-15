from distutils.core import setup, Extension

spam_mod = Extension('file', sources = ['filemodule.c'])
setup(name='ANIMALHUSBANDRYMANAGEMENT',
      version='1.0',
      py_modules=['execute8','main8','menu8','mysmtplib']
      )
