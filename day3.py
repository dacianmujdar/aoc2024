import re

if __name__ == '__main__':
    with open("./input/day3.txt", "r") as f:
        text = f.read()
    clean_pattern = r"don't\(\).*?do\(\)"
    cleaned_text = re.sub(clean_pattern, "", text, flags=re.DOTALL)

    pattern = "mul\(\d{1,3},\s*\d{1,3}\)"
    matches = re.findall(pattern, cleaned_text)

    numbers = [m[4:-1].split(',') for m in matches]
    print(sum([int(number[0]) * int(number[1]) for number in numbers]))
