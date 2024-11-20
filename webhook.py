from flask import Flask, request, jsonify, json

app = Flask(__name__)

def query(intent, parameters):
    res = ""
    task = intent["displayName"]
    for key, value in parameters.items():
        path = f"{task}/{value}.txt"
        print("path is " + path)
        with open(path, 'r') as file:
            content = file.read()
            res += content
    return res;

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Request recieved")
    req = request.get_json(silent=True, force=True)
    queryResult = req["queryResult"]
    intent = queryResult["intent"]
    parameters = queryResult["parameters"]
    result = query(intent, parameters)
    return jsonify({
        "fulfillmentText": result
    })

print("File is running")
app.run(port=8000, threaded=True)
