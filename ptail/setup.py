# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
"""
打包的用的setup必须引入，
"""

VERSION = '0.2.0'

setup(name='ptail',
      version=VERSION,
      description="None",
      author='pythonexam',
      author_email='san332627946@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      entry_points={
        'console_scripts':[
            'ptail = ptail1.tailarg:ptail'
        ]
      },
)