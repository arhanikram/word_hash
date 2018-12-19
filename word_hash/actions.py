"""
-------------------------------------------------------
actions.py
Insert words into a hashSet and keep track of occurrences
and comparisons.
-------------------------------------------------------
Author:  Arhan Ikram
__updated__ = "2018-03-22"
-------------------------------------------------------
"""
from word import Word


def insert_words(file_variable, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a HashSet.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        hash_set - the HashSet to insert the words into (HashSet)
    Postconditions:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    words = file_variable.read().lower().replace('\n', ' ').split(" ")
    for i in words:
        if i.isalpha():
            hash_set.insert(Word(i))


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Preconditions:
        hash_set - a hash set of Word objects (HashSet)
    Postconditions:
        returns
        total - the total of all comparison fields in the HashSet
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    for i in hash_set:
        total += i.comparisons
        if not max_word or i.comparisons > max_word.comparisons:
            max_word = i

    return total, max_word
