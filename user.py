from calculator.calculator import calculate
import re

ASK_FOR_FIRST_NUMBER = "What is the first number ?"
ASK_FOR_PROCESS = "What is the process ?"
ASK_FOR_SECOND_NUMBER = "What is the second number ?"


def isdigit(text):
    return re.match("^-?\d+(\.\d+)?$", text) is not None

class User:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.first_number = None
        self.second_number = None
        self.process = None

    def get_response(self, text):
        if self.first_number is None:
            if text.isdigit():
                self.first_number = int(text)
                return ASK_FOR_PROCESS
            else:
                return ASK_FOR_FIRST_NUMBER


        elif self.process is None:
            self.process = str(text)
            return ASK_FOR_SECOND_NUMBER
    


        elif self.second_number is None:
            text
            if text.isdigit():
                self.second_number = int(text)
                answer = self.calculate_answer()
                self.reset()
                return answer
            else:
                return ASK_FOR_SECOND_NUMBER
                
    def calculate_answer(self):
        return calculate(self.first_number, self.process, self.second_number)
