from flask import Flask, request, render_template
from dbm import deleteData, insertData, showData
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_student")
def add_student():
    return render_template("add_student.html")

@app.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
    name = request.form["name"]
    email = request.form["email"]
    gender = request.form["gender"]
    contact = request.form["contact"]
    dob = request.form["dob"]
    address = request.form["address"]
    t = (name,email,gender,contact,dob,address)
    insertData(t)
    return render_template("success_record.html")



@app.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")



@app.route("/student_info")
def student_info():
    rows = showData()
    return render_template("student_info.html",rows = rows)

@app.route("/deleterecord",methods = ["post"])
def deleterecord():
    id = request.form["id"]
    deleteData(id)
    return render_template("delete_record.html")
        
if __name__ == "__main__":
    app.run(debug = True)  
