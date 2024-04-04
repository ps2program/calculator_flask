from flask import Flask, jsonify, request
from calculator.add import add
from calculator.subtract import subtract
from calculator.multiply import multiply
from calculator.divide import divide
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

@app.route('/add', methods=['GET'])
def addition():
    x = int(request.args.get('x', 0))
    y = int(request.args.get('y', 0))
    result = add(x, y)
    return jsonify({"result": result})

@app.route('/subtract', methods=['GET'])
def subtraction():
    x = int(request.args.get('x', 0))
    y = int(request.args.get('y', 0))
    result = subtract(x, y)
    return jsonify({"result": result})

@app.route('/multiply', methods=['GET'])
def multiplication():
    x = int(request.args.get('x', 0))
    y = int(request.args.get('y', 0))
    result = multiply(x, y)
    return jsonify({"result": result})

@app.route('/divide', methods=['GET'])
def division():
    x = int(request.args.get('x', 0))
    y = int(request.args.get('y', 1))  # Avoid division by zero
    result = divide(x, y)
    return jsonify({"result": result})


# if __name__ == '__main__':
#     app.run(debug=True)


# Now, when you run this Flask application, you can access the routes:

# /add?x=<value>&y=<value>
# /subtract?x=<value>&y=<value>
# /multiply?x=<value>&y=<value>
# /divide?x=<value>&y=<value>

# Replace <value> with the values you want to perform the operation on. For example:

# http://localhost:5000/add?x=10&y=5
# http://localhost:5000/subtract?x=10&y=5
# http://localhost:5000/multiply?x=10&y=5
# http://localhost:5000/divide?x=10&y=5
