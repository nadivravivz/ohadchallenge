from flask import Flask, render_template, request, jsonify
import socket
import yaml
import json
from jsonpath_ng import jsonpath, parse   

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome<br/>This is web tool that extracts a value from a YAML text based on a path expression"

@app.route("/health")
def health():    
    return render_template('health.html', value=socket.gethostname())

@app.route("/api/yaml_extract",methods = ['POST'])
def yaml_extract():
    try:
        data = request.get_json()
        text = data['text']
        expr = data['expr']
        json_string = json.dumps(yaml.safe_load(text))
        json_data = json.loads(json_string)
        jsonpath_expression = parse(expr)
        match = jsonpath_expression.find(json_data)
        return {"data": match[0].value}
    except:
        return "Error with json file"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5123)