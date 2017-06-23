from spydetails import spy, Spy, ChatMessage, friend_list
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#a list of special words which when typed would display a message.
special_messages = ['SAVE ME', 'SOS', 'HELP ME']

# a list has been created with existing status messages.
list_of_status_messages = ['Available', 'On a vacation', 'Coffee is my love.', 'Binge-watching Suits']

#colored is being used to color the text.
print colored("Hello! Let\'s get started", 'magenta')

#Here, question and choice are variables.
question = "Do you want to continue as %s%s (Y/N)? \n"% (spy.salutation, spy.name)
#raw_input would ask for an input from the user.
choice = raw_input(question)

#add_status is a function which will add status.
def add_status():

    #the updated)status_message is currently set to None by default.
    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)

    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (Y/N)? \n")

    #the .upper() method will convert the input to upper case.
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? \n")


        if len(new_status_message) > 0:
            list_of_status_messages.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in list_of_status_messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("Choose from the above messages \n"))


        if len(list_of_status_messages) >= message_selection:
            updated_status_message = list_of_status_messages[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.\n'

    if updated_status_message:
        print 'Your updated status message is: %s \n' % (updated_status_message)

    else:
        print '\nYou current don\'t have a status update'

    return updated_status_message


#add_friend is a function to add friend.
def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("\nPlease add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age?"))

    new_friend.rating =float( raw_input("Spy rating?"))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friend_list.append(new_friend)
        print 'Friend Added!'

    else:
        print '\nSorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friend_list)

#select_a_friend is a function to select from the available friends.
def select_a_friend():
    item_number = 0

    for friend in friend_list:

        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#send_message is a function that will send a message to the friend you have selected.
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("\nWhat is the name of the image?")
    output_path = "landscape.jpg"
    text = raw_input("\nWhat do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friend_list[friend_choice].chats.append(new_chat)

    print "\nYour secret message image is ready!"


#read_message is a function that would read the message from a friend.
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    try:
        secret_text = Steganography.decode(output_path)
    except:
        print "your message is not valid"
        return

    new_chat = ChatMessage(secret_text, False)

    friend_list[sender].chats.append(new_chat)

    print "\nYour secret message has been saved!\n" + secret_text

    if secret_text.upper() in special_messages:
        print "We are on our way!\n"

    if (len(secret_text.split(" "))) > 100:
        print "the spy" + spy.name + "was talking too much hence was deleted"
    del friend_list[sender]


#read_chat_history is a function that would display the chat history between the spy and his friend.
def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friend_list[read_for].chats:

        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"), 'blue'), 'You said:', colored(chat.message, 'grey'))

        else:
            print '[%s] %s said: %s' % (colored(chat.time.strftime("%d %B %Y"), 'blue'), colored(friend_list[read_for].name, 'red'), colored(chat.message, 'grey'))

#This function will start the chat.
def start_chat(spy):

    spy.name = "%s%s"% (spy.salutation, spy.name)


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome %s aged %d with a rating of %.2f. Proud to have you onboard."\
        % ( spy.name, spy.age, spy.rating )

        #The menu will be shown to the user.
        show_menu = True

        while show_menu:
            menu_choices = "\n What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice == 3:
                    send_message()

                elif menu_choice == 4:
                    read_message()

                elif menu_choice == 5:
                    read_chat_history()

                else:
                    #The menu will disappear.
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy\n'

if choice == "Y":
    start_chat(spy)

else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:

        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = int(raw_input("What is your age?"))


        spy.rating = float(raw_input("What is your spy rating?"))

        if spy.rating > 4.5:
            print "You have a great ace.\n"
        elif spy.rating >= 3.5 and spy.rating <= 4.5 :
            print "You can do better.\n"
        else :
            print "We can use someone from the office.\n"


        start_chat(spy)

    else:
        print 'Please add a valid spy name'


