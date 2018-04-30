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
All Bridges Libraries - 10
Concordia Seminary - 11
Covenant Seminary - 1
Fontbonne University - 2
Harris-Stowe State University - 3
Kenrick-Glennon Seminary - 4 
Lindenwood University - 5
Logan University - 6
Maryville University - 7
Missouri Baptist University - 8
Webster University & Eden Seminary - 9


t = title
a = author
d = subject
X = keyword

"http://bridges.searchmobius.org/search/?searchtype={1}&SORT=D&searcharg={0}&searchscope={2}".format(query, kind, which_library))



                    
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



 {% if my_searches %}
                    <table><tr>
                        {% for i in my_searches %}
                        <td>
                          <a href="">{{loop.index}}) {{i.category}}{{i.entry}}</a>
                        </td>
                    {% if loop.index is divisibleby 5 %}
                </tr><tr>
                {% endif %}<form method='POST' action='/delete'><input type="hidden" name="searchid" value="{{ i.id }}"/><input type="submit" value="Delete" /></form>
                        {% endfor %}
                    </div></tr>  </td> 
                        {% endif %}
                </table>

{{all_searches[i].id}}

<form method='POST' action='/'>
<table>
    <tr>
        <td>
            <label>Search by:
                    <select name="category">
                        <option value="keyword" default>Keyword</option>
                        <option value="title">Title</option>
                        <option value="subject">Subject</option>
                        <option value="author">Author</option>
                    </select>
            </label>
        </td>
         <td>      
            <label>Search for:
                {% if query %}
                    <input name="query" type="text" value="{{query}}"/>
                {% else %}
                    <input name="query" type="text" placeholder="Search here" />
                {% endif %}
            </label> 
         </td>
    </tr>
    <tr>
        <td> * Note: Not all libraries except all search types</td>
    </tr>
        <tr><td></td></tr>
</table>

<nav>
<ul class="nav nav-tabs">
        <li role="presentation" class="active"><a href="/">Home</a></li>
        {% if user %}
        <li role="presentation"><a href="/searchhistory">Search History</a></li>
        {% endif %}
      </ul>
</nav>

<table>
<!--send library name object   -->
        <tr>
            {% for library in library_table %} 
            <td>
            {{loop.index}})
        <label>
            <input type="checkbox" name="library" value="{{library.id}}" />{{library.library_name}}
        </label>
            </td>
            {% if loop.index is divisibleby 4 %}
            </tr><tr>
            {% endif %}
        {% endfor %}
        <input type="checkbox" onClick="toggle(this)" /> Select All<br/>
        </tr>
        <tr>
            <td>
                <input type="submit" />
            </td>
        </tr>
        <tr>
            <td>
                For development purposes only:<br>
                        <input type="radio" name="view" value="tab"> Tab format<br>
                        <input type="radio" name="view" value="inline" checked> Inline<br>
            </td>
            </tr>

            {% for j in range(num_list[i]|length) %}
