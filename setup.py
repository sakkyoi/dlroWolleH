from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent

setup(
    name='dlroWolleH',
    version='0.0.1',
    author='sakkyoi',
    description='!dlroWolleH',
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/sakkyoi/dlroWolleH',
)