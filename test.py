target = 10
def probabilityOfSuccessfulTest(hiddenInteger):
    return (hiddenInteger - target + 21) / 20

hiddenInteger = 0
totalRolls = 300
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

    maxProb = max(probs)
    guess = probs.index(maxProb) - 5
    confidence = maxProb / sum(probs)
    return guess, confidence

guess, confidence = predictHiddenIntegerWithConfidence(totalRolls, successfulRolls)
print(f"I guess {guess} with a confidence of {round(confidence * 100)}%!")