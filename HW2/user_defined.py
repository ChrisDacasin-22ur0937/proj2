def countChar(word):
    freq = {}  
    
    word = word.lower()  
    
    for ch in word:  
        if ch.isalpha():   
            if ch in freq:
                freq[ch] = freq[ch] + 1
            else:
                freq[ch] = 1
    return freq

text = input("Enter string: ")

parts = text.split(",")

for p in parts:
    p = p.strip() 
    result = countChar(p)

    for k in result:
        print(k, "=", result[k], end=", ")
    print()
