from datetime import datetime
from termcolor import colored

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Shefali', 'Ms.', 20, 4.7)
friend_one = Spy('Akshit', 'Mr.', 21, 4.9)
friend_two = Spy('Pankhuri', 'Ms.', 21, 6.0)
friend_three = Spy('Karishma', 'Ms.', 22, 8.1)



friend_list = [friend_one, friend_two, friend_three]


