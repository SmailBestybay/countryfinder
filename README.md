# Country Finder
#### Video Demo:  https://youtu.be/CiHE0b10Jog
#### Description:
Country Finder is a web app that searches Netflix catalog accross the globe.
The search result returns a list of netflix titles with flags of countries where that title is available.

It uses [unogsNG database](https://rapidapi.com/unogs/api/unogsng) through RapidApi.

Flask is the backend framework. 

The backend tasks are:
- make API calls to unogsNG database.
- parse over JSON response and convert it into Python dict
- manipulate the converted JSON to extrapulate country names list
- render templates with JINJA

Front end technologies are HTML, CSS, Bootstrap, [MDB flags](https://mdbootstrap.com/docs/standard/content-styles/flags/).

For Card styling I referenced [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Card).

I used Visual Studio Code IDE in a virtual enviroment. 

In the future, there are multitude of features I would like to add, and improve general user experience with better styling and layout.
An example of that would be to make each card a link to a pop up page that would show more details about a particular search result. 

Description of each file in the project:
- **app.py** is the main back end file that contains the routes, manipulates converted JSON, and passes arguments to JINJA.
- **helper.py** contains the function to make the API call to unogsNG database.
- **templates** folder contains html templates.
- **static** folder contains css folder which contains styles.css file.
- **styles.css** is the stylesheet for the web app, mainly for card layout of the results page.
- **requierments.txt** is flask requierments file.

