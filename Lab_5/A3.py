def make_abbreviation(text: str) -> str:
    words = text.split()
    abbr = "".join([w[0].upper() for w in words if len(w) >= 3])
    return abbr

# Пример
print(make_abbreviation("New York City"))          # NYC
print(make_abbreviation("Yanka Kupala State University of Grodno"))  # YKSUG
