# write your code here
# print("""# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# * Imagine
# * Norwegian Wood
# * Come Together
# * In My Life
# * ~~Hey Jude~~ (that was *McCartney*)""")

def get_list(t):
    rows = int(input("- Number of rows: "))
    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("- Number of rows: "))

    list = ""
    for i in range(rows):
        line = input("- Row #1: ")
        if t == 'o':
            line = str(i + 1) + ". " + line
        else:
            line = "* " + line
        line += "\n"
        list += line

    return list


user_option = None
text = ""
while user_option != "!done":
    user_option = input("- Choose a formatter: ")
    if user_option == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
              "Special commands: !help !done")

    elif user_option == 'plain':
        text += input("-Text: ")
    elif user_option == 'bold':
        text += f'**{input("-Text: ")}**'
    elif user_option == 'italic':
        text += f'*{input("-Text: ")}*'
    elif user_option == 'header':
        level = int(input("Level: "))
        header = input("-Text: ")
        hashes = '#' * level
        text += hashes + " " + header + "\n"

    elif user_option == 'link':
        label = input("Label: ")
        url = input("URL: ")
        text += f"[{label}]({url})"

    elif user_option == 'inline-code':
        text += f"`{input('-Text: ')}`"
    elif user_option == 'ordered-list':
        text += get_list('o')

    elif user_option == 'unordered-list':
        text += get_list('u')
    elif user_option == 'new-line':
        text += "\n"

    else:
        print("Unknown formatting type or command")
    print(text)

with open('output.md', 'w') as md_file:
    md_file.write(text)

