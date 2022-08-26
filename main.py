import pandas as pd
from lib.match_finder import MatchFinder

data = pd.read_csv("doc/casual_data_windows.csv", sep=",")
data.drop("Unnamed: 0", axis=1, inplace=True)

mfr = MatchFinder(data["0"])
mfr.fit()

# Randomly selecting and testing a sample of the data.
query_samples = data["1"].sample(n=25)
for query in query_samples:
    print(f'QUERY >> {query}')

    mfr.query(query)
    best_matches = mfr.return_similar()

    for idx in range(3):
        index = best_matches["indexes"][idx]
        score = best_matches["scores"][idx] * 100
        print(f'SIMILAR >> {data["0"][index]} ({score:.2f}%)')
    print("----------------------------------------------------")
