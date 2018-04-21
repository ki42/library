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
        category = request.form['category']
        query = request.form['query']
        
        
        for key in request.form.keys(): #loop through the checkboxes
            
            owner_id = Library.query.filter_by(owner_id = key).first
            
            if owner_id == 1: #SLPL   I don't expect this to work yet 
                their_category_names = Categories.query.get(library_table.owner_id).all
                return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, their_category_names.category))
            if owner_id == Null: #SLCL
                return redirect("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))
            if owner_id == 2:  #Municipal Public Libraries
                their_category_names = Categories.query.get(library_table.owner_id).all
                return redirect("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0&searchid=1".format(query, their_category_names.category, library.consortium_id))


            #I need to get the data out of the post request. 
            #once I have them, I need to see the owner_ids of the checked off libraries
if __name__ == "__main__":
    app.run()


