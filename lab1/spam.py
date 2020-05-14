# %%
# define global corpuses for spam filtering
good_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
spam_corpus = [["i", "am", "spam", "spam", "i", "am"], ["i", "do", "not", "like", "that", "spamiam"]]

# this creates dictionary of word and its frequency in a corpus
def create_word_occurrence_dict(corpus):
    new_dict = {}
    for message in corpus:
        for word in message:
            if word in new_dict:
                #increment frequency
                new_dict[word] += 1
            else:
                new_dict.update({word: 1})
    return new_dict


# get word spam probability of individual word given good and bad corpus
def get_word_spam_probability(word, good_occurrence_dict, spam_occurrence_dict):
    good_freq = 0
    bad_freq = 0
    # get num occurences
    if word in good_occurrence_dict:
        good_freq = good_occurrence_dict[word] * 2
    if word in spam_occurrence_dict:
        bad_freq = spam_occurrence_dict[word]
    # get num messages in corpus
    num_good_messages = len(good_corpus)
    num_bad_messages = len(spam_corpus)
    # if it occurs more than 1x
    if good_freq + bad_freq > 1:
        # get probability
        word_value = max(.01, min(.99, min(1.0, bad_freq / num_bad_messages) / (
                min(1.0, good_freq/num_good_messages) + min(1.0, bad_freq/num_bad_messages))))
    else:
        # if not found, it has probability of .4
        word_value = .4
    return word_value


# get probability dictionary of all words in the message
def get_word_probability_dict(message):
    # Analyze each word from message
    global good_corpus
    global spam_corpus
    # get word frequency dictionaries from both corpus
    good_occurrence_dict = create_word_occurrence_dict(good_corpus)
    spam_occurrence_dict = create_word_occurrence_dict(spam_corpus)
    # split up message
    word_list = message.split()
    new_dict = {}
    for word in word_list:
        # get the probabilities and add them to dictionary
        probability = get_word_spam_probability(word, good_occurrence_dict, spam_occurrence_dict)
        new_dict.update({word: probability})
    return new_dict


# This gets the most interesting words (ones with values furthest from .5 and creates a dictionary with them
def get_most_interesting_words(word_dict):
    new_dict = {}
    max_length = 15
    # if the message is shorter than 15 words, that becomes max length
    if len(word_dict) < 15:
        max_length = len(word_dict)
    for x in range(max_length):
        # get the word probabilities
        probabilities = list(word_dict.values())
        # get the words themselves
        words = list(word_dict.keys())
        # get the max word from the current dictionary
        max_word = words[probabilities.index(max(probabilities))]
        # add it to new dictionary of important words
        new_dict.update({max_word: word_dict[max_word]})
        # delete previous max word so you can get next max
        word_dict.pop(max_word)
    return new_dict

# This gets the combined probability of a dictionary of word / probability pairs
def get_combined_probability(word_dict):
    product = 1
    inverse_product = 1
    for word in word_dict:
        product *= word_dict[word]
        inverse_product *= (1 - word_dict[word])
    return product / (product + inverse_product)


# Determines probability of spam message
def determine_spam_probability(message):
    # Gets the probability that each token is spam
    token_spam_probability_dict = get_word_probability_dict(message)
    # Gets the most interesting tokens from the message
    interesting_tokens_dict = get_most_interesting_words(token_spam_probability_dict)
    print(interesting_tokens_dict) # To show this works as intended
    # this gets combined probability of every word in message
    message_spam_probability = get_combined_probability(interesting_tokens_dict)
    # this rounds the decimal to the 4th place
    return round(message_spam_probability, 4)


test1_spam = "i am samiam and i do not like that spam"
test2_good = "i do i do like green eggs and ham "
test3_mixed = "i like green eggs and ham but only if it is not made by that spamiam because i do not like spam no spam no spam"
print("\n")
test1_probability = determine_spam_probability(test1_spam)
print("Test 1 Spam probability is " + str(test1_probability) + "\n")
test2_probability = determine_spam_probability(test2_good)
print("Test 2 Spam probability is " + str(test2_probability) + "\n")
test3_probability = determine_spam_probability(test3_mixed)
print("Test 3 Spam probability is " + str(test3_probability) + "\n")


