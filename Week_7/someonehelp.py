import random
# *************************************

def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')
# *************************************

def get_input():
    return input().lower()

# *************************************

def main():

    answers = ['Have you tried it on a different operating system', 'Did you reboot it', 'What color is it', 'you should consider installing antiv-virus software','contact telkom','I should get that looked at if i were you']

    welcome()  
    while True:
        rand_idx = random.randint(0, len(answers)- 1) 
        random_num = answers[rand_idx] 

        query = get_input()
      
        if query == 'quit':
          break
        else:
          print (str(random_num))

    while (not query=='quit'):
        print('Curious, tell me more.')
        query = get_input()
       
        
main()   
# *************************************
if __name__ == "__main__":
    main()
 
# *************************************
