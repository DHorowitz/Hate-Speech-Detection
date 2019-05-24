import sys
import csv
import json
import numpy as np

def writeit(write, lineone, linetwo):
    write.writerow([lineone])
    write.writerow([linetwo])


def main():
    with open(sys.argv[1]) as fileone, \
         open(sys.argv[2]) as filetwo, \
         open("shuffled_tweets.txt", "wt") as sort:
        tsv_sort = csv.writer(sort)
        readone = csv.reader(fileone)
        readtwo = csv.reader(filetwo)
        lineone = []
        linetwo = []

        for line in readone:
            lineone.append(line[0])
        for line in readtwo:
            linetwo.append(line[0])

        for i in range(len(lineone)):
            if(np.random.randint(2) == 0):
                writeit(tsv_sort, lineone[i], linetwo[i])
            else:
                writeit(tsv_sort, linetwo[i], lineone[i])

        print(len(lineone))
        print(len(linetwo))
         
        

if __name__ == "__main__":
    main()
