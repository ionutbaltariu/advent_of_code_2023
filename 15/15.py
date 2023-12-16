def hash(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


if __name__ == "__main__":
    file_handler = open("15.in", "r")
    content = file_handler.read().split(",")
    print(sum([hash(x) for x in content]))
    print(hash("HASH"))
