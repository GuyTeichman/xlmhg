from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "xlmhglite.mhg_cython",  # name of the module to be created
        ["xlmhglite/mhg_cython.pyx"],  # file from which it is created
    )
]

setup(
    ext_modules=cythonize(extensions),
)