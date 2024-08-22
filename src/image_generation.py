import base64
import vertexai
import os
from vertexai.preview.vision_models import ImageGenerationModel


def generate_image(prompt):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "src/dandy-433321-38650c621410.json"

    generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")
    prompt = "Make a dungeons a dragons inspired scene with this movie script:" + prompt
    response = generation_model.generate_images(
        prompt=prompt,
    )

    image = response.images[0]
    print(type(response))
    image.save("image.jpg", False)


generate_image("in a dungeon fighting a dragon")
