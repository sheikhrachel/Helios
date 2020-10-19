"""Setup file for Helios."""
from setuptools import setup, find_packages
import os

path_to_helios = "/Users/isaacsheikh/Document/GitHub/helios"

setup(name="helios",
      version="1.0.0",
      description="A slack bot that reads, sends, and deletes SQS issues",
      author="Rachel Sheikh",
      author_email='sheikhrachel97@gmail.com',
      platforms=['osx'],
      license=['MIT'],
      url="http://github.com/sheikrachel/helios",
      packages=[pkg for subdir in os.listdir(path_to_helios)
                if os.path.isdir(os.path.join(path_to_helios, subdir))
                for pkg in find_packages(os.path.join(path_to_helios, subdir))],
      install_requires=['requests',
                        'pytest',
                        'pre-commit',
                        'black',
                        'flask',
                        'boto3',
                        'moto'
                        ]
      )
