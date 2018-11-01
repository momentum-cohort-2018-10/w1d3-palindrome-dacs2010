#for the test.sh file
#./test.sh
#brew install round up

user_input = input("Write something ").lower()

def clean_text(some_input):
    #sets new empty string
    new_text = ""
    #check each character and make the input lowercase
    for char in some_input.lower():
        #if the character is part of the alphabet...
        if char.isalpha():
            #add it to the new string
            new_text = new_text + char
    return new_text


def is_palindrome(user_input):
    #show each stage of interation
    print(user_input)
    #check for an empty string...
    #(note: if this is in another location it throws errors)
    if user_input == '':
        #if it is the it's a Palindrome! 
        print("Palindrome!")
        return 
    #check if first and last index are the same    
    elif user_input[0] == user_input[-1]:
        #remove first and last part of string
        is_palindrome(user_input[1:-1])
    else:
        #doesn't meet previous standards
        print("Nope, not a palindrome...")
        return


is_palindrome(clean_text(user_input))


# def inner(text):
#     print(text)
#     if len(text) > 1:
#         inner(text[1:-1])

# inner(clean_text(user_input))