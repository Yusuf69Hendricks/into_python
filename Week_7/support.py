import random
# *************************************
def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')
# *************************************
def get_input():
    return input('').lower()

# *************************************
def main():

    welcome()  
    while True:
      query = get_input() 
      if query == 'crashed':
        print("Are the drivers up to date?")

      elif query == 'blue': 
        print("Ah, the blue screen of death. And then what happened?")
        
      elif query == 'hacked':
        print("You should consider installing anti-virus software.")
     
      elif query == 'bluetooth':
        print("Have you tried mouthwash?")
      
      elif query == 'windows':
        print("Ah, i think i see your problem. What version?")

      elif query == 'apple':
        print("You do mean the computer kind?")

      elif query == 'spam':
        print("You Should see if your mail client can filter")
        
      elif query == 'connection':
        print("Contact Telkom.")
       

      elif not query=='quit':
        print('Curious, tell me more.')
    
      elif query == 'quit':
        break  
        
main()   
# ************************************* 