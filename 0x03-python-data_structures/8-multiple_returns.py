#!/usr/bin/python3
def multiple_returns(sentence):
    len_sente = len(sentence)

    if (len_sente == 0):
        mynew_tuple = (len_sente, None)
    else:
        mynew_tuple = (len_sente, sentence[0])

    return (mynew_tuple)
