from os import system
from time import sleep
from turtle import clear, clearscreen, delay


hundredQuestions = ["start","What is the supreme law of the land?","What does the Constitution do?",
                    "The idea of self-government is in the first three words of the Constitution. What are these words?",
                    "What is an amendment?","What do we call the first ten amendments to the Constitution?"]
hundredAnswers = ["begin","the Constitution","sets up the government","We the People","a change","the Bill of Rights"]

def exam():
    count = 1

    for x in range(6):
        for y in range(6):
                #print(count)
                print(count, ".", hundredQuestions[count])
                answer = input("answer: ")
                if answer == hundredAnswers[count]:
                    print("correct")
                    sleep(1)
                    system('cls')
                    count = count+1
                    if count == 6:
                        print("Good job you passed the exam!!")
                        break
                else:
                    print("wrong, try again!")
                    count = count

print("start exam?")
begin = input("Yes or No: ")
if begin == "Yes":
    exam()
else:
    print("Goodbye!")
