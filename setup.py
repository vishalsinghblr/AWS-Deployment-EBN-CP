from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=[req.replace('\n','') for req in f.readlines()]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='mlproject',
    version='0.0.1',
    author='vishal',
    author_email='vishal.singh2114@gmail.com',
    packaged=find_packages(),
    install_requires=get_requirements('requirements.txt')
)