# Creating REST API for a Word2Vec model with Gensim
By using Gensim, a Word2Vec model trained and tested on Flask REST API.

## Install Requirements
```
$ pip install -U gensim
$ pip install Flask
$ pip install -U nltk
```

Dataset Categories
- Health
- Sport
- Religious
- Economy
- Politics

## Test trained model on REST API
```
$ python3 api.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

```
http://127.0.0.1:5000/?word=futbol
```
