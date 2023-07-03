def print_upper_words(list, must_start_with):
    for word in list:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())

        # if word.startswith(must_start_with[0]) or word.startswith(must_start_with[1]):
        #     print(word.upper())


            # this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

# print({3,4,3,2,6,3,2})