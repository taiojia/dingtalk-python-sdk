from setuptools import setup, find_packages
from codecs import open
from os import path
import dingtalk_python_sdk

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # the project name
    name='dingtalk-python-sdk',
    version=dingtalk_python_sdk.__version__,
    description='A Python library for the DingTalk',
    long_description=long_description,
    url='https://github.com/jiasir/dingtalk-python-sdk',
    author='jiasir',
    author_email='jiasir@icloud.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='dingtalk python sdk',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
