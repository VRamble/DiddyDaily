from openai import OpenAI

def get_image_prompt(client):
    '''IMAGE_PROMPT_PROMPT="""
                    You are the backend of a text-based meme service called Diddy Daily. Every day, you generate a new meme featuring Sean “Diddy” Combs or a character inspired by him. These memes should be humorous, clever, slightly edgy, and reflect current events or trends if relevant. If no meaningful event is available, use a timeless concept (like hustle culture, fame, etc.).

                    Your job is to:
                    1. Describe the scene in detail that should be sent to DALL·E for image generation.
                    2. Ensure the image leaves **clear blank space** at the **top and bottom** for overlayed meme text (like traditional Impact-font memes). The top and bottom thirds should not have important details to make room for meme text.
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

    #prompt for the meme text and image desc
    response=client.responses.create(
        model="gpt-4.1",
        input=IMAGE_PROMPT_PROMPT
    )'''

    override_response="""Cartoonish scene of Sean “Diddy” Combs dressed in a flashy gold tracksuit and oversized sunglasses, surrounded by stacks of cash and colorful confetti, confidently walking through a modern office filled with stressed-out workers staring at computer screens. Diddy is carrying a briefcase labeled “MONDAY ENERGY.” Ensure the top third (above Diddy’s head) and bottom third (at his feet) are free of important details, leaving these spaces clear for meme text.|WHEN YOU SHOW UP TO WORK AFTER A HOLIDAY WEEKEND|ACTING LIKE THE CEO OF VACATION"""

    #split the response based on the delimeter
    #TODO implement error checking the output
    split_text=override_response.split('|')
    #split_text=response.output_text.split('|')
    image_prompt=split_text[0].strip()
    top_text=split_text[1].strip()
    bottom_text=split_text[2].strip()

    return image_prompt,top_text,bottom_text
    #return response.output_text

def generate_image(image_prompt,client):
    '''generated_diddy = client.images.generate(
        model='dall-e-3',
        prompt=image_prompt,
        response_format="b64_json",
        n=1,
        size="1024x1024"
    )

    diddy_bytes = base64.b64decode(generated_diddy.data[0].b64_json)

    current_time=int(time.time())

    file_path=f'{current_time}.png'

    with open(file_path,"wb") as f:
            f.write(diddy_bytes)

    return file_path'''

    return '1751931347.png'