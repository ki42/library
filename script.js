#this is a JavaScript for redirecting in a new tab.
window.open('http://stackoverflow.com', '_blank');

#this alerts with button clicks
function Hello() {
    alert("Hello, World");
 }

 <script> 
 function toggle(source) {
     checkboxes = document.getElementsByName('library');
     for(var i=0, n=checkboxes.length;i<n;i++) {
       checkboxes[i].checked = source.checked;
     }
   }
 </script> 

 to_do = """<script>window.open('"https://slpl.bibliocommons.com/v2/search?query={0}&searchType={1}".format(query, kind)', '_blank');</script>"""