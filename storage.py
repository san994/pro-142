from flask import Flask,jsonify,request
import csv

with open("article.csv",encoding='utf8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_article=data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/")
def main():
    return "article recomendation"

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_article[0],
        "status":"success"
    },201)

@app.route("/liked-article",methods=["POST"])
def liked_movie():
    global all_article
    article = all_article[0]
    all_article = all_article[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)

@app.route("/unliked-article",methods=["POST"])
def unliked_movie():
    global all_article
    article = all_article[0]
    all_article = all_article[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)


if __name__=="__main__":
    app.run()
