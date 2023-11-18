import string
import humanize

text = string.ascii_uppercase * 100_000_000

# Show the first 50 characters
print(f"Show the first 50 characteres:\n{text[:50]}")  

print(f"{len(text)} > {humanize.intword(len(text))}")

