from flask import Flask,render_template, request,redirect,flash, jsonify
app = Flask(__name__)

app.secret_key = "thisiseasy"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ajax_update',methods=['POST'])
def handle_update():
    from random import randint as ri
    val = ri(1,100)
    return jsonify({ 'value' : val })

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return validate_user(request)
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        import time
        time.sleep(3)
        if name and email and password and phone:
            # save in database
            return jsonify({'status':'success'})
        else:
            # show error to user
            return jsonify({'status':'invalid form data'})

    return render_template('register.html')

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