from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    try:
        with open('requirements.txt','r') as f:
            requirement_list = f.readlines()
            
            for line in requirement_list:
                req = line.strip()
                if req and req!='-e .':
                    requirement_list.append(req)

    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Ayush",
    author_email="ayushpoddar351@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)