def highlight_word(sentence, word):
    word_len = len(word)
    word_start = sentence.index(word)
    word_end = word_start + word_len
    new_sentence = sentence[: word_start]+ "" + word.upper() + ""+ sentence[word_end:]

    return new_sentence

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))