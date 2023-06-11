import io
import os
from os import path
from sys import platform

from setuptools import setup, find_packages, Extension
from wheel.bdist_wheel import bdist_wheel


def get_extra_requires(path, add_all=True):
    import re
    from collections import defaultdict

    with open(path) as fp:
        extra_deps = defaultdict(set)
        for k in fp:
            if k.strip() and not k.startswith('#'):
                tags = set()
                if ':' in k:
                    k, v = k.split(':')
                    tags.update(vv.strip() for vv in v.split(','))
                tags.add(re.split('[<=>]', k)[0])
                for t in tags:
                    extra_deps[t].add(k)

        # add tag `all` at the end
        if add_all:
            extra_deps['all'] = set(vv for v in extra_deps.values() for vv in v)

    return extra_deps


here = path.abspath(path.dirname(__file__))
root = 'xlmhglite'
description = 'XL-mHG lite: A light implementation of the Semiparametric Enrichment Test'
version = '1.0.1'

with open('README.rst', encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

long_description=readme + '\n\n' + history

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split('\n')

ext_modules = []
cmdclass = {}

extras_require = get_extra_requires('requirements_extra.txt')

try:
    # this can fail if numpy or cython isn't installed yet
    import numpy as np
    from Cython.Distutils import build_ext
    from Cython.Compiler import Options as CythonOptions

except ImportError:
    pass

else:
    # tell setuptools to build the Cython extension

    macros = []
    macros.append(('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'))
    ext_modules.append(
        Extension(root + '.' + 'mhg_cython', [root + '/mhg_cython.pyx'],
                  include_dirs=[np.get_include()],
                  define_macros=macros))

    cmdclass['build_ext'] = build_ext


# fix version tag for mac
class CustomBdistWheel(bdist_wheel):
    # source: http://lepture.com/en/2014/python-on-a-hard-wheel
    def get_tag(self):
        tag = bdist_wheel.get_tag(self)
        # print('I\'m running!!! Tag is "%s"' % str(tag))
        if platform == 'darwin':
            repl = 'macosx_10_6_x86_64.macosx_10_9_x86_64.macosx_10_10_x86_64'
            if tag[2] in ['macosx_10_6_x86_64', 'macosx_10_7_x86_64']:
                tag = (tag[0], tag[1], repl)
        return tag


cmdclass['bdist_wheel'] = CustomBdistWheel
# extensions
setup(
    name='xlmhglite',
    version=version,
    python_requires='>=3.8',
    description=description,
    long_description=long_description,
    url='https://github.com/GuyTeichman/xlmhglite',
    author='Guy Teichman',
    author_email='guyteichman@gmail.com',
    license='GPLv3',
    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Cython',
    ],
    keywords=['statistics', 'nonparametric', 'semiparametric', 'enrichment test', 'ranked lists'],
    packages=find_packages(exclude=['docs', 'tests*']),
    # extensions
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    install_requires=requirements,
    extras_require=extras_require,
    tests_require=['pytest'],
    # data
    package_data={
        'xlmhglite': ['xlmhglite/mhg_cython.pyx',
                  'tests/*',
                  'README.rst', 'LICENSE', 'HISTORY.rst'],
    }
)
