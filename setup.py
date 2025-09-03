'''
the setup.py file is an essential part of packaging and distributing python projects it is used by setup toolls 
to define the configration of project such as its dependencies and more 

'''


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirements 
    '''
    requirement_list:List[str]=[]
    try :
        with open('requirements.txt','r') as file:
            ## read lines from the files 
            lines=file.readlines()
            ##process each line 

            for line in lines :
                requirement=line.strip()
                ##ignore the empty lines and -e.
                if requirement and requirement!='-e.':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author="harsh gurnani",
    author_email='harshgurnani88@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)