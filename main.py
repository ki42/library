from flask import request, redirect, render_template, session, flash
import cgi
import webbrowser
from app import app, db
from models import Library, Categories, User, SearchHistory
from hashutils import check_pw_hash

app.secret_key = 'kdjiong395yr1nlkern'
session = []

@app.route("/",  methods =['POST', 'GET'])
def search():	
    library_table = Library.query.all()
    if request.method == 'GET':
        return render_template('index.html', 
            library_table = library_table)
 
 
    if request.method == 'POST':
        cat = request.form['category']     #I have set a default, there will always be a cat
        query_error = ''
        checkbox_error =''
       
        if request.form['query']:               #did my user type in a query?
            query = cgi.escape(request.form['query'])
        else:                                   #query empty:
            flash("Please enter a serch term", category="error")   
            query_error = "error"
               
        if request.form['library']:             #did my user type in a library?
            list_of_checkedboxes = request.form.getlist('library')
        else:                                   #library unchecked:
            flash("Please check at least one library", category="error")
            checkbox_error = "error"

        if not query_error and not checkbox_error :  #this passes if the strings stay empty
            list_of_urls = []   
            for j in list_of_checkedboxes: #loop through library.id checked  
                
                entry = Library.query.filter_by(id = j).first()  #get me the library entry line        
                forkey = entry.owner_id                     #some libraries need their key
                their = Categories.query.filter_by(id = forkey).all()
                for i in their:                             #each library needs it's own query set up right. 
                    if cat == 'keyword':
                        kind = i.keyword
                    if cat == 'title':
                        kind = i.title
                    if cat == 'subject':
                        kind = i.subject
                    if cat == 'author':
                        kind = i.author
                if session:  #not done (check the session for a user name before trying to store data)  
                    library_string = ''.join(j + ',') #create the libary string with each for loop, commit later:
                    #it is not seeing this variable outside of the loop. and I still need to commit it.


# library handler:      #still in the for loop.                     
                if entry.owner_id == 1: #SLPL    
                    list_of_urls.append("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind))
                if entry.owner_id == 2:  #Municipal Public Libraries
                    list_of_urls.append("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0".format(query, kind, entry.consortium_id))
                if entry.owner_id == 3: #SLCL
                    list_of_urls.append("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))

# we exit the for loop:

#the libary_string created in the for loop isn't being returned to be able to handle the session commit.
#figure out how to create it in the loop and only submit it after it finishes, without returning and breaking the current pretty loop. 
#it was nested with it's own loop, but that means it's loop would run for every library submitted... 

#           if library_string:    #There was a user logged in and it got created.
#               #TODO owner needs to come out of the session
#                search = SearchHistory(kind, query, library_string, owner) 
#                db.session.add(search)
#               db.session.commit()  

#            if request.form['view'] == 'tab':
#                for i list_of_urls:
#                    #this is still not the right code for tabs, needs to be JavaScript something....
#                    the_urls = """ <a href="{0}".format(i) target="_blank"></a> """  
#                    return redirect(the_urls)
#                      
#                    render_template('tab.html',
#                        list_of_urls = list_of_urls, 
#                        inline= inline,
#                        library_table = library_table))   #this should be a for loop redirect. 

            if request.form['view'] == 'inline': #route to tab at the moment - fixt it
                    inline = request.form['view']
                    return render_template('index.html', 
                        list_of_urls = list_of_urls, 
                        inline= inline,
                        library_table = library_table)
    
        else:                #it had a user submission error                          
            return render_template("index.html",    
                query=query,
                body=body,
                query_error = query_error,    #I am not sure I have to pass these, they are flash messages
                checkbox_error = body_error
                            ) 
 

                
#untested code, needs database reinitialize:

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
#        verify = request.form['verify']  I am not currently, I may add a drop down window to register in the future
        users = User.query.filter_by(user=user)
        if users.count() == 0:  #I checked, it doesn't exist yet, create it.
            user_object = User(user=user, password=password) #the hash happens in models.py
            db.session.add(user_object)
            db.session.commit()
            session['user'] = user_object.user
            flash('New User created')
            return redirect("/")   #this might need to be a template re-render....
        if users.count() == 1:
            user = users.first() #double check, you have just one entry, right and it is not the user object
            if check_pw_hash(password, user.pw_hash):
                session['user'] = user.user
                flash('welcome back, '+user.email)
                return redirect("/")          #I need to pass something here so the form knows how to deal
        flash('Password incorrect for this username')
        return redirect("/")

#           flash("user + '" is already taken and password reminders are not implemented')
#            return redirect('/register')
#if you have a verify password block in your registration page
#        if password != verify:
#            flash('passwords did not match')
#            return redirect('/register')

#end user/pass dealing with

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        LibraryAdd = LibraryContact.query.join(Library, 
                Library.id==LibraryContact.owner).add_columns(Library.id, 
                Library.library_name,
                LibraryContact.street,   #SyntaxError: keyword can't be an expression
                LibraryContact.city,         #Look up how to do a proper join again.
                LibraryContact.zipcode,
                LibraryContact.email,
                LibraryContact.phone,
                LibraryContact.owner)
                #.paginate(page, 1, False)
        return render_template('contact.html', 
            libraryAdd = LibraryAdd)  #needs both the library and the contact objects


if __name__ == "__main__":
    app.run()


