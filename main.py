from flask import Flask,render_template, request,redirect,flash
app = Flask(__name__)

app.secret_key = "thisiseasy"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return validate_user(request)
    return render_template('login.html')

def validate_user(request):
    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        # check db for email and password
        flash("logged in successfully",'success')
        return redirect('/')
    else:
        flash("No details provided",'danger')
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)