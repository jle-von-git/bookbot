def count_words(text: str) -> int:
    return len(text.split())

def get_char_nums(text: str) -> dict:
    char_nums = {}
    for char in text.lower():
        if char not in char_nums:
            char_nums[char] = 0
        
        char_nums[char] += 1
    
    return char_nums

def sort_char_nums(chars_nums: dict) -> list:
    chars_nums_to_sort = []
    for char in chars_nums:
        num = chars_nums[char]
        chars_nums_to_sort.append(
            {"char": char, "num": num}
        )

    chars_nums_to_sort.sort(
        reverse=True,
        key=lambda item: item["num"]
    )

    return chars_nums_to_sort