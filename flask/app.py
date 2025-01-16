from flask import Flask, request, render_template
 
app = Flask(__name__)   


@app.route('/', methods =["GET", "POST"])
def func_default():
    if request.method == "POST":
       print(f'\n{request.form}\n')

       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")

       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 

       return f"Your name is {first_name} {last_name}"
    return render_template("form.html")
 

if __name__=='__main__':
   app.run(host='0.0.0.0', debug=True, port=5000)
