from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db_vm_ip",  # Replace with PostgreSQL VM IP
        database="testdb",
        user="testuser",
        password="testpassword"
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Microservice is running!"})

@app.route('/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
