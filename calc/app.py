from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    "Takes two inputs and returns sum"
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = add(a,b)
    return str(sum)

@app.route("/sub")
def subtraction():
    "Takes two inputs and returns difference"
    a = int(request.args['a'])
    b = int(request.args['b'])
    diff = sub(a,b)
    return str(diff)

@app.route("/mult")
def multiplication():
    "Takes two inputs and returns product"
    a = int(request.args['a'])
    b = int(request.args['b'])
    prod = mult(a,b)
    return str(prod)

@app.route("/div")
def division():
    "Takes two inputs and returns quotient"
    a = int(request.args['a'])
    b = int(request.args['b'])
    quot = div(a,b)
    return str(quot)

@app.route("/math/<operation>")
def more_math(operation):
    "Figure out what operation the user wants, return result based on operation input and number inputs."
    a = int(request.args['a'])
    b = int(request.args['b'])
    # if operation == 'add':
    #     result = add(a,b)
    # elif operation == 'sub':
    #     result = sub(a,b)
    # elif operation == 'mult':
    #     result = mult(a,b)
    # else:
    #     result = div(a,b)
    # return str(result)


# further study

# operations dictionary should work

    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div':div
    }
    result = operations[operation](a,b)
    return str(result)