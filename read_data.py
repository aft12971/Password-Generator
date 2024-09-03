"""
util function to read txt data for our model
"""
import string
import collections
from unicodedata import normalize
from random import shuffle

    
def read_data(filepath):
    # This function takes a filepath, reads lines of sentences, 
    # and returns a list of lowercase sentences without punctuations.
    data = []
    string_punctuation = string.punctuation + '¿' 
    with  open(filepath, "r", encoding = "utf-8") as fp:
        for line  in fp:
            line = normalize('NFD', line).encode('ascii', 'ignore')
            line = line.decode('UTF-8')
            line = line.rstrip()
            line = line.lower().translate(str.maketrans('', '', string_punctuation))
            data.append(line)
    return data
def read_tsv_data(filepath):
     # This function takes a filepath, reads lines of sentences, 
    # and returns two list of lowercase sentences without punctuations.
    X, y = [], []
    string_punctuation = string.punctuation + '¿' 
    with  open(filepath, "r", encoding = "utf-8") as fp:
        for line  in fp:
            line = normalize('NFD', line).encode('ascii', 'ignore')
            line = line.decode('UTF-8')
            input_text, target_text, _ = line.split("\t")
            input_text = input_text.lower().translate(str.maketrans('', '', string_punctuation))
            target_text = target_text.lower().translate(str.maketrans('', '', string_punctuation))
            X.append(input_text)
            y.append(target_text)
    return X, y
def to_vocab(lines):
    # This function takes creates a counter for the number of unique tokens
    # in every the dataset(lines)
    vocab = collections.Counter()
    for line in lines:
        tokens = line.split()
        vocab.update(tokens)
    return vocab

def trim_vocab(x_lines, y_lines, vocab, min_occurance=100):
    # This function removes sentences that contain tokens that occur
    # less freqeuntly or below the specified threshold.
    for idx, line in enumerate(x_lines): 
        seen = False
        tokens = line.split()
        for token in tokens:
            if vocab[token] < min_occurance:
                    seen = True

        if seen:
            x_lines.pop(idx)
            y_lines.pop(idx)
            seen = False
    return x_lines, y_lines
def shuffle_data(X, y):
    # This function shuffles the input dataset, making sure the order
    # in the train and test set is maintained.
    shuffled_X, shuffled_y = [], []
    indices = list(range(len(X)))
    shuffle(indices)
    for idx in indices: 
        shuffled_X.append(X[idx])
        shuffled_y.append(y[idx])
    return shuffled_X, shuffled_y
        
    
if __name__ == "__main__":
    data = read_data("../data/small_vocab_en")
    print(data[:5])