# DANDY
D&D-inspired text adventure. Player will be able to go through 3 encounters, gearing up, exploring a dungeon, and beating a dragon. The LLM will generate the narrative and control the decisions of all NPCs (non-playable characters) in the story. User will control the main character, and the progression of the story will be determined by the user’s choices. Tested three leading large language models, and prompt engineered with each. LLMs to test: ChatGPT, Gemini, Llama. Decided to go with Gemini to act as the Dungeon Master. Accompanying visuals that are AI generated. We will test three leading AI image generators: Draw Things (Stable Diffusion), Image Fx (Imagen 3), Dall-e. Decided to go with Google’s Imagen 3. Enforce story structure and game loop via LLM prompt checker and scoring system.

install your own vertexAI service and gemini credentials

python3 -m pip install -U google-generativeai
python3 -m pip install --upgrade google-cloud-aiplatform