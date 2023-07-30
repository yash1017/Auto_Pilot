from setuptools import find_packages,setup
from typing import List

def get_req(file_path:str)->List[str]:
    '''
    This will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name='AI AutoPilot',
    version='0.0.1',
    author='Dileep Kumar',
    author_email='dileepkumarreddymanchala@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
    
    
    
)
