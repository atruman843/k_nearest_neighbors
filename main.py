import argparse
import diabetesClassifier
import digitClassifier
import knn
import time

parser = argparse.ArgumentParser(description = 'This script processes data in the \
                                 data folder through the knn algorithm.')

parser.add_argument('-c', '--classifier', action='store', help='Specify which classifier you want.', required=True)
parser.add_argument('-k', action='store', help='Specify how big your k should be.', required=True)
parser.add_argument('-n', '--numLabels', action='store', help='Specify the cardinality of the set of labels.', required=True)

args = parser.parse_args()

fileName = args.classifier
k = int(args.k)
numLabels = int(args.numLabels)

start = time.time()
progTime = start
if fileName == 'diabetes':
    classifier = diabetesClassifier.diabetesClassifier()
elif fileName == 'digits':
    classifier = digitClassifier.digitClassifier()

data = classifier.getData()

classify = knn.knn(k, numLabels, data[0], data[1], data[2], data[3])
classify.getDistances()
classify.stats()
print '---------------------- {} seconds ----------------------'.format(time.time() - progTime)
progTime = time.time()
k += 2
