import discord
from discord.ext import commands , tasks
from discord.utils import get
import asyncio
import time
import random
import datetime
from datetime import date
import numpy as np
import cv2
import pyautogui
import pytesseract
from PIL import Image
import requests as req
from io import BytesIO

client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(""))
    print('Me conecte con el nombre de {0.user}'.format(client))
    screenshots.start()

#? Start Of the non hosted 
@tasks.loop(seconds=20)
async def screenshots():
    # take screenshot using pyautogui

    image = pyautogui.screenshot(region=(1340,180, 450, 790))
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    cv2.imwrite(r"C:\logs\image1.png", image)
    #!!!!!!!!!!!!!!!!!!!
    img = Image.open(r"C:\logs\image1.png") 
    
    
    left = 1340
    top = 180
    right = 1800
    bottom = 1000
    
        

    #!!!!!!!!!!!!!!!!!!!
    # Import required packages

    
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    
    # Read image from which text needs to be extracted
    img = cv2.imread(r"C:\logs\image1.png")
    
    # Preprocessing the image starts
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    # Specify structure shape and kernel size. 
    # Kernel size increases or decreases the area 
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect 
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # Appplying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                    cv2.CHAIN_APPROX_NONE)
    
    # Creating a copy of image
    im2 = img.copy()
    
    # A text file is created and flushed
    file = open(r"C:\logs\recognized.txt", "w+")
    file.write("")
    file.close()
    
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Open the file in append mode
        file = open(r"C:\logs\recognized.txt", "a")
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
    veces=text.count("destroved!")
    veces=veces+text.count("destroved")
    veces=veces+text.count("destroyed")
    veces=veces+text.count("destroyed!")
    veces=veces+text.count("idestioved!")
    teksensor=text.count("triggered")
    teksensor= teksensor + text.count("triagered")
    teksensor= teksensor + text.count("itriagered")
    teksensor= teksensor + text.count("iriagered")

    canaldelogs=client.get_channel(877643542598651924)
    iddd=canaldelogs.last_message_id
    mensaje=await canaldelogs.fetch_message(iddd)
    
    img = Image.open(r"C:\logs\image1.png")
    
    if img == mensaje:
        print("omitio")
    else:
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.id==877643542598651924:
                    ctx=channel
                    f = discord.File(r"C:\logs\image1.png", filename="image1.png")
                    await ctx.send(file=f)
                    if veces>=1:
                        ctx = client.get_channel(877307417107497070)
                        try:
                            await ctx.send("More than a thing destroyed is shown on the #log photo on 773")
                        except:pass
                    if teksensor!=0:
                        ctx = client.get_channel(878010938874277919)
                        try:
                            await ctx.send(f"Tek sensor triggered 773 times: {teksensor}")
                        except:
                            pass
    teksensor=0
    veces=0
client.run('ODc3NjQyODk2NjA4NzQ3NjAw.YR1mpA.R8Z1asVViPC3Msw0-IjIyyCIQ9M')
