import csv

class diabetesClassifier:

    fileName = 'diabetes'
    data = []
    max = []
    trainingLabel = []
    testLabel = []
    trainingData = []
    testData = []

    def __init__(self):
        self.fileInput()
        self.preProcessData()
        self.splitData()

    def fileInput(self):
        with open(('./data/' + self.fileName + '.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for index1, row in enumerate(csv_reader):
                self.data.append([])
                for index2, item in enumerate(row):
                    item = float(item)
                    self.data[index1].append(item)
                    if index2 == len(row) - 1:
                        continue
                    else:
                        if index1 == 0:
                            self.max.append(item)
                        elif item > self.max[index2]:
                            self.max[index2] = item


    def preProcessData(self):
        for index1, row in enumerate(self.data):
            for index2, item in enumerate(row):
                if index2 == len(row) - 1:
                    continue
                else:
                    self.data[index1][index2] = float(item/self.max[index2])

    def splitData(self):
        trainSplit = int(0.8 * len(self.data))
        for index1, row in enumerate(self.data):
            if index1 < trainSplit:
                self.trainingLabel.append(row[len(row)-1])
                self.trainingData.append(row[1:len(row)-2])
            else:
                self.testLabel.append(row[len(row)-1])
                self.testData.append(row[1:len(row)-2])

    def getData(self):
        return [self.trainingData, self.trainingLabel, self.testData, self.testLabel]
