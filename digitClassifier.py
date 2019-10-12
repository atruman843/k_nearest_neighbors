import csv

class digitClassifier:

    fileName = 'digits'
    keyDigit = 7.0
    data = []
    max = []
    trainingLabel = []
    testLabel = []
    trainingData = []
    testData = []

    def __init__(self):
        self.fileInput()
        self.splitData()

    def fileInput(self):
        with open(('./data/' + self.fileName + '.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for index1, row in enumerate(csv_reader):
                self.data.append([])
                sum = 0

                for index2, item in enumerate(row):
                    if index2 == 0:
                        item = float(item)
                        if item == self.keyDigit:
                            item = 1
                        else:
                            item = 0
                        self.data[index1].append(item)
                    elif index2%28 == 0 and not (index2 == 0):
                        self.data[index1].append(sum)
                        sum = 0
                    else:
                        sum += float(item)/255


    def splitData(self):
        trainSplit = int(0.8 * len(self.data))
        for index1, row in enumerate(self.data):
            if index1 < trainSplit:
                self.trainingLabel.append(row[0])
                self.trainingData.append(row[1:len(row)-1])
            else:
                self.testLabel.append(row[0])
                self.testData.append(row[1:len(row)-1])

    def getData(self):
        return [self.trainingData, self.trainingLabel, self.testData, self.testLabel]
