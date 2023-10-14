### Django Hands On Project
---

**Project Configuration:**

Creating a Virtual Environment
1. Create a folder
2. Cd to that folder
3. Use this command: to create a virtual environment in that folder
   - **command:** *python3 -m venv venv*
   - **Syntax:** *python3 -m venv 'name of virtual environment'*
   - *It is a good practice to name the virtual enironment as 'venv'*
4. Cd to venv
5. To activate the virtual environment please use the below command:
   - **command:** *source bin/activate*
   - **Syntax:** *source bin/activate*
6. To deactivate the virtual environment please use the below command:
   - **command:** deactivate
   - **Syntax:** deactivate
   - *The virtual environment will be deactivated*

Configuring the Django Environment
1. Open the project in VS Code. Click on the root project folder. File -> Save workspace as -> Give a file name
2. Create a requirements.txt file in the root project folder
3. Enter all the required libraries which you would like to import
   - Example: 
   - `django, djangorestframework, pyyaml, requests, django-cors-headers`
4. **Use this command:** *pip install -r requirements.txt*
   - This downloads all the required dependencies for the project and put them in the external libraries directory
5. **Use this command:** *pip install --upgrade pip*
   - This will update the version of pip
6. To create a home folder to manage the django api end points you can use this: cd to the folder where you want to create the home folder and then type the below command:
   - **command:** *django-admin startproject 'project_name' .*
   - **Example**: *django-admin startproject home .*
7. To start the server in a django project use the following command:
   - **command:** *python manage.py runserver 8000*
8. To create a new app to group your end points and their views logically, use this
   - **command:** *python manage.py startapp 'app_name'*
   - **Example:** *python manage.py startapp api*