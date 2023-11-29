import pyodbc
from datetime import date
def db(Category,Title, date,time, duration, msg):
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=192.168.66.200,1422;'
        'Database=bimehTest;'
        'UID=BimehTester;'
        'PWD=B@Test409'
        
    )

# Creating a cursor object using the cursor() method
    cursor = conn.cursor()

# Creating table as per requirement
    try:
        sql = '''CREATE TABLE TestResult(
        Id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
        Category VARCHAR(20) NULL,
        Title VARCHAR(20) NULL,
        Date VARCHAR(20) NULL,
        Time VARCHAR(20) NULL,
        Duration VARCHAR(20) NULL,
        Result VARCHAR(50) NULL
        )'''
        cursor.execute(sql)
    except:
        pass

    sql = "INSERT INTO TESTRESULT (Category, Title , Date ,Time, Duration , Result) VALUES (?,?, ?, ?, ?, ?)"
    val = (Category,Title, date,time, duration, msg)

    cursor.execute(sql, val)
# Commit your changes in the database
    conn.commit()

# Closing the connection
    conn.close()





