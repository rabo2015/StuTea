from blog import db

class User(db.Model):
    __tablename__='b_user'
    id=db.Colum(db.Integer,primary_key=True)
    username=db.Colum(db.string(10),unique=True)
    password=db.Colum(db.String(16))

    def __int__(self,username,password):
        self.username=username
        self.password=password

    def __repr__(self):
        return '<User %r>'%self.username #返回用户名
