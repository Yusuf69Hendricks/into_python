vowels = ('AEIOUaeiou')

# **************************************
def to_pig_latin(s):
    sen = s.split(" ")
    pl= ""
    for word in sen:
      if word[0] in vowels:
          pl+= word + "way" + " "
      else:
          vowel_index = 0
          for letter in word:
              if letter not in vowels: 
                  vowel_index += 1
                  continue
              else: 
                  break
          pl+= word[vowel_index:] + "a" + word[:vowel_index] + "ay" + " "
    return pl[:len(pl) - 1]




# ****************************************
def to_english(s):
    sen = s.split(" ")
    english = ""
    for word in sen:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else: 
            noay = word[:len(word) - 2]
            first = noay.split("a")[-1]
            removed = noay[:len(noay) - (len(first)+1)]
            english += first + removed + " "
    return english


# ****************************************








    
  