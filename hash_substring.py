# python3

def read_input():
    in_type = input()
    if "I" in in_type:
        pat = input()
        lon = input()
    elif "F" in in_type:
        try:
            file = open("tests/06", "r")
            file_input = file.readlines()
            pat = file_input[0]
            lon = file_input[1]
            file.close()
        except FileNotFoundError:
            print("File open error")
    return (pat.rstrip(), lon.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pat, lon):
    hashp = 0
    patlen = len(pat)
    tlen = len(lon)
    res = []


    for i in range(patlen):
        hashp += ord(pat[i])
    for i in range(tlen-patlen+1):
        hasht = 0
        for k in range(patlen):
            hasht += ord(lon[i+k])
        if hashp == hasht:
            if pat == lon[i:patlen]:
                res.append(i)
    return res


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

