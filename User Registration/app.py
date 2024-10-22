from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='U.A.2.12'
app.config['MYSQL_DB']='register'


my_sql=MySQL(app)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        name=request.form['name']
        id=request.form['id']
        email=request.form['email']
        city=request.form['city']

        cur=my_sql.connection.cursor()

        cur.execute('INSERT INTO Info(Name,ID,Email,City) VALUES(%s,%s,%s,%s)',(name,id,email,city))

        my_sql.connection.commit()

        cur.close()

        return 'Success'
    return render_template('register.html')

@app.route('/users')
def use():

    cur=my_sql.connection.cursor()

    users=cur.execute('SELECT * FROM Info ORDER BY Name ASC')

    if users>0:
        usersDetail=cur.fetchall()
    
    return render_template('users.html',usersDetail=usersDetail)


if __name__=='__main__':
    app.run(debug=True)