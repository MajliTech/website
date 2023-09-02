import flask
import requests


def return_template():
    response = requests.get("https://api.github.com/users/MajliTech/repos")
    if response.status_code != 200:
        with open("./templates/projekty/template.html") as f:
            return flask.render_template_string(f.read(), content="Nie udało się połączyć z GitHubem.")
    data = response.json()
    paragraphs = ""
    for repo in data:
        paragraph = ""
        if repo["fork"] or repo["name"] == repo["owner"]["login"] or repo["name"]!="website":
            continue
        if repo["archived"]:
            paragraph = "<i>"
        paragraph = paragraph + "<a href='" + \
            repo["html_url"]+"'><p>"+repo['name']+" | "
        if repo['description']:
            paragraph = paragraph+repo['description']+" | "
        else:
            paragraph = paragraph+"Brak opisu | "
        if repo["language"]:
            paragraph = paragraph+repo['language']+" | "
        else:
            pass
        if repo['stargazers_count']:
            paragraph = paragraph+str(repo['stargazers_count'])+" gwiazdek |"
        else:
            paragraph = paragraph+"Brak gwiazdek"
        if repo["archived"]:
            paragraph = paragraph + "</i>"
        paragraphs = paragraphs + paragraph+"</a>"
    with open("./templates/projekty/template.html") as f:
        return flask.render_template_string(f.read(), content=flask.Markup(paragraphs))
