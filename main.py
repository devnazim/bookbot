def count_letters(txt):
    lower_txt = txt.lower()
    char_dict = {}
    for char in lower_txt:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    arr = list(filter(lambda d: d[0].isalpha(), char_dict.items()))
    arr.sort(reverse=True, key=lambda d: d[1])
    print(arr)

    return arr

def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read() 
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(file_content.split())} words found in the document")
        count = count_letters(file_content)

        for c in count:
            print(f"The '{c[0]}' character was found {c[1]} times")

        print("--- End report ---")

main()
