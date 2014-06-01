import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='suzune',
    version='0.1',
    packages=['suzune'],
    url='https://github.com/hirokiky/suzune',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='Command line image registration tool.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tinydb==1.1.0',
    ],
    entry_points={
        'console_scripts': [
            'suzune = suzune.commands:run',
        ],
    },
)
