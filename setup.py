import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension

extensions = [
    Extension(
        "xlmhglite.mhg_cython",  # name of the module to be created
        ["xlmhglite/mhg_cython.pyx"],  # file from which it is created
        include_dirs=[np.get_include()]
    )
]

setup(
    ext_modules=cythonize(extensions),
)
