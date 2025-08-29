import json

# Open the corpus
with open('tv_text.txt', 'r') as file:
    corpus = file.read()
    file.close()

# Split the corpus and init the document
corpus = corpus.split(" ")
word_counts = {}

# Get the word counts
for i in corpus:
    try:
        word_counts[i] = word_counts[i] + 1
    except:
        word_counts[i] = 1

# Write the word counts into a JSON file
with open('word_counts.json', 'w') as word_counts_json:
    word_counts_json.write(json.dumps(word_counts))

