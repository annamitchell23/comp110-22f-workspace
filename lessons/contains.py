"""Example implementing a list utility function"""

# Function name: contains
# We will have 2 paramenters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Gameplan:
    # 1. Start with the first index
    i: int = 0
    # 2. Loop through every index
    while i < len(haystack):
        if haystack[i] == needle:
        #   2.A True Return True! We found it!
         return True
        i += 1
    return False