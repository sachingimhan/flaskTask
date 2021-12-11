from os import name
from flask import Flask,render_template,request,session,url_for
import flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
from werkzeug.utils import redirect

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


@application.route("/invest",methods=['POST'])
def invest():
    if request.method == 'POST':
        data = request.get_json()
        print(data['nic'])
        if(data['nic'] != None or data['amount'] != None):
            old_amount = db.session.query(User.User.balance).filter_by(nic=data['nic']).first()
            amount = float(old_amount[0]) + float(data['amount'])
            db.session.query(User.User).filter_by(nic=data['nic']).update(dict(balance=amount))
            db.session.commit()
            return json.dumps({ 'status':'200','message':'success' }),200
        else:
            return json.dumps({ 'status':'400','message':'fail' }),400


@application.route("/start",methods=['POST'])
def get_start():
    if request.method == 'POST':
        nic = request.form.get('nic')
        username = request.form.get('username')
        if nic != None or username != None:
            exists = db.session.query(User.User.nic).filter_by(nic=nic).first() is not None
            print(exists)
            if(exists != False):
                user = db.session.query(User.User).filter_by(nic=nic).first()
                print(user,"asdasd")
                jsonData = { 'nic':user.nic,'user_name':user.user_name,'balance':user.balance }
                return render_template('home.html.j2',data=json.dumps(jsonData))
                # return redirect(url_for('home',message=jsonify(jsonData)))
            else:
               newUser = User.User(nic=nic,user_name=username,balance=0,is_guarantee=False)
               db.session.add(newUser)
               db.session.commit()
               user = db.session.query(User.User).filter_by(nic=nic).first()
               print(user)
               jsonData = { 'nic':user.nic,'user_name':user.user_name,'balance':user.balance }
               return render_template('home.html.j2',data=json.dumps(jsonData))
                #   return redirect(url_for('home',values=jsonify(jsonData)))
        else:
            return jsonify({ 'status':'NIC or User Name Not Found.' })
    else:
        return jsonify({ 'status':'Not a Valid Method' })

@application.route('/home',methods=['GET'])
def home():
    return render_template('home.html.j2')


if __name__ == '__main__':
    application.run(debug=True)