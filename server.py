from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def root():


    return render_template('index.html')

@app.route('/return', methods=['POST'])
def gohome():
    return redirect('/')

@app.route('/users', methods=['POST'])
def user_data():
    print 'received the post data!'
    
    if '_flashes' in session:
        session.pop('_flashes', None)
    
    errors = 0

    if len(request.form['email']) < 1:
        flash('Email cannot be empty!','error')
        errors+=1
        #return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        errors+=1
        #return redirect('/')
    else:
        email = request.form['email']
    
    if len(request.form['fname']) < 1:
        flash('First name cannot be empty!')
        errors+=1
        #return redirect('/')
    elif not request.form['fname'].isalpha():
        flash("First name should be alpha only")
        errors+=1
        #return redirect('/')
    else:
        fname = request.form['fname']


    if len(request.form['lname']) < 1:
        flash('Last name cannot be empty!')
        errors+=1
        #return redirect('/')
    elif not request.form['lname'].isalpha():
        flash("First name should be alpha only")
        errors+=1
        #return redirect('/')
    else:
        lname = request.form['lname']

    if len(request.form['pass']) < 9:
        flash('Password should be more than 8 characters!')
        errors+=1
        #return redirect('/')
    else:
        password = request.form['pass']
        
    if len(request.form['pass_confirm']) < 9:
        flash('Password confirm should be more than 8 characters!')
        errors+=1
        #return redirect('/')
    else:
        pass_confirm = request.form['pass_confirm']
    
    if password != pass_confirm:
        flash('Password does not match password confirmation')
        errors+=1
        #return redirect('/')

    if errors > 0:
        print "Number of errors:",errors
        return redirect('/')
    else:
        return render_template('showData.html', email = email,fname = fname, lname = lname)

app.run(debug=True)