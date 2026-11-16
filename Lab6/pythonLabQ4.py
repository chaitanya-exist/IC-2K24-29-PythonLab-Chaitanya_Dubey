"""Q4: Word-frequency counter and simple text analysis."""


def analyse_text(text: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for raw_word in text.split():
        word = "".join(character.lower() for character in raw_word if character.isalnum())
        if word:
            frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def main() -> None:
    print("Enter a paragraph. Submit an empty line to finish:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    frequencies = analyse_text(" ".join(lines))
    if not frequencies:
        print("No words were entered.")
        return

    total_words = sum(frequencies.values())
    print(f"Total words: {total_words}")
    print(f"Unique words: {len(frequencies)}")
    top_n = input("How many frequent words should be displayed? ").strip()
    try:
        count = max(1, int(top_n))
    except ValueError:
        count = 5
    ranked = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))
    print("Most frequent words:", ranked[:count])
    print("Words used once:", sorted(word for word, amount in frequencies.items() if amount == 1))

    grouped: dict[int, list[str]] = {}
    for word, amount in frequencies.items():
        grouped.setdefault(amount, []).append(word)
    print("Words grouped by frequency:", {key: sorted(value) for key, value in sorted(grouped.items())})
    search = input("Search for a word: ").strip().lower()
    print(f"'{search}' occurs {frequencies.get(search, 0)} time(s).")


if __name__ == "__main__":
    main()
