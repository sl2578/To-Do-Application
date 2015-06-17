import datetime
from flask import Flask, json, request, session, redirect, url_for, abort, render_template, flash
from contextlib import closing
from flask.ext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'user1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tsevwh'
app.config['MYSQL_DATABASE_DB'] = 'tododb'
app.config['MYSQL_DATABASE_HOST'] = '23.253.70.25'
app.config['MYSQL_DATABASE_PORT'] = 3306
db = MySQL()
db.init_app(app)

# ROUTES
# Index page gets passed on information about tasks
@app.route("/")
def index():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.callproc('get_table', ())
    tasks = [dict(id=row[0], title=row[1], descr=row[2], done=row[3], dline=row[4], finish=row[5]) for row in cursor.fetchall()]
    cursor.close() 
    conn.close()
    return render_template('index.html', tasks=tasks)


# Adds new task to list and stores relevant information
@app.route('/add', methods=['POST'])
def add_entry():
    _title = request.form['title']
    _descr = request.form['descr']
    _dline = request.form['dline']
    _done = 0

    if _title and _descr and _dline:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.callproc('add_task', (_title, _descr, _done, _dline))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            cursor.close() 
            conn.close()  
            return redirect(url_for('index'))
        else: 
            return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


# Deletes task from either lists
@app.route('/delete', methods=['POST']) 
def delete_task():
    _id = request.form['task_to_delete']
    conn = db.connect()
    cursor = conn.cursor()
    cursor.callproc('delete_task', (_id))
    conn.commit()
    cursor.close() 
    conn.close()    
    return redirect(url_for('index'))

# Moves task from unfinished to finished
@app.route('/move', methods=['POST'])
def move_task():
    _id = request.form['task_to_move']
    _finish = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    conn = db.connect()
    cursor = conn.cursor()
    cursor.callproc('move_task', (_id, _finish))
    conn.commit()
    cursor.close() 
    conn.close()
    return redirect(url_for('index'))

# INITIALIZATION
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
