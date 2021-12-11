from application import db

class User(db.Model):
    nic = db.Column(db.String(15), primary_key=True)
    user_name = db.Column(db.String(255),nullable=False)
    balance = db.Column(db.Float,nullable=False,default=0)
    is_guarantee = db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,nic,user_name,balance,is_guarantee):
        self.nic = nic
        self.user_name = user_name
        self.balance = balance
        self.is_guarantee = is_guarantee

    def __repr__(self) -> str:
        return f"[nic => {self.nic}, user_name => {self.user_name}, balance => {self.balance}, is_guarantee => {self.is_guarantee}]"

