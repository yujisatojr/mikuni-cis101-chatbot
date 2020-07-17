from javax.swing import JButton, JFrame, JLabel, ImageIcon, JPanel, JTextField
from java.awt.BorderLayout import NORTH, SOUTH, WEST, EAST
import random

#get name and picture
name = requestString("What's your name?")
file = "C:\Users\YOUR NAME COMES HERE\Desktop\Cat.jpg"

def react(event):
 #pass the String from textfield to chatbot function
 answer = textField.text
 newAnswer = chatbot(answer)

 #hide the old window
 frame.visible = False

 #create a new window
 newFrame = JFrame("hey", size = (400,550))

 #show an answer from robot and show
 message = JLabel(" ")
 message.text = newAnswer
 newFrame.add(message, SOUTH)

 #add other parts to the layout
 newbutton = JButton("push", actionPerformed=react)
 newFrame.add(newbutton, EAST)
 newtextField = JTextField('', 15)
 newFrame.add(textField, NORTH)
 newFrame.add(image, WEST)
 newFrame.visible = True

#create the window
frame = JFrame("ChatCat", size = (400, 550))
#create textfield
textField = JTextField('', 15)
frame.add(textField, NORTH)
#create button
button = JButton("push", actionPerformed=react)
frame.add(button, EAST)
#show picture
image = JLabel(ImageIcon(file))
frame.add(image, WEST)
#show greeting
greeting = JLabel(" ")
greeting.text = "Nice to see you, " + name
frame.add(greeting, SOUTH)
#show the window
frame.visible = True

def chatbot(answer):
  #arrays
  greeting_keywords = ("Hi", "Hello", "hi", "what's up?", "hey", "Hey", "hello")
  greeting_responses = ["Hi", "Hey", " Hello"]
  conversation_keywords = ("How are you doing?", "How are you?", "how are you?", "How's going?")
  conversation_responses = ["I'm fine", "good"]
  introducing_keywords = ("what is your name?", "name?", "what's your name?", "who are you?")
  introducing_responces = ["I am a kitten", "I am just a cute cat"]
  reaction_keywords = ("really?", "what?", "Really?", "nice to meet you")
  reaction_responces = ["yes", "yep"]
  japanese_keywords = ("konnichiwa", "do you speak japanese?", "arigato")
  japanese_responces = ["konichiwa", "hai", "arigato"]

  #if statement
  if answer == "bye":
    return "bye"
  elif answer in greeting_keywords:
    return random.choice(greeting_responses)
  elif answer == "yes":
    return"okay"
  elif answer in conversation_keywords:
    return random.choice(conversation_responses)
  elif answer in introducing_keywords:
    return random.choice(introducing_responces)
  elif answer in reaction_keywords:
    return random.choice(reaction_responces)
  elif answer in japanese_keywords:
    return random.choice(japanese_responces)
  else:
    return "nani?"