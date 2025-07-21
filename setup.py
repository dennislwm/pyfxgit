from os import path
from setuptools import setup

# read the contents of your README file
strCwd = path.abspath(path.dirname(__file__))
with open(path.join(strCwd, 'README.md'), encoding='utf-8') as f:
  strDesc = f.read()

# setup details
# 0.1.0 version
# ┬ ┬ ┬
# │ │ └─────────────── test version
# │ └──────────────────── minor version
# └───────────────────────── major version
setup(name='pyfxgit',
  version='0.1.0',
  description='This is a package of helper classes and libraries.',
  packages=['pyfxgit'],
  install_requires=['matplotlib==3.9.4','mpl_finance','numpy==2.0.2','pandas==2.3.1'],
  author='Dennis Lee',
  author_email='dennislwm@gmail.com',
  url="https://github.com/dennislwm/pyfxgit", 
  long_description=strDesc,
  long_description_content_type='text/markdown',
  license="MIT", 
  zip_safe=False
)
