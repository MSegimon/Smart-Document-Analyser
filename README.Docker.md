### Building and running your application

#### Prerequisites
Before you start, make sure you have Docker installed on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

You also need to have a mysql database running. You should have a `mysql` service running on your machine with the following structure:
- Database name: `DocumentAnalyser`
- User table:
```
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    session_cookie TEXT,
    session_cookie_timestamp INTEGER
);
```
- File table:
```
CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    body TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

You also need to create the db.py file in the `app` directory with the following content:
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="<user>",
  password="<password>"
)

def getDBCursor():
    mycursor = mydb.cursor()
    mycursor.execute("USE DocumentAnalyser")
    return mycursor
```


#### Building your application
When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.
