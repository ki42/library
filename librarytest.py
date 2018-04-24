from flask import request, redirect, render_template, session, flash
import cgi
from app import app, db
from models import Library, Categories, User, SearchHistory

@app.route("/")
def things():
    query = 'thisthing'
    kind ='title'
    return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind))

if __name__ == "__main__":
    app.run()





