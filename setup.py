from setuptools import find_packages,setup #IMPORT ALL THE ML PACKAGES
from typing import List
HYPEN_E_DOT = '-e .' #TO MAP TO setup.py

def get_requirements(file_path: str)->List[str]:
    '''
    It will return the List of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # Here a \n will also get added so to remove that next Line
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
setup(
name= 'WaterQualityCheck',
version= '0.0.1',
author = 'ayush',
author_email='ayushgoyat17@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')

)