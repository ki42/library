from flask import Flask, request
	
	app = Flask(__name__)
	app.config['DEBUG'] = True
	
	
@app.route("/form-inputs", methods=['POST'])
def print_form_values():
	resp = ""
	for field in request.form.keys():
	    resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])
	    return resp
	    
	
	app.run()






#SLPL
#their names /my names
smart = keyword
title = title
author = author
subject = subject
return redirect("https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, SearchType)

#SLCL
#their names /my names
#they are running an app that does not use standard query params. 
return redirect("http://encore.slcl.org/iii/encore/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&target={0}".format(query)


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

return redirect("http://pac.mlc.lib.mo.us/polaris/search/searchresults.aspx?ctx={2}.1033.0.0.1&type=Keyword&term={0}&by={1}&sort=RELEVANCE&limit=TOM=*&query=&page=0&searchid=1".format(query, SearchType, which_library)




<div> 
    <object type="text/html" data="http://validator.w3.org/" width="800px" height="600px" style="overflow:auto;border:5px ridge blue">
    </object>
 </div>

@app.route("/"  methods =["POST", "GET"])

