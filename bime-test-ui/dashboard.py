from flask import render_template, Flask
import pyodbc

app = Flask(__name__)
@app.route('/dashboard')    
def index(): 
    connection = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=192.168.66.200,1422;'
        'Database=bimehTest;'
        'UID=BimehTester;'
        'PWD=B@Test409')

    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM TestResult WHERE Date")
    data = cursor.fetchall()   
    return render_template("table.html", data=data)

if (__name__ == '__main__'):
    app.run()