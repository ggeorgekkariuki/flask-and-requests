from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():

    language = request.args.get('language')
    framework = request.args['framework']
    
    return '''<h1>The language value is {}.</h1>
              <h1> The framework is {}</h1>'''.format(language, framework)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is {}</h1>
        <h1> The framework is {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                Language: <input type="text" name="language"><br>
                Framework: <input type="text" name="framework"><br>
                <input type="submit" value="Submit"><br>
            </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    req_data = request.get_json(force=True)

    print(req_data)

    language = req_data['language']
    framework = req_data['framework']
    website = req_data['website']
    version_info = req_data['version_info']['python']
    examples = req_data['examples'][0]
    boolean_test = req_data['boolean_test']

    return '''
            <h1>The language value is: {}</h1>
            <h1>The framework value is: {}</h1>
            <h1>The website value is: {}</h1>
            <h1>The Python version is: {}</h1>
            <h1>The item at index 0 is: {}</h1>
            <h1>The boolean value is: {}</h1>
            '''.format(language, framework, website, version_info, examples, boolean_test)

if __name__ == '__main__':
    app.run(debug=True)