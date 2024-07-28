from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',  # replace with your MySQL username
    'password': 'Trushant@2001',  # replace with your MySQL password
    'host': 'localhost',
    'database': 'quiz_competition'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    student_id = data['student_id']
    score = data['score']
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (student_id, score) VALUES (%s, %s)", (student_id, score))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Score submitted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to connect to the database'}), 500

@app.route('/get_scores/<student_id>', methods=['GET'])
def get_scores(student_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM scores WHERE student_id = %s", (student_id,))
        scores = cursor.fetchall()
        cursor.close()
        conn.close()
        if scores:
            return jsonify({'student_id': student_id, 'scores': scores}), 200
        else:
            return jsonify({'message': 'No scores found for this student'}), 404
    else:
        return jsonify({'message': 'Failed to connect to the database'}), 500

if __name__ == '__main__':
    app.run(debug=True)
