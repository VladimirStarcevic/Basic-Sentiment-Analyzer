import os
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word: str) -> str:
    clean_word = word

    for punc in punctuation_chars:
        clean_word = clean_word.replace(punc, "")
    return clean_word


def get_pos(sentence_text: str) -> int:

    count_positive =  0
    words_in_sentence = sentence_text.lower().split()
    for word in words_in_sentence:
        clean_word = strip_punctuation(word)
        if clean_word in positive_words:
            count_positive += 1
    return count_positive

def get_neg(sentence_txt: str) -> int:
    count_negative = 0
    words_in_txt = sentence_txt.lower().split()

    for word in words_in_txt:
        clean_word = strip_punctuation(word)
        if clean_word in negative_words:
            count_negative += 1
    return count_negative




data = "data"
file_name = "positive_words.txt"
file_path = os.path.join("..",data, file_name)
file_name_negative = "negative_words.txt"
file_path_negative = os.path.join("..", data, file_name_negative)

positive_words = []
negative_words = []

try:

    with open(file_path, "r", encoding='UTF-8') as file_in:
        for line in file_in:
            if line.strip() and not line.startswith(';'):
                positive_words.append(line.strip())
    with open(file_path_negative, "r", encoding='UTF-8') as fil_neg_in:
        for line in fil_neg_in:
            if line.strip() and not line.startswith(";"):
                negative_words.append(line.strip())


except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")