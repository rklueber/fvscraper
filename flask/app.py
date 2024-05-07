import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL

app = Flask(__name__)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'scraper'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'prices'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/prices')
def prices():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT isin, datafrom, price, currency FROM prices ORDER BY datafrom DESC LIMIT 10")
        pricesRows = cursor.fetchall()
        response = jsonify(pricesRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        return jsonify({"error": "Unable to fetch data"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/prices/<isin>')
def pricesIsin(isin):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT isin, datafrom, price, currency FROM prices WHERE isin=%s ORDER BY datafrom DESC LIMIT 30", (isin,))
        pricesRows = cursor.fetchall()
        response = jsonify(pricesRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        return jsonify({"error": "Unable to fetch data for ISIN"}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
