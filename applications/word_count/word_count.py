import string

def word_count(s):
    # Implement me.
    # removetable = str.maketrans("","",":;,.-+=/\"\t\r\n|[]{}()*^\\&")
    # translated = s.translate(removetable)
    # return translated
    new_string = ""
    blacklist = ":;,.-+=/\"|[]{}()*^\\&"
    for element in s:
        if element not in blacklist:
            new_string += element

    words = new_string.split()
    lower_words = [w.lower() for w in words]
    print(lower_words)
    
    index = {}
    for word in lower_words:
        if word not in index:
            index[word] = 1
        else:
            index[word] += 1
    return index
            



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello    hello"))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

