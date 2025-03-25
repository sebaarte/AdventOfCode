import csv
from functools import reduce
import operator


def extract_data():
    data = []
    a = 0
    with open('day2/data.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            a += 1
            parsed = list(map(int,row))
            data.append(parsed) 
    return data


def assess_validity(record: list[int]):
    safety = True
    if not (sorted(record,reverse=True) == record or sorted(record, reverse=False) == record):
        safety = False
    
    for i in range(len(record)-1):
        if abs(record[i] - record[i+1]) > 3 or abs(record[i] - record[i+1]) < 1:
            safety = False

    return safety

def check_removal_of_level(record: list[int]):
    
    if assess_validity(record):
        return True

    for i,level in enumerate(record):
        rec = record.copy()
        rec.remove(level)
        if assess_validity(rec):
            return True
        
    return False

def count_safe(data):
    sum = 0
    res = list(map(check_removal_of_level,data))
    for i in res:
        sum += 1 if i else 0

    print(sum)

    liste = []
    safeReportCount = 0
    for report in data:
        if assess_validity(report) == True:
            safeReportCount += 1 
        else: # Part 2
            for i, level in enumerate(report):
                reportCopy = report.copy()
                reportCopy.pop(i)
                if assess_validity(reportCopy) == True:
                    safeReportCount += 1
                    break
    return safeReportCount


if __name__ == "__main__":
    data = extract_data()
    summ = count_safe(data)
    print(summ)

    