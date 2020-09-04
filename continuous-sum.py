inputSeq = [6, 2, 4, 1, 5]
targetSum = 6
import pdb

def countSubSequence(inputSeq, targetSum):
    elementsFound = []
    i = 0;

    while (i < len(inputSeq)):
        currentItem = inputSeq[i]
        localElementsList = [currentItem]
        currentSum = currentItem
        k = i+1
        while (k <= len(inputSeq)):
            if (currentSum == targetSum):
                elementsFound.append(localElementsList)
                if (i!= 0):
                    i = k-1 
                break

            if (k == len(inputSeq)):
                break
            currentSum +=  inputSeq[k]
            localElementsList.append(inputSeq[k])
            if (currentSum > targetSum):
                break
            k  += 1

        i+= 1
    return elementsFound


print (countSubSequence(inputSeq, targetSum))