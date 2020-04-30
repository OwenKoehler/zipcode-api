import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_zip():
	try:
		_json = request.json
		_zip = _json['zip']
		# validate the received values
		if _zip and request.method == 'POST':
			sql = "INSERT INTO zipcodes(zip) VALUES(%s)"
			data = (_zip)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Zip added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/zips')
def zips():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM zipcodes")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:zip>')
def delete_zip(zip):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM zipcodes WHERE zip=%s", (zip,))
		conn.commit()
		resp = jsonify('Zip deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()