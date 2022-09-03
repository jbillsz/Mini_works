
"""
Created on Tue Jan 11 15:34:34 2022
A class which incorporates a log in system
@author: User
"""
#defining the user class
class user():
    #creating a class method called deets
    def deets(self):
        #self.name and self.age attributes which take in input parameters
        self.name = input('What is your name: ')
        self.age = int(input("What is your age? :"))
        print(f'Your name is {self.name} and age is {self.age}.')
  
    #password class which allows the user to set a username and password and
    #stores it in a dictionary and to which a for loop prints the key and values
    def password(self):
        
        self.user_name = input(" Input user name:")
        self.password = input('set password: ')
        user_name = {self.user_name:self.password}
        for key,value in user_name.items():
            print(f"\nYour name is {self.name}"
                  f"\nYour username is {key}."
                  f"\nYour password is {value}")
    #login method which validates the username and password authenticity by
    #comparing it to the key and value in the user_name dictionary representing
    #a while loop with a nested if-else statement to navigate the log in system
    def login(self):
        user_name = {self.user_name:self.password}
        login = 0
        self.login_user = input('Input user name:')
        self.login_pass = input('Input pass word:')
                
        while login < 3:
            if self.login== user_name[self.user_name]:
                print("Access Granted")
                break
            else:
               print("Try again!")
               login += 1
               break

#A simple inheritance
class male_user(user):
   #I figured out that all attributes can be created under a method, if 
   #I do not want to define all attributes under at instantiating point.
    def __init__(self):
        super(male_user, self).__init__()
        self.priviledge_1 = 'can delete post.'
        self.priviledge_2 = 'can ban women.'
    def kill(self):
        print('Me')
   
    def display_priviledge(self):
       print(self.priviledge_1,
           self.priviledge_2)
       

Louis = male_user()
Louis.deets()
Louis.password()
Louis.display_priviledge()