from flask import Flask,jsonify,request
from demographicfiltering import output
from contentfiltering import get_recommendations
import csv

all_article = []
with open("article.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article = data[1:]

liked_movies = []
not_liked_movies = []

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

@app.route("/popular-articles")
def popular_movies():
    article_data = []
    for article in output:
        _d = {
            "data":article_data,
            "status":"success"
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"success"
    },200)

@app.route("/recomended-articles")
def recomended_movies():
    all_recomended=[]
    for likedmovies in liked_movies:
        output = get_recommendations(likedmovies[19])
        for data in output:
            all_recomended.append(data)

    import itertools
    all_recomended.sort()
    all_recomended = list(all_recomended for all_recomended,_ in itertools.groupby(all_recomended))
    article_data = []
    for article in all_recomended:
        _d = {
            'title':article[11],
            "text":article[12]
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"success"
    },200)



if __name__=="__main__":
    app.run()
