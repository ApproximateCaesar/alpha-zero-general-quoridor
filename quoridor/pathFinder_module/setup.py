# Install microsoft build tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# open terminal in folder of setup.py
# To create a .pyd file (which you can import into your scripts) run: python setup.py build_ext --inplace
# The .pyd file is created in the same folder as the .cpp file. Rename the pyd file to "pathFinder.pyd".
# Clean up unneeded files after compilation: python setup.py clean --all
from setuptools import setup, Extension

setup(name='pathFinder', version='1.0',
      ext_modules=[Extension('pathFinder', ['pathFinder.cpp'])])
