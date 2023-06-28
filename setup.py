from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
        Returns list of libraries from filepath
    '''
    requirements = []
    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip() != '-e .']
    return requirements

setup(
    name='ml_pipe',
    author='Etietop Abraham',
    author_email='etietopdemasabraham@gmail.com',
    packages=find_packages(),
    description='machine learning pipes',
    install_requires=get_requirements('requirements.txt')
)