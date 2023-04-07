#################
## CHALLENGE 2 ##
#################

# Requirements
# * Define a Password class that supports two instance attributes: strength and length
# * The class should generate a random password having the following characteristics, depending on strength:
# - low: include a mix of 8 lowercase and uppercase letters only
# - mid: a mix of 12 lowercase and uppercase letters and numbers
# - high: a mix of 16 lowercase and uppercase letters and numbers and punctuation signs
# * If the user specifies a length, the user-specified one overrides the defaults above
# * If the user does not specify a strength, assume "high"
# * Finally, the class should also implement a method called show_input_universe() which is not specific to the instance.
# The method should return a dict of lists exposing the pools of characters from where the sampling is done, e.g.
# {"letters": ["a", "b"...], "numbers": [0, 1, 2...], "punctuation": ["!", "?"...]}.

# Example Usage
# p1 = Password(strength="low")
# p1.password
# LAyuu4EI

# p2 = Password(strength="mid", length=37)
# p2.password
# D6tjKt885vM2U5IwHYqhr9aL6SbIBhHJ16gZf

# p3 = Password(strength="high")
# p3.password
# 71'Z>fG{9gIUQQ2a

# p4 = Password()
# p4.password
# IGYY2veeqz1Q

from string import ascii_letters, punctuation
from random import choices
from copy import copy

class Password():
    """A password of customize strength and length.

    Encapsulate a randomly generate password depending on the user-specified strength and length, where the latter
    is optional and automatically set depending on the strength (low -> 8, mid -> 12, high -> 16). If a length is
    user-specified these presets are overridden regardless of the strength.

    :param strength: a measure of the password's effectiveness against brute-force guessing
    :type strength: str, optional

    :param length: the length of the password
    :type length: int, optional
    """

    universal_numbers = {
        "letters" : list(ascii_letters),
        "numbers" : list(range(10)),
        "punctuation" : list(punctuation)
    }

    default_length = {
        'low' : 8,
        'mid' : 12,
        'high' : 16
    }

    @classmethod
    def show_input_universe(cls):
        return cls.universal_numbers

    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length

    def _generatePassword(self):
        """ 
        combination = self.universal_numbers["letters"] 
        -> here combination refers to place in memory,
        if it changes in previous iteration then that change will also reflect in current iteration.
        So to overcome this we use copy of universal_numbers.
        """
        combination = copy(self.universal_numbers["letters"])
        length = self.length or self.default_length[self.strength]     

        if self.strength == 'mid':
            combination += self.universal_numbers["numbers"]
        elif self.strength == 'high':
            combination += self.universal_numbers["numbers"] + self.universal_numbers["punctuation"]
        
        password = "".join(list(map(lambda x: str(x), choices(combination, k=length))))

        return password

if __name__ == "__main__":   
    # print(Password.show_input_universe())
    ins1 = Password("low")
    print("Low strength Password : ", ins1._generatePassword())

    ins1 = Password("low", 10)
    print("Low strength Password with 10 chars : ", ins1._generatePassword())

    ins1 = Password("mid")
    print("Mid strength Password : ", ins1._generatePassword())

    ins1 = Password("mid", 5)
    print("Mid strength Password with 5 chars : ", ins1._generatePassword())

    ins1 = Password("high", 10)
    print("High strength Password with 10 chars : ", ins1._generatePassword())

    ins1 = Password()
    print("Default strength Password : ", ins1._generatePassword())
