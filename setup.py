from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='tftextembeddinghub',
    version='1.1.0',
    description='TensorFlow Hub module producer for text embedding lookup',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shkarupa-alex/tftextembeddinghub',
    author='Shkarupa Alex',
    author_email='shkarupa.alex@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tftextembeddinghub-convert=tftextembeddinghub.export:main',
        ],
    },
    install_requires=[
        'tensorflow>=1.9.0',
        'tensorflow_hub>=0.1.1',
    ],
    test_suite='nose.collector',
    tests_require=['nose']
)
