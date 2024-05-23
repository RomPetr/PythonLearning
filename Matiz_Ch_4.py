magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see you next trick, {magician.title()}.\n")
# ------------------------------------------------
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
