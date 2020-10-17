alienDictionary = {"we": "vorag", "come": "thang", "in": "zon", "peace": "argh", "hello": "kodar", "can": "zank", "i": "az", "borrow": "liftit"}
englishPhrase = input ("please enter a word or a phrase in English")
englishWords = englishPhrase.lower().split()
alienWords = []
for word in englishPhrase:
    if word in alienDictionary:
        alienWords.append(alienDictionary[word])
    else:
        alienWords.append (word)
    
         
print ("In alien, say","".join(alienWords))
