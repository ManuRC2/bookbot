import sys

def wordsInString(text: str):
    if text:
        return len(text.split())
    return 0

def countChar(text: str):
    res = dict()
    for x in text:
        times = res.get(x.lower()) or 0
        res[x.lower()] = times + 1
    return res

def reportChars(text: str):
    chardir = countChar(text)
    charlist = []
    for x in chardir.items():
        charlist.append({'char': x[0], 'num': x[1]})
    charlist.sort(reverse=True, key=lambda x: x["num"])
    for x in charlist:
        if x['char'].isalpha():
            print(f"The '{x['char']}' character was found {x['num']} times")


def main():

    if len(sys.argv) < 2:
        print("Invalid ammount of arguments.")
        return 0
    path_to_file = sys.argv[1]

    # path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        reportChars(file_contents)

if __name__ == '__main__':

    main()