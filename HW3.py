# Your name: Jake Domagalski
# Your student id: 2465 7437
# Your email: jdomagal@umich.edu
# List who you have worked with on this homework:
#Ambra 

# import the random module for use in this program
import random

# Create the class Magic_8
class Magic_8:

    def __init__(self, possible_answers):
        self.answer_list = possible_answers
        self.question_list = []
        self.answer_history_list = []
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's answer_list (instance variable) to the passed list of possible answers
    # it sets this object's question_list (instance variable) to the an empty list
    # it sets this object's answer_history_list (instance variable) to an empty list 

    def __str__(self):
        return  ", ".join(self.answer_list)
    # create the __str__ method
    # It should return a string with all the possible answers  
    # in answer_list separated by commas
    # For example : "Yes, No, Not clear"

    def shake_ball(self):
        index = random.randint(0, len(self.answer_list) - 1)
        self.answer_history_list.append(index)
        return self.answer_list[index] 
    # create the shake_ball method
    # it randomly picks an index from 0 to the number of items in the answer_list minus one
    # it adds that index to the end of the answer_history_list
    # it returns the answer at the picked index

    def check_question(self, question):
        answer = ""
        if question not in self.question_list:
            self.question_list.append(question)
            answer = question + " - " + self.shake_ball()
            return answer
        else:
            return "I already answered that question!"
    # create the check_question method that takes a question
    # it checks if the question is in the question_list and if so returns 
    #         "I already answered that question!”
    # Otherwise it adds the question to the question_list and
    # returns the answer from shake_ball

    def print_history(self):
        if len(self.answer_history_list) == 0:
            print("None yet")
        else:
            for i in range(0, len(self.answer_history_list)):
                print( '[' + str(self.answer_history_list[i]) + ']' + self.question_list[i] + ' -' + self.answer_list[self.answer_history_list[i]])
                

                

    # create the print_history method
    # prints "[answer index] question - answer" for each of the indices in the answer_history_list
    # from the first to the last with each on a single line.  If there are not items in the 
    # answer_history_list it prints "None yet"
    # it does not return anything!
            
    
    
def main():

    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8(answer_list)

    # get the first question or quit

    # loop while question is not "quit"
    

    question = ""
    question = input("Ask the Magic 8 Ball a yes or no question, or 'quit' when you're finished")
    while question != 'quit':
        answer = bot.check_question(question)
        bot.print_history()
        question = input("Ask the Magic 8 Ball a yes or no question, or 'quit' when you're finished")







def test():
    
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_history()
    print()

    print("Asking the Question: Am I hungry?")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Am I hungry? again")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Should I go for a walk?")
    print(bot2.check_question("Should I go for a walk"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()
    
  #testing change for commits

  


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    #test() - uncomment when you are ready to test your magic 8 ball