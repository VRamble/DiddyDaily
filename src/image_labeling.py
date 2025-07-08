from PIL import Image, ImageFont, ImageDraw

def add_text(img_loc,top_text,bottom_text):
    #define some constants for the feel of the added text
    TEXT_PADDING_PX=20
    TEXT_HEIGHT_PX_MAX=120
    BORDER_RATIO=.2
    FONT_LOCATION="res\fonts\impact.ttf"
    
    raw_img=Image.open(img_loc)
    line_width_px_max=raw_img.width-TEXT_PADDING_PX*2
    text_size=min(get_text_size(top_text,line_width_px_max,FONT_LOCATION),get_text_size(bottom_text,line_width_px_max,FONT_LOCATION))
    font=ImageFont.truetype(FONT_LOCATION,text_size)

    #add text to top and bottom of image, get text width that will allow text to fit
    processed_img=ImageDraw.Draw(raw_img)
    
    top_text_loc_x=(raw_img.width-processed_img.textlength(top_text,font=font))/2
    top_text_loc_y=TEXT_PADDING_PX
    bottom_text_loc_x=(raw_img.width-processed_img.textlength(bottom_text,font=font))/2
    bottom_text_loc_y=(raw_img.height-TEXT_PADDING_PX-text_size)

    processed_img.text((top_text_loc_x,top_text_loc_y),top_text,fill=(0,255,0),font=font)
    processed_img.text((bottom_text_loc_x,bottom_text_loc_y),bottom_text,fill=(0,255,0),font=font)

    raw_img.save('edits.png')

def get_text_size(text,line_width_px_max,FONT_LOCATION):
    font_size_px=100
    temp_font=ImageFont.truetype(FONT_LOCATION,font_size_px)

    #create a temp image just to see the line width
    temp_img=Image.new("RGB",(1,1))
    temp_draw=ImageDraw.Draw(temp_img)

    #iterate down until it fits the line
    while temp_draw.textlength(text,font=temp_font)>line_width_px_max:
        font_size_px-=1
        temp_font=ImageFont.truetype(FONT_LOCATION,font_size_px)

    return font_size_px