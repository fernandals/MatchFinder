from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MatchFinder:
    """
    This class vectorizes a given corpus using TF-IDF and
    uses Cosine Similarity to find 3 similar docs for a given query.
    """

    def __init__(self, corpus):
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        self.vec_corpus = []
        self.vec_query = []

    def fit(self):
        """ Learns vocabulary and vectorizes corpus. """
        self.vec_corpus = self.vectorizer.fit_transform(self.corpus)

    def query(self, doc):
        """ Vectorizes the input query. """
        self.vec_query = self.vectorizer.transform([doc])

    def return_similar(self):
        """
        Calculates the similarity score between the input and each entry on the corpus
        using cosine similarity as measure.
        Returning the index and score of the 3 most similar entries.
        """
        similarities = cosine_similarity(self.vec_query, self.vec_corpus)
        flattened = similarities.flatten()
        index = flattened.argsort()[:-4:-1]
        best_matches = {
            "indexes" : index,
            "scores"  : [flattened[idx] for idx in index]
        }
        return best_matches
