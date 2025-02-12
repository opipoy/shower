# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from modules.file_managment import *
from flask_cors import CORS, cross_origin

time_file = TimeStoreFile("tst.json")
# creating a Flask app 
app = Flask(__name__) 
CORS(app)

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
@cross_origin(origins="*")
def home(): 
	if(request.method == 'GET'): 

		data = "hello world"
		return jsonify({'data': data}) 


# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 

	return jsonify({'data': num**2}) 


@app.route('/add_usr/<string:name>', methods = ['POST']) 
def add_usr(name):
    time_file.add_user(name)
    return "success"

@app.route('/add_time_usr/<string:name>', methods = ['POST']) 
def add_time_usr(name):
    time_file.add_time(name)
    print(time_file[name].sessions[-1].get_time())
    return "success"

# driver function 
if __name__ == '__main__': 

    app.run(host = "0.0.0.0", debug = True) 

