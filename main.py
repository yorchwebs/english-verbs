from flask import Flask, render_template, request
import pymysql

# Creating a Flask object called `app`
app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

# This function connects to the database and returns the connection object
# :return: A connection to the database.
def connection():
    s = 'localhost'
    d = 'english_verb_list' 
    u = 'root'
    p = 'XXXXXXXX'
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

# It connects to the database, gets all the verbs, and then renders the index.html template with the verbs
# :return: The index.html file is being returned.
@app.route('/', methods=['GET', 'POST'])
def main():
    verbs = []
    conn = connection()
    cursor = conn.cursor()
    if request.method=="POST" and 'txtsearch' in request.form:
        cursor.execute("SELECT * FROM regular_irregular_verbs WHERE UPPER(simple_form) LIKE '%" + request.form['txtsearch'] + "%'")
    else:
        cursor.execute("SELECT * FROM regular_irregular_verbs")
    verbs = cursor.fetchall()
    conn.close()
    return render_template("index.html", verbs = verbs)

# Checking if the file is being run directly or if it is being imported.
if(__name__ == "__main__"):
    # Running the app.
    app.run(port = PORT, debug = True)