from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Country Finder")

@app.route("/search", methods=["POST"])
def search():
    
    title = request.form.get("search")

    try:
        response = search_unogs(title)
        if not response.ok:
            raise Exception()
        else:
            result = response.json()
    except:
        return render_template("index.html", title="Something Went Wrong, Try again")

    if "results" not in result:
        return render_template("index.html", title="No Results")

    result_only = result["results"]
    
    # convert comma separated list of countries into dictionary
    for i in range(len(result_only)):  
        result_only[i]["clist"] = "{" + result_only[i]["clist"] + "}"
        result_only[i]["clist"] = json.loads(result_only[i]["clist"])

        # for country names consisting from more than one word convert to slug.
        for key, value in result_only[i]["clist"].items():
            if " " in result_only[i]["clist"][key]:
                result_only[i]["clist"][key] = value.replace(" ", "-") 

    return render_template("results.html", result_only=result_only, title="Results")

def search_unogs(title):
    """Send request to UNOGS API based on title"""

    url = "https://unogsng.p.rapidapi.com/search"
    f = open("api_key.txt", "r")
    
    querystring = {
        "start_year":"1972",
        "orderby":"rating",
        "audiosubtitle_andor":"and",
        "limit":"100",
        "subtitle":"english",
        "query":title,
        "audio":"english",
        "country_andorunique":"or",
        "offset":"0",
        "end_year":"2021"
        }

    headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': f.read()
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response
