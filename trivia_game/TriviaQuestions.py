# Trivia Questions Module #

# Description: This is the second of three modules used in this program. In this module, I created a function that would create a list of objects that are the questions that are going
        ## to be asked to participants. It has all of the vital information needed for the driver program as well.


# Questions is the file name and QuestionsClass is the class name

import Questions

def TriviaQuestions():

    global TrivQuestions
    
    TrivQuestions = []

    question1 = Questions.QuestionsClass('How many days are in a lunar year?',\
                                         '354','365','243','379',1)

    TrivQuestions.append(question1)
    
    question2 = Questions.QuestionsClass('What is the largest planet?',\
                                         'Mars','Jupiter','Earth','Pluto',2)
    TrivQuestions.append(question2)
    
    question3 = Questions.QuestionsClass('What is the largest kind of whale?',\
                                         'Orca whale', 'Humpback whale', 'Beluga whale',\
                                         'Blue whale',4)
    TrivQuestions.append(question3)

    question4 = Questions.QuestionsClass('Which dinosaur could fly?',\
                                         'Triceratops', 'Tyrannosaurus Rex', 'Pteranodon',\
                                         'Diplodocus',3)
    TrivQuestions.append(question4)

    question5 = Questions.QuestionsClass('Which of these Winnie the Pooh characters is a donkey?',\
                                         'Pooh','Eeyore','Piglet','Kanga',2)
    TrivQuestions.append(question5)

    question6 = Questions.QuestionsClass('What is the hottest planet?',\
                                         'Mars','Pluto','Earth','Venus',4)
    TrivQuestions.append(question6)

    question7 = Questions.QuestionsClass('Which dinosaur had the largest brain compared to body size?',\
                                         'Troodon','Stegosaurus','Ichthyosaurus','Gigantoraptor',1)
    TrivQuestions.append(question7)

    question8 = Questions.QuestionsClass('What is the largest type of penguins?',\
                                         'Chinstrap penguins','Macaroni penguins', \
                                         'Emperor penguins','White-flippered penguins',3)
    TrivQuestions.append(question8)

    question9 = Questions.QuestionsClass("Which children's story character is a monkey?",\
                                         'Winnie the Pooh','Curious George','Horton','Goofy',2)
    TrivQuestions.append(question9)

    question10 = Questions.QuestionsClass('How long is a year on Mars?',\
                                         '550 Earth days', '498 Earth days', '126 Earth days', \
                                          '687 Earth daysa',4)
    TrivQuestions.append(question10)


    return TrivQuestions


    
