# Page Object Model Test

## Overview
This project was created using tools to Automation Testing on Web Application, the tools used were Selenium, Pytest , WebDriver Manager following the Page Object Model pattern and using the environment variables

## Setup Instructions
If you know how to clone a repository from github please do it, If you don’t know how do yo do it, please go the following page https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository


1.	Install Python 3.9 or above
2.	Is a good practice to have a virtual environment for each project, with this we can guarantee that a repository after setup it works good, now for to create our own virtual environment we use the following instruction:
    #### Windows Users
    - In your PowerShell terminal we create our virtual environment
    
      `python -m venv <virtual_environment>`
      
    - We activate our virtual environment
    
      `<virtual_environment>/Scripts/activate`
    
    #### MAC Users
    
    - In your terminal we create our virtual environment
    
      `pyenv virtualenv <virtual_environment>`
    
    - We activate our virtual environment
    
      `pyenv activate <name of venv>`
    
3. Now with the virtual environment activated we need to go to the where we clone this repository, and then enter path Page Object Model folder
    
    `/user_path/PageObjectModel/`
    
4. Now we need to install of the requirements with the following command
    
    `pip install -r requirements.txt`
    
5. Then we are gonna set one environment variable that we will use for to open own browser, this project was created for to be used with Chrome, Firefox and Edge browsers, only we need to change the browser name in the following command

   #### Windows Users

      `[Environment]::SetEnvironmentVariable('BROWSER_NAME', 'chrome')`
    
   #### MAC Users
  
      `export BROWSER_NAME=chrome`
      
    
  
   ***Note:***
    
   We can change the browser name for firefox, edge or chrome.
  
6.	Now we can use the pytest framework, that it was installed with the requirements, executing the following commmand

    `pytest .\Test\test_Scenario1.py`
    
    For to test the first scenario or for the second scenario we can execute the following command
    
    `pytest .\Test\test_Scenario2.py`
    
    Or only executing the following command we can execute both scenarios
    
    `pytest`
 
 7.  For to finish we can deactivate the virtual environment
    `deactivate`
 
 ### References
 
 - https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
 - https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html
 
    
    
