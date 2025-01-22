from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'database': os.getenv('DB_NAME', 'testdb'),
    }
    db_status = "Unable to connect"
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        db_status = f"Connected to database: {db_name[0]}"
    except mysql.connector.Error as err:
        db_status = f"Error: {str(err)}"
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

    return render_template("index.html", db_status=db_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
