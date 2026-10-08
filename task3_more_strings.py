# Assignment 8 - Task 3
# More experiments with strings

text = "apple banana apple orange banana apple"

print("--- Original text ---")
print(text)

print("\n--- Different find() calls ---")
print("First apple:", text.find("apple"))
print("Apple after index 1:", text.find("apple", 1))
print("Apple after index 15:", text.find("apple", 15))
print("Banana between 0 and 20:", text.find("banana", 0, 20))
print("Orange between 0 and 15:", text.find("orange", 0, 15))

print("\n--- Different rfind() calls ---")
print("Last apple:", text.rfind("apple"))
print("Last banana:", text.rfind("banana"))
print("Last apple before index 25:", text.rfind("apple", 0, 25))

print("\n--- Extracting substrings using find() ---")

first_apple = text.find("apple")
first_banana = text.find("banana")

part = text[first_apple:first_banana]
print("From first apple to first banana:", part)

orange_pos = text.find("orange")
after_orange = text[orange_pos:]
print("From orange to the end:", after_orange)

print("\n--- More slicing ---")
print("First 12 characters:", text[:12])
print("From index 13 to the end:", text[13:])
print("Every third character:", text[::3])
print("Reversed:", text[::-1])
