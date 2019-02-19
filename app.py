from flask import Flask, render_template, request
from create_table import *
  

app = Flask(__name__)

#CORS(app, support_credentials=True)
  
  
@app.route("/" , methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        mock_variable = "hello"
        return render_template('template.html', mock_variable=mock_variable)
        
    elif request.method == "POST":
        if 'task_title' in request.form:
            form_data = request.form
            task_title = form_data.get('task_title', "")
            task_description = form_data.get('task_description', "")
            status = form_data.get('status', "")
            important = form_data.get('important', "")
            date = form_data.get('date', "")
            form_data = [{'title': task_title,'description': task_description, 'status':status, 'important': important, 'date':date}]
            
            create_task = add_data_to_table("tasks", form_data, ["title", "description", "status", "important", "date"])
            message_to_user = "Task titled {} has been added to  calender".format(task_title)
            return render_template("template.html", form_data=form_data, message_to_user=message_to_user )
    else:
        return render_template("template.html", mock_variable="No Response")

if __name__ == "__main__":
    app.run(debug=True)



#get all data in db



#delete version
@app.route("/<int:taskid>" , methods=['DELETE'])
def home():
    if request.method=="GET":
        if 'task_title' in request.form:
            form_data = request.form
            task_title = form_data.get('task_title', "")
            task_description = form_data.get('task_description', "")
            status = form_data.get('status', "")
            important = form_data.get('important', "")
            date = form_data.get('date', "")
            form_data = [{'title': task_title,'description': task_description, 'status':status, 'important': important, 'date':date}]
            create_task = add_data_to_table("tasks", form_data, ["title", "description", "status", "important", "date"])
            message_to_user = "Task titled {} has been added to  calender".format(task_title)
            return render_template("template.html", form_data=form_data, message_to_user=message_to_user )
    else:
        return render_template("template.html", mock_variable="No Response")

if __name__ == "__main__":
    app.run(debug=True)







