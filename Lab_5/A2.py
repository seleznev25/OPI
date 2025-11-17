import re

def split_sentences(text: str):
    sentences = re.split(r'\s*(?<=[.?!])\s+', text.strip())
    for s in sentences:
        print(s)
    print("Предложений в тексте:", len(sentences))

# Пример
text = "He jests at scars. That never felt a wound!   Hello, friend!    Are you OK?"
split_sentences(text)
