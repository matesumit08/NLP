import re
import random


class Chatbot:
    
    #Potential negative responces
    negative_responses = ('no','nope','nah','not a chance','sorry')
    #Potential exit responces
    exit_commands = ('quit','stop','pause','exit','bye')
    #Potential random questions
    random_questions = ('Why are you here? ','Does you like earth? ','Who is your manager? '
                       'How are you? ', 'What technologies you know? ')
    
    def __init__(self):
        self.alienabble = {'describe_planet_intent':r'.*\s*your planet.*',
                          'answer_why_intent': r'why\sare.*',
                          'about_earth': r'.*\s*earth'}
        
    def greet(self): 
        self.name = input('What is your Name?\n')
        will_help = input(
        f'Hi {self.name}, will you help me to learn about earth?\n')
        if will_help in self.negative_responses:
            print('Ok, have a nice day!\n')
            return
        self.chat()
        
    def make_exit(self,reply):
        if reply in self.exit_commands:
            print('Ok, have a nice day!\n')
            return True
        
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply) :
            reply = input(self.match_reply(reply))
            
    def match_reply(self,reply):
        for key, value in self.alienabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_earth':
                return self.about_earth()
            
            if not found_match:
                return self.no_match_intent()
            
    def describe_planet_intent(self):
        responses = ('I am from Mars\n', 'I am Thor, God of Thunder, from Assgard ')
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ('I come in peace\n', 'I am here to learn about earth\n')
        return random.choice(responses)
    
    def bout_earth(self):
        responses = ('Erth is beutiful\n', 'HUmanity is wonderful\n','India is best\n')
        return random.choice(responses)  
    
    def no_match_intent(self):
        responses = ('Please Explain bit more!\n', 'Why would you say that\n','Tell me more about it\n')
        return random.choice(responses)     
        
    
bot = Chatbot()
bot.greet()
