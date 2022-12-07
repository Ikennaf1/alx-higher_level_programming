#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        best_score_key = None
        for x in a_dictionary:
            if best_score_key is None:
                best_score_key = x
            if a_dictionary[x] > a_dictionary[best_score_key]:
                best_score_key = x
    else:
        return None
    return best_score_key
