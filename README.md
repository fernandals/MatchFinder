# MatchFinder

The program combines the functions of a TF-IDF vectorizer and Cosine Similarity metric.
From a given query, extracted from a column of the sample dataset, the objective is to return the 3 most similar texts in the corpus based on the defined metric.
The program output consists of
```
QUERY >> the query
SIMILAR >> 1st most similar entry (score percentage)
SIMILAR >> 2nd most similar entry (score percentage)
SIMILAR >> 3rd most similar entry (score percentage)
----------------------------------------------------
```

## Dataset

The data was collected from a forum on Reddit (r/CasualConversation) between 2016-12-29 and 2019-12-31.
The dataset consists of 4 columns, where each row is an index and a length-3 conversation.
There is repetition of the question/answer between the columns as they may belong to the same topic in the forum.
Link to dataset: https://www.kaggle.com/datasets/jerryqu/reddit-conversations

## TF-IDF Vectorizer

TF-IDF is the abbreviation for Term Frequency - Inverse Document Frequency, as the name implies, this technique vectorizes documents by measuring the frequency of words and assigning them a certain value of importance.
This importance is inverse to the frequency: words that appear little in the corpus are classified as rare and their importance is high in the vectorization process.

## Cosine Similarity

The cosine similarity metric calculates the distance between 2 vectors by analyzing the angle formed by these vectors.
The relationship between the cosine and the angle is inversely proportional, so the greater the angle (the distance in this case) the smaller the cosine (the similarity).
In a sense, if two text-vectors have a great angle between then, they represent different texts (they may even be pointing in opposite directions).
So we can safely assume that the cosine will tell us when the texts are in fact different (assuming our constructions of vectors really do represent well our texts).

## How to run

Just run the `main.py` file, as in the example below:
```
python main.py
```

