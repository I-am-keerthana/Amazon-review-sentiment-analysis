import nltk

packages = [
    "vader_lexicon",
    "punkt",
    "stopwords",
    "averaged_perceptron_tagger"
]

for pkg in packages:
    nltk.download(pkg)

print("All NLTK packages downloaded successfully.")
