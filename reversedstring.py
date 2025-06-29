# This reverses a word or sentence
#Create class with empty input and output strings
#create new variable to call methods
class Reverse:
    def __init__(self):
        self.string=''
        self.result=''
    #Create method to ask user for string
    def str(self):
        self.string=(input("Enter a word/sentence: "))
    #create method using for loop to reverse the given string
   #Create method to display entered string string
    def strdisplay(self):
        print("Your entered string is: {}".format(self.string))
    def strrev(self):
        for i in self.string:
            self.result=i+self.result
    #create method for printing result
    def display(self):     
        print("Your word/sentence reversed is: {}".format(self.result))
#create new variable to call methods
string2=Reverse()
string2.str()
#string2.strdisplay()
string2.strrev()
string2.display()