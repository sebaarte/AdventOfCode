import re




def parse():
    summ = 0
    mul_regex = r"mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)"
    with open("day3/data.txt") as file:
        content = file.read()
        matches = re.findall(mul_regex,content)
        for i in matches:
            summ += i.group(0)        



if __name__ == "__main__":
    parse()