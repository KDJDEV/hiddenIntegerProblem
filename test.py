target = 10
def probabilityOfSuccessfulTest(hiddenInteger):
    return (hiddenInteger - target + 21) / 20

hiddenInteger = 3
totalRolls = 600
successfulRolls = int(totalRolls * probabilityOfSuccessfulTest(hiddenInteger))
print(f"Total Rolls: {totalRolls} Successful Rolls: {successfulRolls}")

from scipy.stats import binom
def predictHiddenIntegerWithConfidence(totalRolls, successfulRolls):
    probs = []
    for h in range(-5, 6):
        p = probabilityOfSuccessfulTest(h)

        dist = binom(totalRolls, p)
        prob = dist.pmf(successfulRolls)
        probs.append(prob)

    closest = max(probs)
    guess = probs.index(closest) - 5
    confidence = closest / sum(probs)
    return guess, confidence

guess, confidence = predictHiddenIntegerWithConfidence(totalRolls, successfulRolls)
print(f"I guess {guess} with a confidence of {round(confidence * 100)}%!")