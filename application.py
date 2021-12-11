from os import name
from flask import Flask,render_template,request
import flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sachin:rockey123@localhost:3306/c2"

db = SQLAlchemy(application)

import model.Account as Account
import model.Lone as Lone
import model.User as User

db.create_all()
db.session.commit()

@application.route('/')
def index():
    return render_template('index.html.j2')


@application.route("/start",methods=['POST'])
def get_start():
    if(request.method == 'POST'):
        nic = request.form.get('nic')
        username = request.form.get('username')
        print(nic,username)
        if(nic != None or username != None):
            exists = db.session.query(User.User.nic).filter_by(nic=nic).first() is not None
            print(exists)
            if(exists != False):
                user = db.session.query(User.User).filter_by(nic=nic).first()
                print(user,"asdasd")
                jsonData = { 'nic':user.nic,'user_name':user.user_name,'balance':user.balance }
                return render_template('home.html.j2',context=jsonData)
            else:
               newUser = User.User(nic=nic,user_name=username,balance=0,is_guarantee=False)
               db.session.add(newUser)
               db.session.commit()
               user = db.session.query(User.User).filter_by(nic=nic).first()
               print(user)
               jsonData = { 'nic':user.nic,'user_name':user.user_name,'balance':user.balance }
               return render_template('home.html.j2',context=jsonData)
        else:
            return jsonify({ 'status':'NIC or User Name Not Found.' })
    else:
        return jsonify({ 'status':'Not a Valid Method' })



if __name__ == '__main__':
    application.run(debug=True)