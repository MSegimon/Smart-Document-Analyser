import mysql.connector
import json

from db import getDBCursor, mydb
from TextExtraction.cleanText import filter_content, generate_json_from_content
from TextExtraction.webScrapper import scrape_article_content

def extract_content(url):
    # Scrape the article content
    article_content = scrape_article_content(url)
    
    # Filter the content
    filtered_content = filter_content(article_content)
    
    # Generate JSON from the filtered content
    json_content = generate_json_from_content(filtered_content)
    
    return json_content

def upload_file(url, session_cookie):
    # Scrape the article content
    article_content = extract_content(url)

    # Get user ID from session cookie
    user_id = session_cookie.split('-')[0]

    mycursor = getDBCursor()
    
    try:
        # SQL query to insert file into the database
        query = "INSERT INTO files (user_id, body) VALUES (%s, %s, %s)"
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
