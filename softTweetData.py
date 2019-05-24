import sys
import csv
import json

def main():
    with open(sys.argv[1]) as hatefile, \
         open("softtweets.txt", "wt") as w:
        tsv_writer = csv.writer(w)
        reader = csv.reader(hatefile)
        count = 0

        for tweet in reader:
            #Specific code for soft_tweets.csv
            if(count <= 2717):
                tsv_writer.writerow([''.join("0" + "\t" + tweet[0])])
                count = count + 1
        tsv_writer.writerow([count])
            




if __name__ == "__main__":
    main()
