from sentences import get_determiner, get_noun, get_preposition, get_verb, get_prepositional_phrase, get_adjectives
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_nouns():
    # 1. Test the single determiners.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns



def test_get_verbs():
    # 1. Test the single determiners.

    single_verbs_present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_verbs_present

    # 2. Test the plural determiners.

    plural_verbs_present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_verbs_present



    verbs_past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        single_word = get_verb(1, "past")
        plural_word = get_verb(2, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert single_word in verbs_past
        assert plural_word in verbs_past



    verbs_future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        single_word = get_verb(1, "future")
        plural_word = get_verb(2, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert single_word in verbs_future
        assert plural_word in verbs_future
 
def test_get_preposition():
    # 1. Test the prepositions.

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the list.
        assert word in prepositions

def test_get_adjectives():

    adjectives = ["yellow", "wild", "magical", "hungry", "kind", "obsolete", "fortunate", "polite"]

    for _ in range(4):

        word = get_adjectives()

        assert word in adjectives

def test_get_prepositional_phrase():

    #Test if the length of get_prepositional_phrase is 3:
    assert 3 == len(get_prepositional_phrase(1))


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])