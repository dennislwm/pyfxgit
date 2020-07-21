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
setup(name='pyplus',
  version='0.1.0',
  description='This is a package of helper classes and libraries.',
  packages=['pyplus'],
  install_requires=['matplotlib==3.2.2','mpl_finance'],
  author='Dennis Lee',
  author_email='dennislwm@gmail.com',
  URL="https://github.com/dennislwm/pyplus", 
  long_description=strDesc,
  long_description_content_type='text/markdown',
  license="MIT", 
  zip_safe=False
)
