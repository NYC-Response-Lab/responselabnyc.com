# responselabnyc.com
Content + script for http://responselabnyc.com/ website.

# To build the site
* make sure `_site` folder exists (create locally if needed; DO NOT put it on github)
* make sure it contains a link to `assets` (create a symolic link if needed (`ln -s ../assets .`); DO NOT put it on gihub)
* from the top folder, run `python build_site.py`

# To add text content to a page
* go to the page and make an HTML edit

# To add data to a collection, e.g. people, projects, etc.
* go to the corresponding page and add to the array that represents the collection

# To add a new page
* copy an existing page and make changes
* add the name of the page (without the html suffix) to the Python script
