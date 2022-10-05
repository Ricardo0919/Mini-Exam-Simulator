#Import libraries
import random
import matplotlib.pyplot as plt

#Defining global variables
quest=[]
ans=[]
grades=[]
exam=[]
acum_exams=0
quantity=0
acum=0
num=1
ex=0
final_average_acum=0

#Welcome to the program
print("Welome to this math exam simulator where you'll test your math abilities from middle school level")

def importing_questions():
    #list of questions and answers
    global quest
    global ans
    with open("q&a.txt", encoding="utf-8") as quests:
        questions=quests.read()
    quest=questions.split("\n\n")
    #list of answers
    ans=["a","b","c","c","b","c","a","c","b","a","b","d","d","b","b"]

def questions():
    #Questions Selection
    global quantity
    quantity=int(input("\nHow many questions would you like to answer? \n(maximum posible questions to answer are 15): "))
    
    #Program will select random questions
    #questrand=random.choice(quest)
    
    #Creation of acumulator for grade
    global acum, final_average_acum
    acum=0
    
    #Acumulator for the number of the question
    global num
    #Print random questions
    for times in range(quantity):
        questrand=random.choice(quest)
        print(f"\n{num}. {questrand}")
        answer=str(input("Answer: "))
        answer=answer.lower()
        while answer!="a" and answer!="b" and answer!="c" and answer!="d":
            answer=str(input("Invalid option, try again: "))
            answer=answer.lower()
        if (answer==ans[quest.index(questrand)]):
            print("Correct")
            acum+=1
            final_average_acum+=1
        else:
            print("Incorrect")
            print(f"The correct answer was {ans[quest.index(questrand)]}")
        
        #Functions for not repeating questions
        ans.pop(quest.index(questrand))
        quest.remove(questrand)
        num+=1

def grade():
    global acum,quantity,num,ex,final_average_acum,average
    num=1
    #Calculation of grade
    grade=(acum/quantity)*100
    grades.append(grade)
    
    #Calculation of incorrect questions
    inc=quantity-(acum)
    
    print(f"\nYour final score is {grade:.0f} out of 100")
    print(f"You got {acum} correct question(s) and {inc} incorrect question(s)")
    
    #Calculation of exercises made
    ex+=quantity
    
    #Calculation of final average
    average=(final_average_acum/ex)*100    

def grafica():
    #lists
    global grades,exam
    
    #plt.bar(x,y)
    plt.bar(exam,grades, color=['r', 'g'])

    #Add a title to the plot
    plt.title('Activity grades')

    #Add labels to the axes
    plt.xlabel('Exams')
    plt.ylabel('Grades')

    #Show the plot
    plt.plot(100)
    plt.show()

def menu():
    #Menu
    global avrgacum,ex,average,exam,acum_exams
    print("\nTo continue select an option \n1. Start \n2. Exit")
    op=(int(input("Option: ")))
    while True:
                
        while True:
            if op==1 or op==2:
                break
            else:
                op=int(input("Invalid option, please try again: "))
                
        if op==1:
            importing_questions()
            questions()
            grade()
            acum_exams+=1
            exam.append(f"Exam {acum_exams}")
        
        elif op==2:
            print(f"\nYou made {ex} exercises")
            if ex!=0:
                print(f"Your final average from your exam(s) that you made is {average:.0f} out of 100")
            print("Thanks for using the program, hope it improved your skills, or if you got a low score we recommend you to study and take another quick exam.")
            grafica()
            break
            
        print("\nIf you like to do another exam for a better study select again start if not choose exit \n1. Start \n2. Exit")
        op=(int(input("Option: ")))
          
menu()
            
            





