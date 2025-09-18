def main():
    # Output using our own function
    user_text = input("enter text: ")
    print(convert(user_text))

# Create our own def convert
def convert(text):
    # Replace emoticons with emojis
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()
