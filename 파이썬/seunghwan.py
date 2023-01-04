# from nltk.tokenize import TreebankWordTokenizer

# tokenizer = TreebankWordTokenizer()
# text = "Model-based RL don't need a value function for the policy."
# print(tokenizer.tokenize(text))

# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# print(stopwords.words('english')[:5])

# import nltk
# nltk.download('stopwords')

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# input_sentence = "We should all study hard for the exam."
# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(input_sentence)
# result = []
# for w in word_tokens:
#     if w not in stop_words:
#         result.append(w)
# print(word_tokens)
# print(result)

# from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords

# stop_words = set(stopwords.words('english'))
# stop_words.add("1")
# stop_words.add(".")
# stop_words.add("?")
# stop_words.add(",")

# input_sentence = """Hello professor, Iam currently listening your Python course. I have some question regarding this mid-term Python exam.
# I think my exam score is currently incorrect. Would you please double-check my exam score?"""


# word_tokens = word_tokenize(input_sentence)
# print(word_tokens)

# result = []
# for w in word_tokens:
#     if w not in stop_words:
#         w = w.lower()
#         result.append(w)
# print(result)

# vocab = {}
# for w in result:
#     if w not in vocab:
#         vocab[w] = 1
#     else:
#         vocab[w] += 1
# print(vocab)

# vocab_sort = sorted(vocab.items(), key = lambda x:x[1], reverse = True)
# print(vocab_sort)
# word2inx = {word[0] : index + 1 for index, word in enumerate(vocab_sort)}
# print (word2inx)

