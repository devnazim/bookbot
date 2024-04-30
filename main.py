def count_letters(txt):
    lower_txt = txt.lower()
    char_dict = {}
    res = []
    def sort_on(d):
        return d["count"]
    for char in lower_txt:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for letter in char_dict:
        if letter.isalpha():
            # res.append(dict([(letter, char_dict[letter])]))
            res.append({ 'letter': letter, 'count': char_dict[letter] })
    res.sort(reverse=True, key=sort_on)
    return res

def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read() 
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(file_content.split())} words found in the document")
        count = count_letters(file_content)

        for c in count:
            print(f"The '{c['letter']}' character was found {c['count']} times")

        print("--- End report ---")

main()
