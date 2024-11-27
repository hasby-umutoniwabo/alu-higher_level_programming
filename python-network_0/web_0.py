#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/route_5', methods=['GET'])
def route_5():
    # Get the value of the custom header 'X-HolbertonSchool-User-Id'
    user_id = request.headers.get('X-HolbertonSchool-User-Id')
    
    # Print the headers for debugging purposes
    print("Received Headers:", request.headers)
    
    # Validate the header value
    if user_id == "98":
        return "OK"
    else:
        return "NOP"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
