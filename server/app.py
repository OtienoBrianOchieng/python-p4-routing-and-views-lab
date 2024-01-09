#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<str:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1> {parameter} </h1>' 

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [f'<p>{i}</p>' for i in range (parameter + 1)]:
    
    numbers_html = ''.join(numbers)
    
    return numbers_html
    
@app.route('/math/<num1><operation><num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p> Error: Division by Zero</p>'
    elif operation == '%':
        result = num1 % num2
    else: 
        return '<p>Error: Invalid operation <p/>'





if __name__ == '__main__':
    app.run(port=5555, debug=True)
