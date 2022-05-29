from flask import Flask,jsonify,request
from demographicfiltering import output
from contentfiltering import get_recommendations
from storage import liked_articles,not_liked_articles,all_article
import csv

app = Flask(__name__)

@app.route("/")
def main():
    return "article recomendation"

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data":all_article[0],
        "status":"success"
    })

@app.route("/popular-movies")
def popular_movies():
    article_data = []
    for article in output:
        _d = {
            'title':article[0],
            "text":article[2],
            "url":article[3]
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"success"
    },200)

@app.route("/recomended-articles")
def recomended_movies():
    all_recomended=[]
    for likedarticle in liked_articles:
        output = get_recommendations(likedarticle[19])
        for data in output:
            all_recomended.append(data)

    import itertools
    all_recomended.sort()
    all_recomended = list(all_recomended for all_recomended,_ in itertools.groupby(all_recomended))
    article_data = []
    for article in all_recomended:
        _d = {
            'title':article[0],
            "text":article[1],
            "url":article[2]
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"success"
    },200)



if __name__=="__main__":
    app.run()
