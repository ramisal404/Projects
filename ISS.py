#!/usr/local/bin/python3

import json
import turtle
import urllib.request
from pathlib import Path
import time
import tkinter
import os

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)

url1 = "http://api.open-notify.org/iss-now.json"
response1 = urllib.request.urlopen(url1)
result1 = json.loads(response1.read())

result = json.loads(response.read())
print("People in space:", result["number"])

people = result["people"]
for p in people:
    print(p["name"] + " in " + p["craft"])

location = result1["iss_position"]
lat = float(location["latitude"])
lon = float(location["longitude"])
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("/Users/ramisalman/Documents/GitHub/Projects/images/map.gif")

screen.register_shape("/Users/ramisalman/Documents/GitHub/Projects/images/iss.gif")
iss = turtle.Turtle()
iss.shape("/Users/ramisalman/Documents/GitHub/Projects/images/iss.gif")
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)
tkinter.mainloop()
