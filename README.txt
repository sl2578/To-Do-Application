# ToDoApplication
Install the required libraries, preferably using pip and virtualenv:
    i. Download `pip` and `virtualenv`
        $ sudo easy_install pip
        $ sudo pip install virtualenv
    ii. Create an isolated environment with `virtualenv`:
        $ virtualenv --no-site-packages env
        $ source env/bin/activate
    iii. Install dependencies with `pip`:
        $ pip install -r requirements.txt

Then in the shell, run the python file 'main.py' in the project home directory and the application will
         greet you on http://localhost:5000/
