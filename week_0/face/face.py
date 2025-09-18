def main():
    # Output using our own function
    user_text = input("enter text : ")
    convert(user_text)


# Create our own function
def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "☹️")
    print(text)

main()

