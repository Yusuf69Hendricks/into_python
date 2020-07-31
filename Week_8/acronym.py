
# "The Center for Theoretical Physics and Astrophysics"
# **********************************
def main():

  # User inputing words to be excluded
  ex = input("Enter words to be ignored seperated by commas:")
  # spliting input, into seperate words
  exclude = ex.split(",")

  # creating and appending input into list
  stopwords = exclude
  stopwords.append(exclude)

  # User inputing a phrase to get accronym
  query = input("Enter a title to generate its accronym: ")
  # Seperating input to join accronym
  querywords = query.split()
 
  # removing selected words from the phrase inputed
  resultwords  = [word for word in querywords if word.lower() not in stopwords]

  # Joining the first letter[0] of the words not removed
  result =  "".join(word[0] for word in resultwords).upper()

  # Printing the result
  print("The accronym is: " + result)

main()

# **********************************
