from flask import request, redirect, render_template, session, flash
import cgi
import webbrowser
from app import app, db
from models import Library, Categories, User, SearchHistory, LibraryContact
from hashutils import check_pw_hash

app.secret_key = 'kdjiong395yr1nlkern'

# I need library_table globally.
library_table = Library.query.all()

#some helper functions pulled out of my existing code because I need rereuse the variables in other functions. 

def searchedlibraries():
    user = session['user'] #who's logged in?
    users = User.query.filter_by(user=user).first() #get user line from table.
    owner_id = users.id  #get the user id
    all_searches = SearchHistory.query.filter_by(owner_id = owner_id).all() #get all of the search histories for that owner
    list_lib_names = []
    searched = []
    for n in all_searches:       #n should be an object for each search
        libraries_searched = n.libraries        # libraries searched is holding the string of lib numbers
        each_library = libraries_searched.split('.')  #split them into a list
        searched.append(each_library)   #now store that nested list in another list
    for j in searched: #for each row of lib
        temp_inner_list = []
        for lib in j: #for each lib in the search
            library_row = Library.query.filter_by(id = lib).first()  #get it's libary row from the table
            library_name = library_row.library_name
            temp_inner_list.append(library_row.library_name) #get it's library name and append it to a list. 
               #build the list with each entry with separate nested list
        list_lib_names.append(temp_inner_list)
    return [searched, list_lib_names] 


@app.route("/delete", methods=['POST'])
def delete():
    searchid = request.form['searchid']
    delete_id = SearchHistory.query.get(searchid)
    if not delete_id:
        return redirect("/searchhistory")
    db.session.delete(delete_id)
    db.session.commit()
    flash("entry deleted")
    return redirect('/searchhistory')

# def searchedcategories():
#    users = User.query.filter_by(user=user).first() #get user line from table.
#    owner_id = users.id
#    all_searches = SearchHistory.query.filter_by(owner_id = owner_id).all() 
#    list_cat_names = []
#    for n in all_searches:       #m should be an object for each search
#        category_searched = n.category
#        category_label = "key_this_test"
#        list_cat_names = list_cat_names.append(category_label)
#    return list_cat_names


@app.route("/",  methods =['POST', 'GET'])
def search():	
    library_table = Library.query.all()
    if request.method == 'GET':
        if "user" in session:
            user = session["user"]
            return render_template('index.html', 
                library_table = library_table,
                user = user)
        else:
            return render_template('index.html', 
                library_table = library_table
                )
        
    if request.method == 'POST':
        cat = request.form['category']     #I have set a default, there will always be a cat
        query_error = ''
        checkbox_error =''
        list_of_checkedboxes = []
       
        if request.form['query']:               #did my user type in a query?
            query = cgi.escape(request.form['query'])
        else:                                   #query empty:
            query = ''
            flash("Please enter a serch term", category ="error")   
            query_error = "error"

        if request.form.getlist('lib'):   
            list_of_checkedboxes = request.form.getlist('lib')

        else:
 #       if request.form['library']:             #did my user check a library?
            if list_of_checkedboxes == []:
                if request.form.getlist('library') != []:
                    list_of_checkedboxes = request.form.getlist('library')
                else: 
                    flash("Please check at least one library", category="error")
                    checkbox_error = "error"
                    return redirect("/")
            
        if not query_error and not checkbox_error:  #this passes if the strings stay empty
            list_of_urls = []   
            for j in list_of_checkedboxes: #loop through library.id checked  
                entry = Library.query.filter_by(id = j).first()  #get me the library entry line 
                print(entry)       
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
               
# library handler:      #still in the for loop.                     
                if entry.owner_id == 1: #SLPL    
                    list_of_urls.append("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind))
                if entry.owner_id == 2: #SLCL
                    list_of_urls.append("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))
                if entry.owner_id == 3:  #Municipal Public Libraries
                    list_of_urls.append("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0".format(query, kind, entry.consortium_id))
                if entry.owner_id == 4: #Washington University
                    list_of_urls.append("http://catalog.wustl.edu/search/a?searchtype={1}&searcharg={0}&SORT=D".format(query, kind))
                if entry.owner_id == 5: #SLU
                    list_of_urls.append("http://libcat.slu.edu/search/?searchtype={1}&SORT=D&searcharg={0}&searchscope=5".format(query, kind))
                if entry.owner_id == 6: #Bridges
                    list_of_urls.append("http://bridges.searchmobius.org/search/?searchtype={1}&SORT=D&searcharg={0}&searchscope={2}".format(query, kind, entry.consortium_id))



# we exit the for loop:
            if session and not request.form.getlist('lib'):     #store my search history
                user = session['user']
                users = User.query.filter_by(user=user).first()
                library_string = ''
                for m in list_of_checkedboxes:                
                    library_string = library_string + m + "."
                owner = users.id
                library_string = library_string.rstrip('.')
                search = SearchHistory(cat, query, library_string, users) 
                db.session.add(search)
                db.session.commit()  
                my_searches = SearchHistory.query.filter_by(owner_id = owner).all()
                
                if my_searches:            
                    lib_names =[]
                    for n in my_searches:
                        list_libraries = [x.strip() for x in n.libraries.split('.')]
                        for j in list_libraries:
                            each_lib_names =[]
                            for library in library_table:
                                if j == library.id:
                                    lib_names = lib_names.append(library.name) #this has only worked for one entry.
                            each_lib_names = each_lib_names.append(lib_names)
                            

            if request.form.getlist('lib'): #if the search is being returned, it doesn't have inline/view
                return render_template('index.html', 
                    list_of_urls = list_of_urls, 
                    library_table = library_table,
                    category = cat,
                    query = query)

            if request.form['view'] == 'inline': 
                inline = request.form['view']
                return render_template('index.html', 
                    list_of_urls = list_of_urls, 
                    inline= inline,
                    library_table = library_table,
                    category = cat,
                    query = query, 
                    my_searches = my_searches,
                    each_lib_names = each_lib_names
                        )

#            if request.form['view'] == 'tab':
#                render_template('tab.html',
#                    list_of_urls = list_of_urls)



        else:                #it had a user submission error                          
            return render_template("index.html",    
                query=query,
                library_table = library_table,
                query_error = query_error,    
                checkbox_error = checkbox_error,
                list_of_checkedboxes = list_of_checkedboxes
                ) 
#the libary_string created in the for loop isn't being returned to be able to handle the session commit.
#figure out how to create it in the loop and only submit it after it finishes, without returning and breaking the current pretty loop. 
#it was nested with it's own loop, but that means it's loop would run for every library submitted... 


#TODO add tab and pills menu
#TODO add nav bar
#TODO make it pretty
#TODO handle delete function




@app.route("/searchhistory", methods=['GET'])  #Display for user
def show_search():
    library_num_and_name = searchedlibraries()
    #list_cat_names = searchedcategories()
    user = session['user']
    users = User.query.filter_by(user=user).first()

    all_searches = SearchHistory.query.filter_by(owner_id = users.id).all()
    name_list = library_num_and_name[1] 
    num_list = library_num_and_name[0]   #get me just the two nested lists of lib numbers. 
    return render_template ('searchhistory.html', #   TODO what does searchhistory need to function?
        all_searches = all_searches,
        name_list = name_list,
        num_list = num_list,
        library_table = library_table)         


#@app.route("/previous") #When they've clicked on a link to search the history
#def previous():
   #turn the previous 


#    library_num_and_name = searchhistory()
#    for l in library_num_and_name[1]:
      

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
            session['user'] = user
            flash('New User created')
            return redirect("/", code="303")  #this might need to be a template re-render....
        if users.count() == 1:
            user = users.first() #double check, you have just one entry, right and it is not the user object
            if check_pw_hash(password, user.pw_hash):
                session['user'] = user.user
                flash('Welcome back, '+ user.user)
                return redirect("/", code="303")          #I need to pass something here so the form knows how to deal
        flash('Password incorrect for this username', 'error')
        return redirect("/", code="303")

@app.route('/logout', methods=['POST'])
def logout():
    del session['user'] #delete username from session
    flash("You have been logged out")
    return redirect("/", code="303")  

@app.route("/contact", methods=['GET', 'POST']) #not currently using this handler and it's associated table
def contact():
    if request.method == 'GET':
        locate = "True"
#        LibraryAdd = LibraryContact.query.join(Library, 
#                Library.id== LibraryContact.owner).add_columns(Library.id, 
#                Library.library_name,
#                LibraryContact.street,   
#                LibraryContact.city,         
#                LibraryContact.zipcode,
#                LibraryContact.email,
#                LibraryContact.phone,
#                LibraryContact.owner)
                #.paginate(page, 1, False)
        return render_template('contact.html',
           locate = locate)
#            libraryAdd = LibraryAdd)  #needs both the library and the contact objects

@app.route("/images")
def images():
    return ("""<img src="./images/liblogo.jpg" alt="Lib Logo" style="width:100px;height:100px;">""")

if __name__ == "__main__":
    app.run()


