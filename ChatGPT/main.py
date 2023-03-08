import tkinter

import openai
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import json
import os

MY_API_KEY = ""
# openai.organization = "Personal"


def ChatGPT():
  msg= website_entry.get("1.0",'end-1c')
  openai.api_key = API_KEY_entry.get()

  openai.Model.list()
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"{msg}"}]
  )
  answer = completion["choices"][0]["message"]["content"]
  print(completion)
  print(answer)
  answer_entry.delete('1.0', END)
  answer_entry.insert(INSERT,answer)


def whisper():
  try:
      with open("/path/to/file/openai.mp3", "rb") as file:
        transcription = openai.Audio.transcribe("whisper-1", file)
        print(transcription)

  except FileNotFoundError:
    print("No such file")

windows = Tk()
windows.title("chatGPT UI")
windows.geometry("800x800")
windows.config(padx=50,pady=50)

website_label = Label(text="ASK")
website_label.grid(column=0,row=2, pady=5)

answer_label = Label(text="AI ANSWER")
answer_label.grid(column=0, row=3)

answer_entry = Text(width=60, height =25)
answer_entry.grid(column=1, row=3)
answer_entry.focus()


API_KEY_label = Label(text="ENTER YOUR API KEY")
API_KEY_label.grid(column=0,row=0)

API_KEY_entry = Entry(width=80)
API_KEY_entry.grid(column=1, row=0)
API_KEY_entry.insert(0, MY_API_KEY)
API_KEY_entry.focus()


website_entry = Text(width=60, height =10)
website_entry.grid(column=1, row=2,pady=10)
website_entry.focus()

search_button = Button(text="Chat",width=15,command=ChatGPT)
search_button.grid(column=2,row=2,columnspan=2, padx=10)


windows.mainloop()



