# \t - tab
# \n - new line
# rstrip() - strip whitespace from right
# lstrip() - strip whitespace from left
# strip() - strip whitespace from both sides

name = "Ray "
name = name.rstrip()

message = f"\tMy name is {name}."
message2 = "\tI'm learning Python for the 50th time."

print(message)
print(message2)


"""
Removing prefixes
"""
url = "https://github.com/rlanier-webdev"
url = url.removeprefix("https://")
print("Github URL: ", url)
