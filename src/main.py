import base64
import time
from openai import OpenAI
from openai_api import get_image_prompt,generate_image
from dotenv import load_dotenv
from image_labeling import add_text

#load in api key to envi vars
load_dotenv()

if __name__ == '__main__':
    
    #start the openai api client
    client=OpenAI()

    #generate dall-e prompt + the meme text
    img_prompt,top_text,bottom_text=get_image_prompt(client)
    print(img_prompt)
    print(top_text)
    print(bottom_text)

    #make image from previously generated prompt
    raw_img_loc=generate_image(img_prompt,client)
    print(raw_img_loc)

    #add the text to the image
    processed_image_loc=add_text(raw_img_loc,top_text,bottom_text)