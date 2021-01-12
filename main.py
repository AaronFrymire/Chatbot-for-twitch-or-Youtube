import random



def generate_response(user_input):
  responses = [
    "The weather is partly cloudy all day!",
    "Alarm set for 6:00 am",
    "There are 50 states in the United states",
    "Thursday is going to be the coldest day of the week "
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()