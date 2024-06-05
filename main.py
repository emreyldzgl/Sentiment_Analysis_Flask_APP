from flask import Flask, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] != 0:
            message = "Negative 👎"
            message_class = "negative"
        else:
            message = "Positive 👍"
            message_class = "positive"
        return render_template('home.html', message=message, message_class=message_class)
    return render_template('home.html', message="", message_class="")
