from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():

    language = request.args.get('language')
    framework = request.args.get('framework')
    

    return '''<h1>The language value is {} and framework is {}</h1>'''.format(language, framework)

@app.route('/form-example')
def form_example():
    return 'Todo ...'

@app.route('/json-example')
def json_example():
    return 'Todo ...'

if __name__ == '__main__':
    app.run(debug=True)