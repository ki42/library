from flask import request, redirect, render_template, session, flash
import cgi
from app import app, db
from models import Library, Categories, User, SearchHistory


@app.route("/",  methods =['POST', 'GET'])
def search():	
    library_table = Library.query.all()
    if request.method == 'GET':
        return render_template('index.html', 
            library_table = library_table,)
 
 
    if request.method == 'POST':
        cat = request.form['category']



# these lines are new and are causeing things to break:       
        if request.form['query']:
            query = request.form['query']
#        else:
#            flash("Please enter a serch term", category="error")   
               
        if request.form['library']:
#            list_of_checkedboxes = []
#            for n in range(len(library_table)+1):
#                if request.form.value(n):
#                    list_of_checkedboxes = list_of_checkedboxes.append(n) #this should be giving me library.id of the ones checked
#        else:
#            flash("Please check at least one library", category="error")



            list_of_allkv = request.form.values()
            if list_of_allkv.keys() == 'library':




#this all works...don't touch it.  #but it doesn't count above 10 and # it isn't taking in multiple checkboxes              
        list_of_checkedboxes = request.form['library']
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
                #the redirect happens if more than one is selected, so I need to fix this:    
                if entry.owner_id == 1: #SLPL     
                    return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind))
                if entry.owner_id == 2:  #Municipal Public Libraries
                    return redirect("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0".format(query, kind, entry.consortium_id))
                if entry.owner_id == 3: #SLCL
                    return redirect("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))
                else:
                    return print(forkey, kind, query)

            #I need to get the data out of the post request. 
            #once I have them, I need to see the owner_ids of the checked off libraries
if __name__ == "__main__":
    app.run()


