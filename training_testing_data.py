import sys
import csv
import json

def trainingData(dataset):
    training = []
    for i in range((int) (len(dataset) * 0.9)):
        training.append(dataset[i])
    return training

def main():
    with open(sys.argv[1]) as data, \
         open("training_data.txt", "wt") as training, \
         open("testing_data.txt", "wt") as testing:
        tweets = []
        count = 0
        tsv_reader = csv.reader(data)
        tsv_train = csv.writer(training)
        tsv_test = csv.writer(testing)

        for tweet in tsv_reader:
            tweets.append(tweet[0])

        trained = trainingData(tweets)

        for train_tweet in trained:
            tsv_train.writerow([train_tweet])

if __name__ == "__main__":
    main()
