import mysql.connector
import json

from db import getDBCursor, mydb
from TextExtraction.extractContent import extract_content
from inputValidation import validate_integer, validate_url

def upload_file(url, session_cookie):
    # Scrape the article content
    article_content = extract_content(url)

    # Get user ID from session cookie
    user_id = session_cookie.split('-')[0]

    mycursor = getDBCursor()
    
    try:
        # input validation
        if not validate_url(url):
            return None

        # SQL query to insert file into the database
        query = "INSERT INTO files (user_id, body) VALUES (%s, %s)"
        values = (user_id, json.dumps(article_content),)
        
        # Execute the SQL command
        mycursor.execute(query, values)
        
        # Commit the changes
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        mycursor.close()

def get_file_by_id(file_id, session_cookie):
    # Get user ID from session cookie
    user_id = session_cookie.split('-')[0]

    mycursor = getDBCursor()
    
    try:
        # input validation
        if not validate_integer(file_id):
            return None

        # SQL query to get file by ID and user ID
        query = "SELECT * FROM files WHERE id = %s AND user_id = %s"
        values = (file_id, user_id,)
        
        # Execute the SQL command
        mycursor.execute(query, values)
        
        # Fetch the result
        result = mycursor.fetchone()
        
        if result:
            return json.loads(result[2])
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        mycursor.close()

def delete_file_by_id(file_id, session_cookie):
    # Get user ID from session cookie
    user_id = session_cookie.split('-')[0]

    mycursor = getDBCursor()
    
    try:
        # input validation
        if not validate_integer(file_id):
            return None

        # SQL query to delete file by ID and user ID
        query = "DELETE FROM files WHERE id = %s AND user_id = %s"
        values = (file_id, user_id,)
        
        # Execute the SQL command
        mycursor.execute(query, values)
        
        # Commit the changes
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        mycursor.close()

def get_all_file_tittles(session_cookie):
    # Get user ID from session cookie
    user_id = session_cookie.split('-')[0]

    mycursor = getDBCursor()
    
    try:
        if not validate_integer(user_id):
            return None

        # SQL query to get all files by user ID
        query = "SELECT * FROM files WHERE user_id = %s"
        values = (user_id,)
        
        # Execute the SQL command
        mycursor.execute(query, values)
        
        # Fetch the result
        result = mycursor.fetchall()
        
        if result:
            return [{"id": row[0], "title": json.loads(row[2])} for row in result]
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        mycursor.close()
