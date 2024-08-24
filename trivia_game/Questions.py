# Questions Class Module #

# Description: This is the one of three modules that was created to simulate a trivia game! In this module, I defined a class that stored the attributes (below) to systematically
        ## use them through the second module through importing the module. At the bottom is the format of the questions that will be asked the user.
 
class QuestionsClass:
    def __init__(self, trivQues, ans1, ans2, ans3, ans4, correctAns):
        self.trivQues = trivQues
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.correctAns = correctAns

    def getTrivQues(self):
        return self.trivQues
    def getAns1(self):
        return self.ans1
    def getAns2(self):
        return self.ans2
    def getAns3(self):
        return self.ans3
    def getAns4(self):
        return self.ans4
    def getCorrectAns(self):
        return self.correctAns

    def __str__(self):
        return f'{self.trivQues}\n1. {self.ans1}\n2. {self.ans2}\n3. {self.ans3}\n4. {self.ans4}'
    
