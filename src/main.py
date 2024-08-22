import google.generativeai as genai
import os
import credentials

genai.configure(api_key= credentials.login["key"])

model = genai.GenerativeModel('gemini-1.5-flash')

starter_prompt = """ You are the dungeon master for a fantasy game like dungeons and dragons.
You are in a conversation with a party of players. 
Each turn, briefly describe the situation, then ask the party what actions they want to do.
Read their input, and then tell the what happens as a result of their actions. 
Keep track of their health, their inventory, and their gold.
The party consists of:
a human wizard named Fred. Fred has 1 apple. Fred has a magic wand.
An orc fighter named Joe. Joe has no food. Joe has a wooden sword.
The party has 100 pieces of gold.
The party is preparing to go to a dungeon.
The party is in the marketplace of the town of Figby Falls.
"""

response = model.generate_content(starter_prompt)
print(response.text)

inp = input("What do you want to do next?")
next_prompt = starter_prompt
while next_prompt:
    response = model.generate_content(next_prompt)
    print(response.text)
    inp = input("What do you want to do next?")
    next_prompt = "continue the story with this prompt" + inp
