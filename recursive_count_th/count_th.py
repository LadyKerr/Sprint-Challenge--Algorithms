'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case
    # if the word is less than 1, then it wont have the 2 letters we're looking for
    if len(word) < 1:
        return 0
    # recursive case
    # if the first 2 letters of the word includes `th`
    if word[:2] == "th":
        # increment the function by 1 and return the num of times word
        return 1 + count_th(word[1:])
    # otherwise, just return the nums of letters in the word
    else:
        return count_th(word[1:])
