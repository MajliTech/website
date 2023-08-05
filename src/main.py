import flask
import xml.etree.ElementTree as ET
import random
import importlib
from bs4 import BeautifulSoup
import traceback
app = flask.Flask(__name__,static_url_path="/")
app.static_folder="static/"

@app.route("/")
def indexredir():
    return flask.redirect("/index.html")

@app.route("/basic/")
def basicredir():
    return flask.redirect("/basic/omnie")
@app.route("/basic/<site_url>")
def basic(site_url):
    try:
        with open("static/content/"+site_url+".html") as site:
            content = site.read()
            if content.find("<!-- allowsend -->")==-1:
                return flask.Response(status=403)
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.title
            if title_tag:
                     title_tag.text.strip()
            if content.find("<!-- template -->")!=-1:
                templaterenderer = importlib.import_module("templates."+str(site_url)+".render")
                return flask.render_template("basic.html",content=flask.Markup(templaterenderer.return_template()),title=title_tag.text.strip())
            return flask.render_template("basic.html",title=title_tag.text.strip(),content=flask.Markup(content))
    except Exception as e: 
        print(traceback.format_exc())
        return flask.Response(status=404)
if __name__=="__main__":
    port = random.randint(1025,65535)
    print("""!!! WARNING !!! WARNING !!!
This server is for debugging purposes only.""")
    app.run(debug=True,port=port,host="127.0.0.1")
