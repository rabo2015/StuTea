from blog import db

class Category(db.model):
    __tabname__='b_category'
    id=db.Colum(db.Integer,primary_key=True)
    title=db.Colum(db.String(10),Unique=True)
    content=db.Colum(db.String(200))

    def __init__(self,title,content):
        self.title=title
        self.content=content

    def __repr__(self):
        return '<Category %r>'%self.title

