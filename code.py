
from Question import Question
question_prompts = 
[
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are mangoes?\n(a) Red\n(b) Yellow\n(c) Black\n",
    "What color are strawberries?\n(a) yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
    Question(question_prompts[3],"a")
]
#This is the function that will run questions and check the answers, the 0 will be incremented after every question
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
#to print number along side string you have to use str the type the number ie score len will show the total number of questions
    print("You got " + str(score) + "/"+ str (len(questions)) + "Correct")
run_test(questions)

