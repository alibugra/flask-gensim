from gensim.models import Word2Vec
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def word2vec():
    model = Word2Vec.load("model/trained_model.bin")
    w = request.args['word']
    return jsonify(model.most_similar(positive=[w], topn=10))

if __name__ == '__main__':
    app.run(debug=True)
