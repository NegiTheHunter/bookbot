def word_count(text):
    return len(text.split())

def character_count(text):
    count_text = text.lower()
    counts = {} 
    for char in count_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_characters(character_list):
    sort_chars = []
    keys = list(character_list)
    for key in keys:
        sort_chars.append({"char": key, "count": character_list[key]})
    sort_chars.sort(reverse=True, key=sort_on)
    return sort_chars

def sort_on(dict):
    return dict["count"]