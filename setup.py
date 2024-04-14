from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='pyls',
version='0.0.1',
description="Linux ls Python Package", 
author='Sk. Atahar Ali',
author_email='ataharsk10@gmail.com',
install_requires=get_requirements('requirements.txt'),
license="MIT",
packages=find_packages(),
entry_points={
        'console_scripts': [
            'pyls = pyls.__main__:expand'
        ]
}
)

"""
from setuptools import setup

setup(
    name='pyls',
    version='0.0.1',
    packages=['pyls'],
    entry_points={
        'console_scripts': [
            'pyls = pyls.__main__:expand'
        ]
    }
)
"""