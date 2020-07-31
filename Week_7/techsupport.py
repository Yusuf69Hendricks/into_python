
# *************************************
def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')
# *************************************
def get_input():
  return input().lower()
# *************************************

def main():

    welcome()  
    while True:
      query = get_input() 
    
      if 'crashed' in query:
        print("Are the drivers up to date?")

      elif 'bluetooth' in query:
        print("Have you tried mouthwash?")

      elif 'blue' in query: 
        print("Ah, the blue screen of death. And then what happened?")
        
      elif 'hacked' in query:
        print("You should consider installing anti-virus software.")
      
      elif 'windows' in query:
        print("Ah, i think i see your problem. What version?")

      elif 'apple' in query:
        print("You do mean the computer kind?")

      elif 'spam' in query:
        print("You Should see if your mail client can filter")
        
      elif 'connection' in query:
        print("Contact Telkom.")
       

      elif not query=='quit':
        print('Curious, tell me more.')
    
      elif 'quit' in query:
        break  
        
main()   
# ************************************* 