import base64
import time
from openai import OpenAI
from dotenv import load_dotenv

#load in api key to envi vars
load_dotenv()

def get_image_prompt(recurrsion_counter):
    '''
    client=OpenAI()

    image_prompt_prompt="""
                    You are the backend of a text-based meme service called Diddy Daily. Every day, you generate a new meme featuring Sean “Diddy” Combs or a character inspired by him. These memes should be humorous, clever, slightly edgy, and reflect current events or trends if relevant. If no meaningful event is available, use a timeless concept (like hustle culture, fame, etc.).

                    Your job is to:
                    1. Describe the scene in detail that should be sent to DALL·E for image generation.
                    2. Ensure the image leaves **clear blank space** at the **top and bottom** for overlayed meme text (like traditional Impact-font memes).
                    3. **Do NOT include any text in the image prompt itself** — all meme text will be added later using a separate tool.
                    4. Return the meme text in a clearly structured way using these tags:
                       - `TOP_TEXT:` (for the text to appear at the top of the image)
                       - `BOTTOM_TEXT:` (for the text to appear at the bottom of the image)

                    The image style should be cartoonish or photorealistic — you choose what fits best. The prompt should be vivid, concrete, and easy for DALL·E to render.

                    Return only the following:

                    1. image prompt for DALL-E followed by a `|` 
                    2. the top text of the meme in all caps, followed by a `|`
                    3. the bottom text of the meme in all caps
                    
                    Today’s date is: 6-30-2025
                """

    response=client.responses.create(
        model="gpt-4.1",
        input=image_prompt_prompt
    )
    '''

    override_response="""Sean “Diddy” Combs dressed in an extravagant bathrobe and sunglasses, lounging in a golden throne-shaped pool float in a luxurious rooftop pool, holding a smartphone showing multiple trending social media apps, with a city skyline and summer sunset in the background. Leave clear blank spaces at the top and bottom of the scene for meme text. | WHEN YOUR WEEKEND PLANS TURN INTO A CEO MEETING | STILL COLLECTING BAGS, JUST WITH MORE SPLASH"""

    split_text=override_response.split('|')
    image_prompt=split_text[0].strip()
    top_text=split_text[1].strip()
    bottom_text=split_text[2].strip()

    return image_prompt,top_text,bottom_text
    #return response.output_text

if __name__ == '__main__':
    image_prompt,top_text,bottom_text=get_image_prompt(1)
    print(image_prompt)
    print(top_text)
    print(bottom_text)

'''
generated_diddy = client.images.generate(
    model='dall-e-3',
    prompt=response.output_text,
    response_format="b64_json",
    n=1,
    size="1024x1024"
)

diddy_bytes = base64.b64decode(generated_diddy.data[0].b64_json)

current_time=int(time.time())

with open(f'../{current_time}.png',"wb") as f:
        f.write(diddy_bytes)
'''