# ATTENDANCE MANAGEMENT SYSTEM IN DJANGO

## Overview
This is an attendance management system implemented as a learning assignment to practice Django. This app utilizes Python and Django as the backend and HTML,CSS,Javascript and Bootstrap for the front end.

## Installation
1. Clone this repository using the following command :-
```bash
git clone https://github.com/vkEnine/attendance-V2.git
```

2. Ensure that you have created your virtual environment.
+ For Windows users, `virtualenv env_name`
+ For Linux System users, `/usr/bin/python3 -m venv env_name` 

3. Activate Your virtual environment. 
+ For Windows users, `env_name\Scripts\activate`
+ For Linux System users, `source env_name/bin/activate`

4. Install all the necessary dependencies using the requirements file in this repository using the following command.
```bash
pip install -r requirements.txt
```

5. Run the server using the following command,
```bash
python3 manage.py runserver
``` 

6. Follow the link,  then add  "home/" in the end of the url to be directed to the home or incase of a new user, the login and register page.Go to a new tab in your browser, copy the base url and add a "home/" endpoint to it.The url will look something like this `http:127.0.0.1:8000/login/`


## Usage
1. Register as a new user, and while setting the password, keep in mind the following things for a successful registration.
+ The password should be atleast 8 characters long.
+ It should not be entirely numeric.
+ include atleast one number,one letter and one special character.

2. After a succesful registration, you will be directed to the login page. after login with the right credentials, you will see the home page.

3. In order to add employees, You need to access the django admin which will add the user and dynamically create record for the new employee. To access the admin portal, follow the steps below,
+ Create a superuser by typing this command in the terminal.
```python3 manage.py createsuperuser```
+ Set up a username, email and password.
+ Go to a new tab, copy the base url and add a "admin/" endpoint to it.
The url will look something like this `http:127.0.0.1:8000/admin/`

4. Add a new employee in The `User models` table under `App_V2` category. Then, that employee will show up on your home page.

5. Now you can mark your employees attendance using the dropdowns for each date.

6. Once done, Logout by clicking the sign out button in the dropdown at the top left corner near the username. 
