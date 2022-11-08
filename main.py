from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
# This function checks if adding 'Cherry' was successful
@app.route('/api/update_basket_a')
def updateBasket():

	cursor, connection = 
util.connect_to_db(username, password, host, port, database)

#adds (5, Cherry) into basekt_a
	record = util.run_and_commit_sql(cursor, connection, "INSERT INTO basket_A (a, fruit_a) VALUES (5, 'Cherry')")
		if record == -1:
			print('Something is wrong with the SQL command')
			log = 'ERROR IN SQL or Item is already in basket_a'
		else:
			log = 'Success!'
	util.disconnect_from_db(connection, cursor)
	
return render_template('ErrorChecker.html', log_html = log)

#Displays the table with unique fruit
@app.route('/api/unique')
def table():
	cursor, connection =
util.connect_to_db(username,password,host,port,database)

#Collects fruits from basket_a and basket_b
	record1 = util.run_and_fetch_sql(cursor,"select a, fruit_a, b, fruit_b, from basket_a full join basket_b on fruit_a = fruit_b where a is null of b is null;")
	if record1 == -1:
		print('ERROR')
	else:
		col_names = [desc[0] for desc in cursor.description]
		log = record1[:5]
	util.disconnect_from_db(connection,cursor)
	
	return render_template('index.html', sql_table = log, table_title = col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

