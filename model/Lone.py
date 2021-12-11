from application import db

class Lone(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nic = db.Column(db.String(15), nullable=False)
    lone_amount = db.Column(db.Float,nullable=False,default=0)
    guarantee = db.Column(db.String(15), nullable=False)
    is_settled = db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,nic,lone_amount,guarantee,is_settled):
        self.nic = nic
        self.lone_amount = lone_amount
        self.guarantee = guarantee
        self.is_settled = is_settled

    def __repr__(self) -> str:
        return f"[id => {self.id}, main_balance => {self.main_balance}]"
