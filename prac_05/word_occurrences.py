def word_count():
    """
    Estimated time: 30 minutes
    Actual time: 24 minutes
    """

    text = input("Text: ")

    # Split the text into words
    words = text.split()

    word_counts = {}

    # Count occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1

        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items())

    longest_word_length = max(len(word) for word, count in sorted_words)

    for word, count in sorted_words:
        print(f"{word:{longest_word_length}} : {count}")

if __name__ == "__main__":
            word_count()


