from flask import Flask, request

app = Flask(__name__)

@app.route('/route_5', methods=['GET'])
def route_5():
    # Get the value of the custom header 'X-HolbertonSchool-User-Id'
    user_id = request.headers.get('X-HolbertonSchool-User-Id')
    
    # Validate if the header value matches 98
    if user_id == "98":
        return "OK"  # Correct output if the header is valid
    else:
        return "NOP"  # Return "NOP" if the header is incorrect

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
