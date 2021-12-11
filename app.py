from flask import Flask, render_template, request
import nltk
from newspaper import Article

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        link = request.form['link']
        nltk.download('punkt')
        try:

            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            tit = article.title
            res = article.summary
            return render_template('result.html',title=tit,summary=res)
        
        except:
           return render_template('result.html',title="Invalid URL", summary="Try again with valid one")
              
    else:
        return render_template(template_name_or_list)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
