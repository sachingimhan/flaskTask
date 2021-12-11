from application import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    main_balance = db.Column(db.Float,nullable=False,default=0)

    def __init__(self,main_balance):
        self.main_balance = main_balance

    def __repr__(self) -> str:
        return f"[id => {self.id}, main_balance => {self.main_balance}]"
