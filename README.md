
In order to execute the program, from the command line, call:

    `python main.py -c [CLASSIFIER] -k [K] -n [NUMLABELS]`

An example command is as follows:

    `python main.py -c diabetes -k 5 -n 2`
    
*******************************************************************************
*******************************************************************************

| Argument Flag | Description                                                                               |
|---------------|-------------------------------------------------------------------------------------------|
|-c, --classifer|specifies which dataset to examine (either 'diabetes' or 'digits')                         |
|-k             |specifies the k value for your program                                                     |
|-n, --numLabels|specifies the dimensionality of your data (for both datasets, the dimensionality is two(2))|

To enable a different distance metric, change line 24 in the knn.py file to the
distance metric you would like. (Euclidean, Manhattan, and Chebyshev are available)
