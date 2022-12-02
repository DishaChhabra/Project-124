from flask import Flask,jsonify, request

app1 = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact_name': u'A',
        'phone_number': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'contact_name': u'B',
        'phone_number': u'7896543210', 
        'done': False
    }
 ]


@app1.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'contact_name': request.json['Name'],
        'phone_number': request.json.get('Phone Number', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app1.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app1.run(debug=True)