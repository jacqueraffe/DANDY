import google.generativeai as genai
import os
import credentials
import image_generation

genai.configure(api_key=credentials.login["key"])
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

rubric = """Score each response with the following criteria then print the response with the highest score:
Add one point to the score if the health points of the character are consistent. For example, if the player had 100 health, then got stabbed by a sword, they should lose 80 health points.
Add one point to the score if the amount of money the player holds is consistent. For example, if the player had 100 gold, then spent 50 gold. Their inventory should now have 50 gold.
Add one point to the score if where the player is and goes is possible and logical.
Subtract one point from the score if the player tries to do something that is impossible. For example, if the player tries to lift a building with their bare hands.
Subtract one point if there isn't a lot of descriptive language.
Subtract one point if you did not give 3 choices for the player to follow.
"""

response = model.generate_content(starter_prompt)
print(response.text)

inp = input("input:")
next_prompt = starter_prompt
while next_prompt:
    response1 = model.generate_content(next_prompt)
    response2 = model.generate_content(next_prompt)
    response3 = model.generate_content(next_prompt)
    responses = [response1, response2, response3]
    scores = []
    for response in responses:
        score_string = model.generate_content(
            "respond to me with only an integer score of the following text:"
            + response.text
            + " Grade the text based off the following rubric:"
            + rubric
        ).text
        try:
            score = int(score_string)
        except:
            score = 0
        scores.append(score)
    best_response = max(scores)
    print(best_response)
    image_generation.generate_image(best_response.text)
    inp = input("input:")
    next_prompt = "continue the story with this prompt" + inp
