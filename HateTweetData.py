import sys
import csv
import json

def main():
    with open(sys.argv[1]) as hatefile, \
         open("hatetweets.txt", "wt") as w:
        tsv_writer = csv.writer(w)
        reader = csv.reader(hatefile)
        count = 0

        for tweet in reader:
            #Specific code for twitter-hate1.csv file
            #if(tweet[0] == "The tweet contains hate speech"):
                #count += 1
                #tsv_writer.writerow(['1' + '\t' + ''.join(tweet[1])])

            #Specific code for twitter-hate2.csv file
            if(tweet[5] == "0"):
                count += 1
                tsv_writer.writerow([''.join("1" + "\t" + tweet[6])])
        tsv_writer.writerow([count])
            




if __name__ == "__main__":
    main()
