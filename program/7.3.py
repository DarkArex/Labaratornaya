def Stats(text):
    letters = 0
    words = 0
    lines = 0

    with open(text, 'r') as file:
        for line in file:
            letters += sum(c.isalpha() for c in line)
            words += len(line.split())
            lines += 1
    print(f'Input file contains:')
    print(f'{letters} letters')
    print(f'{words} words')
    print(f'{lines} lines')
if __name__ == "__main__":
    text = "input.txt"
    Stats(text)