def spin_words(text: str, threshold: int) -> str:
    words = []
    for word in text.split():
        if len(word) >= threshold:
            word = word[::-1]
        words.append(word)
    return ' '.join(words)


def spin_words_with_comprehension(text: str, threshold: int) -> str:
    return ' '.join(w[::-1] if len(w) >= threshold else w for w in text.split())
