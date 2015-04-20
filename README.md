# ToDoApplication

Hi Joe,

For my To-Do Application, I used the Flask framework, so in order to run the app, you may need to download Flask. Here are some instructions written by others online on installation:

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

-----------

Now I will describe my implementation briefly. I included a button for adding a task at the top of the page, that opens a form that takes in the task name, description, and deadline. Clicking the "add" button will add the new task to the top of the incomplete list. Each item in the list can be expanded by simply clicking on the name of the task. In that view, you can see the description and the deadline date, and there is an option to either delete or move it to the completed list. Once the task is moved to the completed list, you can click on the title to see its description and the date/time completed, in addition to a delete button.   

The web app uses a SQLite database that we create in the tmp folder.   
* Note: Some issues may arise if the database is not reset manually between changes to main.py.  

If I were to expand this web application, I would make sure to include form validation, a separate viewer for the current task selected, an option to restore a completed task back to the incomplete list, and a functionality to prioritize certain tasks. 
# To-Do-Application
# To-Do-Application
