import csv
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

file_twitter_data = "project_twitter_data.csv"
twitter_path = os.path.join("..", data, file_twitter_data)

output_file_name = "resulting_data.csv"
output_path = os.path.join("..", data, output_file_name)

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
    with open(twitter_path, "r", encoding='UTF-8') as file_twitter_in:
        csv_reader = csv.reader(file_twitter_in)
        header = next(csv_reader)
        twitter_data_list = list(csv_reader)
        with open(output_path, "w", encoding='UTF-8') as file_out:

            header_out = "Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n"
            file_out.write(header_out)

            for tweet_row in twitter_data_list:
                tweet_txt = tweet_row[0]
                retweet_count = tweet_row[1]
                replay_count = tweet_row[2]

                positive_score = get_pos(tweet_txt)
                negative_score = get_neg(tweet_txt)
                net_score = positive_score - negative_score

                tweet_new_file_data = [retweet_count, replay_count, str(positive_score), str(negative_score), str(net_score)]
                new_line = ",".join(tweet_new_file_data)

                file_out.write(new_line + "\n")

except FileNotFoundError as e:
    print(f"ERROR: A required file was not found.")
    print(f"Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")