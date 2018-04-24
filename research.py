#SLPL
#their names /my names

title = title
author = author
subject = subject
smart = keyword
return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, SearchType))

#SLCL
#their names /my names
#they are running an app that does not use standard query params. 
#I can only keyword
return redirect("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query))


#Municipal Public Libraries

which_library[
    'Municipal Library Consortium'= 1,
    'Brentwood' = 3,
    'ebranch' = 20,
    'Ferguson'= 5,
    'Kirkwood' = 7,
    'Maplewood' = 9,
    'Richmond Heights' = 11,
    'Rock Hill' = 13,
    'Ucity' = 15,
    'Valley Park' = 17,
    'Webster Groves' = 19
]

#their names /my names
TI = title
AU = author
SU = subject
KW = keyword

return redirect("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0&searchid=1".format(query, SearchType, which_library))




#------------------not in database yet:
#Washington University
#their names /my names
t = title
a = author
d = subject
w = keyword

return redirect("http://catalog.wustl.edu/search/a?searchtype={1}&searcharg={0}&SORT=D".format(query, SearchType))

#Saint Louis University
t = title
a = author
d = subject
X = keyword

return redirect("http://libcat.slu.edu/search/?searchtype={1}&SORT=D&searcharg={0}&searchscope=5".format(query, SearchType))


#Bridges
All Bridges Libraries = 10
Concordia Seminary 
Covenant Seminary 
Fontbonne University 
Harris-Stowe State University
Kenrick-Glennon Seminary 
Lindenwood University 
Logan University
Maryville University 
Missouri Baptist University 
Webster University 
Eden Seminary


t = title
a = author
d = subject
X = keyword

"http://bridges.searchmobius.org/search/?searchtype={1}&SORT=D&searcharg={0}&searchscope={2}".format(query, SearchType, which_library))



                    
if not checked_boxes:
            flash("You need to select a library")
            return redirect('/')

#        else:
#            flash("Please enter a serch term", category="error")   
               
        if request.form['library']:
            list_of_checkedboxes = []
            for n in len(library_table)+1:
                if request.form.get[n]:
                    list_of_checkedboxes = list_of_checkedboxes.append(n) #this should be giving me library.id of the ones checked
        else:
            flash("Please check at least one library", category="error")


#for contact table


