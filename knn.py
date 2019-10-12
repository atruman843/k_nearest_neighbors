from progress.bar import Bar

class knn:

    k = 0
    numLabels = 10

    def __init__(self, k, numLabels, trainingData, trainingLabel, testData, testLabel):
        self.k = k
        self.numLabels = numLabels
        self.trainingData = trainingData
        self.trainingLabel = trainingLabel
        self.testData = testData
        self.testLabel = testLabel
        self.predictions = []

    def getDistances(self):
        statusBar = Bar('Calculating distances', max = len(self.testData))
        for index1, test in enumerate(self.testData):
            labels = [0] * self.numLabels
            distances = []
            sortedDistances = []
            for index2, train in enumerate(self.trainingData):
                newDistance = self.euclideanDistance(test, train)
                distances.append([newDistance, self.trainingLabel[index2]])
            sortedDistances = sorted(distances, key=lambda distance: distance[0])
            for i in range(0, self.k):
                labels[int(sortedDistances[i][1])] += 1
            maxInd = 0
            for ind, num in enumerate(labels):
                if num > labels[maxInd]:
                    maxInd = ind
            self.predictions.append(maxInd)
            statusBar.next()
        statusBar.finish()

    def stats(self):
        totalCorrect = 0
        truePositive = 0
        falsePositive = 0
        trueNegative = 0
        falseNegative = 0
        for index, prediction in enumerate(self.predictions):
            # print 'Test  #{testNum} predicted: {prediction} Test #{testNum} actual: {actual}'.format(testNum=index, prediction=prediction, actual=self.testLabel[index])
            if (prediction == self.testLabel[index] and prediction == 1):
                truePositive += 1
                totalCorrect += 1
            elif (prediction == self.testLabel[index] and prediction == 0):
                trueNegative += 1
                totalCorrect += 1
            elif (prediction == 1 and self.testLabel[index] == 0):
                falsePositive += 1
            else:
                falseNegative += 1
        print ('\n' + \
               '===========\n' + \
               'Statistics: \n' + \
               '===========\n' + \
               'Total Correct: {percentCorrect}%\n' + \
               ' True Positive: {truePositive}\n' + \
               'False Positive: {falsePositive}\n' + \
               ' True Negative: {trueNegative}\n' + \
               'False Negative: {falseNegative}').format(percentCorrect=float(100*totalCorrect/len(self.testLabel)), \
                                                 truePositive=truePositive, falsePositive=falsePositive, \
                                                 trueNegative=trueNegative, falseNegative=falseNegative)

    def euclideanDistance(self, test, train):
        sum = 0
        for coord1, coord2 in zip(test, train):
            sum += ((coord2 - coord1)**2)
        return (sum**0.5)

    def manhattanDistance(self, test, train):
        sum = 0
        for coord1, coord2 in zip(test, train):
            sum += abs(coord2 - coord1)
        return sum

    def chebyshevDistance(self, test, train):
        maximumDist = 0
        for coord1, coord2 in zip(test, train):
            diff = abs(coord2 - coord1)
            if diff > maximumDist:
                maximumDist = diff
        return maximumDist
