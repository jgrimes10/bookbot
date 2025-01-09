def main():
    try:
        prepare_report("books/frankenstein.txt")
    except Exception as e:
        print(e)

def get_text_from_path(path):
    """Gets the entire contents of a file at the given filepath."""
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    """Returns the number of words in the given string."""
    words = text.split()
    return len(words) 

def character_count(text):
    return_dictionary = {}
    lower_text = text.lower()

    for character in lower_text:
        if character in return_dictionary:
            return_dictionary[character] += 1
        else:
            return_dictionary[character] = 1

    return return_dictionary

def sort_on(dict):
    return dict["num"]

def prepare_report(path):
    text = get_text_from_path(path)
    words = word_count(text)
    characters_dict = character_count(text)
    characters_list = []

    for character in characters_dict:
        if character.isalpha():
            entry = { "character": character, "num": characters_dict[character] }
            characters_list.append(entry)

    characters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    
    for character in characters_list:
        char = character["character"]
        num = character["num"]

        print(f"The '{char}' was found {num} times")

    print("--- End Report ---")

main()
