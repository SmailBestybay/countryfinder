from flask import Flask, redirect, render_template, request, session
from helper import search_unogs # more exact names to what function does.
import requests
import json

# to start virtual enviroment set execution policy and run activate.ps1 file 
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Country Finder")

@app.route("/search", methods=["POST"])
def search():
    
    title = request.form.get("search")
    result = search_unogs(title)

    # if no results
    if "results" not in result:
        return render_template("index.html", title="No Results")

    result_only = result["results"]
    
    # concatenate clist with {} then use json.loads() to convert it to dict
    
    for i in range(len(result_only)):  # lines 26 to 32 put into helper file, leave lower func to python.  
        result_only[i]["clist"] = "{" + result_only[i]["clist"] + "}"
        result_only[i]["clist"] = json.loads(result_only[i]["clist"])

        # for key and value in clist, lower and replace whitespace with dash
        for key, value in result_only[i]["clist"].items():
            result_only[i]["clist"][key] = value.replace(" ", "-") 

    return render_template("results.html", result_only=result_only, title="Results")