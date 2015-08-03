#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
import sys

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i+order]
        next_letter = text[i+order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model

def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print output

if __name__ == "__main__":
    text = "It doesn't hurt me Do you wanna feel how it feels?  Do you wanna know, know that it doesn't hurt me? Do you wanna hear about the deal that I'm making?  You It's you and me And if I only could I'd make a deal with God And I'd get him to swap our places Be running up that road Be running up that hill Be running up that building See if I only could, oh You don't wanna hurt me But see how deep the bullet lies Unaware I'm tearing you asunder Oh, there is thunder in our hearts Is there so much hate for the ones we love? Well tell me, we both matter, don't we?  You It's you and me It's you and me won't be unhappy And if I only could I'd make a deal with God And I'd get him to swap our places Be running up that road Be running up that hill Be running up that building Say, if I only could, oh You It's you and me It's you and me won't be unhappy Oh c'mon, baby, c'mon darling Let me steal this moment from you now. C'mon, angel, c'mon, c'mon, darling Let's exchange the experience, oh And if I only could I'd make a deal with God And I'd get him to swap our places I'd be running up that road Be running up that hill With no problems See and if I only could I'd make a deal with God And I'd get him to swap our places Be running up that road Be running up that hill With no problems So if I only could I'd make a deal with God And I'd get him to swap our places I'd be running up that road Be running up that hillWith no problems So if I only could  Be running up that hill  With no problems If I only could, I'd be running up that hill If I only could, I'd be running up that hill"

    generateText(text, int(sys.argv[1]), int(sys.argv[2]))
