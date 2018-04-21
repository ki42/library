from app import db

class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    library_name = db.Column(db.String(120), unique=True)
    consortium_id = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __init__(self, library_name, library_categories, consortium_id, owner):
        self.library_name = library_name
        self.library_categories = library_categories
        self.consortium_id = consortium_id
        self.owner = owner

    def __repr__(self):
        return '<Library %r>' % self.library_name

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(120))
    author = db.Column(db.String(120))
    subject = db.Column(db.String(120))
    keyword = db.Column(db.String(120))
    library_categories = db.relationship('Library', backref='owner')
    

    def __init__(self, title, author, subject, keyword):
        self.title = title
        self.author = author
        self.subject = subject
        self.keyword = keyword
        

    def __repr__(self):
        return '<category %r>' % self.id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    entries = db.relationship('SearchHistory', backref='owner')
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.user


class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20))
    entry = db.Column(db.String(150))
    libraries = db.Column(db.String(150))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, category, entry, libraries, owner):
        self.category = category
        self.entry = entry
        self.libraries = libraries
        self.owner = owner

    def __repr__(self):
        return '<history %r>' % self.entry