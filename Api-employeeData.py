from flask import Flask, request, jsonify
import json

app = Flask(__name__)

location = "empData.json"

def get_data(location):
    try:
        with open(location, 'r') as fileData:
            result = json.load(fileData)
            print(result)
        return result
    except FileNotFoundError:
        return None

def get_employee_data(user_data, emp_id):
    for user in user_data['users']:
        if user.get('id') == emp_id:
            return user
    return None  

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/userid', methods=['GET'])
def getDetails():
    user_id = request.args.get('id', type=int)

    if user_id is None:
        return jsonify({"error": "Please provide a valid 'id' parameter."}), 400
    respData = get_data(location)
    user_data = get_employee_data(respData, user_id)

    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found."}), 404

if __name__ == "__main__":
    app.run(debug=True,host=('0.0.0.0'))
