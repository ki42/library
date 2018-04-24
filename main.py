from flask import request, redirect, render_template, session, flash
import cgi
from app import app, db
from models import Library, Categories, User, SearchHistory

app.secret_key = 'kdjiong395yr1nlkern'

@app.route("/",  methods =['POST', 'GET'])
def search():	
    library_table = Library.query.all()
    if request.method == 'GET':
        return render_template('index.html', 
            library_table = library_table,)
 
 
    if request.method == 'POST':
        cat = request.form['category']


# these lines are new and are causeing things to break:       
        query_error = ''
        checkbox_error =''
        if request.form['query']:
            query = request.form['query']
        else:
            flash("Please enter a serch term", category="error")   
            query_error = "error"
               
        if request.form['library']:
#            list_of_checkedboxes = []
#            for n in range(len(library_table)+1):
#                if request.form.value(n):
#                    list_of_checkedboxes = list_of_checkedboxes.append(n) #this should be giving me library.id of the ones checked
            list_of_checkedboxes = request.form.getlist('library')
        else:
            flash("Please check at least one library", category="error")
            checkbox_error = "error"








#            list_of_allkv = request.form.values()
#            if list_of_allkv.keys() == 'library':


#this all works...don't touch it.  #but it doesn't count above 10 and # it isn't taking in multiple checkboxes              
           
        for j in list_of_checkedboxes: #loop through library.id checked  
            entry = Library.query.filter_by(id = j).first()  #get me the library entry line        
            forkey = entry.owner_id
            their = Categories.query.filter_by(id = forkey).all()
            for i in their:
                if cat == 'keyword':
                    kind = i.keyword
                if cat == 'title':
                    kind = i.title
                if cat == 'subject':
                    kind = i.subject
                if cat == 'author':
                    kind = i.author
                    
                if not query_error and not checkbox_error :  #this passes if the strings stay empty
                    if user in session:  #not done (check the session for a user name before trying to store data)
                        for lib in list_of_checkedboxes:   
                            library_string = ''.join(lib + ',') 
                        search = SearchHistory(kind, query, library_string, owner) #TODO owner needs to come out of the sesion
                        db.session.add(search)
                        db.session.commit()  
                #the redirect happens if more than one is selected, so I need to fix this:    
                if entry.owner_id == 1: #SLPL     
                    return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind))
                if entry.owner_id == 2:  #Municipal Public Libraries
                    return redirect("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0".format(query, kind, entry.consortium_id))
                if entry.owner_id == 3: #SLCL
                    return redirect("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))
                else:                                
                    return render_template("index.html",    #it had an error
                        query=query,
                        body=body,
                        query_error = query_error,    #I am not sure I have to pass these, they are flash messages
                        checkbox_error = body_error
                        ) 
 

#I haven't worked on the login side of things yet
#I want the signin and register with the same two boxes.
#user password
#if user and check_pw_hash(password, user.pw_hash):
#if first time, flash new user account
#if back flash welcome back {0}!

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        if not is_email(email):
            flash('zoiks! "' + email + '" does not seem like an email address')
            return redirect('/register')
        email_db_count = User.query.filter_by(email=email).count()
        if email_db_count > 0:
            flash('yikes! "' + email + '" is already taken and password reminders are not implemented')
            return redirect('/register')
        if password != verify:
            flash('passwords did not match')
            return redirect('/register')
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['user'] = user.email
        return redirect("/")
    else:
        return render_template('register.html')
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email)
        if users.count() == 1:
            user = users.first()
            if password == user.password:
                session['user'] = user.email
                flash('welcome back, '+user.email)
                return redirect("/")
        flash('bad username or password')
        return redirect("/login")

#end user/pass dealing with

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        LibraryAdd = LAddresses.query.join(Library, 
                Library.id==LAddresses.owner).add_columns(Library.id, 
                Library.library_name,
                LAddresses.street = street,   #SyntaxError: keyword can't be an expression
                LAddresses.city = city,
                LAddresses.zipcode = zipcode,
                LAddresses.email = email,
                LAddresses.phone = phone,
                LAddresses.owner = owner)
                #.paginate(page, 1, False)
        return render_template('contact.html', 
            libraryAdd = LibraryAdd)  #needs both the library and the contact objects




#I don't think contact will handle post requests. 
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email)
        if users.count() == 1:
            user = users.first()
            if password == user.password:
                session['user'] = user.email
                flash('welcome back, '+user.email)
                return redirect("/")
        flash('bad username or password')
        return redirect("/login")




if __name__ == "__main__":
    app.run()


