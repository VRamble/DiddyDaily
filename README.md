# **DiddyDaily**
## What is it?

Diddy Daily is a text-based tool that will send daily memes regading Sean "Diddy" Combs to the user.

## Why is it?

This concept is an inside joke with a coworker who recieved daily diddy memes.

## How is it?

This program prompts for a response using the OpenAi API to generate the meme text, in addition to a image prompt. This image prompt is passed into Dall-E to generate the image. Finally the meme text from earlier is drawn on top of the generated image.

This project will use Twilio for SMS functionality.

## Notice
This project uses impact font for captioning the meme, due to licensing of the font download, it is not included in this repository. Download the impact.ttf and place it in res\fonts\ folder