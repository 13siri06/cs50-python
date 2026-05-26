def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

def main():
    x = input("Input: ")
    print(convert(x))

main()
