from flask import Flask, redirect, url_for, render_template
import twint
import nest_asyncio
import pandas as pd
import os

nest_asyncio.apply()
app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def home():
    tweets_df = pd.read_csv("tweets.csv")
    return render_template('index.html',  tables=[tweets_df.to_html()])

@app.route('/retweets')
def sortby_retweet():
    tweets_df = pd.read_csv("tweets.csv")
    tweets_df = tweets_df.sort_values(by=['retweets_count'], ascending=False)
    return render_template('index.html',  tables=[tweets_df.to_html()])

@app.route('/likes')
def sortby_like():
    tweets_df = pd.read_csv("tweets.csv")
    tweets_df = tweets_df.sort_values(by=['likes_count'], ascending=False)
    return render_template('index.html',  tables=[tweets_df.to_html()])

@app.route('/discussions')
def sortby_discussion():
    tweets_df = pd.read_csv("tweets.csv")
    tweets_df = tweets_df.sort_values(by=['replies_count'], ascending=False)
    return render_template('index.html',  tables=[tweets_df.to_html()])

def take_data():
    c = twint.Config()
    c.Search = "request for startup"
    c.Store_csv = True
    c.Output = "tweets.csv"
    twint.run.Search(c)

if __name__ == "__main__":
    take_data()
    app.run(debug=True)