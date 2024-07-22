def reverse_with_spaces(text):
    reversed_chars = text[::-1].replace(" ", '') 
    result = ""
    j = 0 # Fix index to zero-based
    
    for i in text:
        if i == ' ':
            result += ' '
        else:
            result += reversed_chars[j]
            j += 1
    
    return result

original_string = "i am a java developer"
reversed_string = reverse_with_spaces(original_string)
print(reversed_string)
