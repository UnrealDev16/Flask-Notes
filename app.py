from flask import Flask , render_template , request , redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html",tasks=tasks)

@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == 'POST':
        task = request.form.get('note')
        if not task:
            print("LOL")
            return render_template('index.html',error="No Note Inputted",tasks=tasks)
        tasks.append(task)
    return render_template("index.html",tasks=tasks)

@app.route('/remove',methods=['POST','GET'])
def remove():
    if len(tasks) == 0:
        return redirect("/")
    tasks.remove(request.form.get('val'))
    return render_template("index.html",tasks=tasks)

app.run(host='0.0.0.0',port=80,debug=True)