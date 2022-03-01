# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:18:37 2022

@author: qli003
"""
from bokeh.layouts import row,column
from bokeh.models import Div, TextInput,Button
from bokeh.io import output_file, show
output_file("my_GUI.html")

# set up textarea (div)
top = Div(
    text="""
          <h1 style="width:680px; height:40px;text-align:center;border-style:solid">Calculate Backward Curve</h3>
          """,
    width = 680,
    height = 60,
)
subtitle1 = Div(
    text="""
          <p>Input</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,15],
)

# set up textarea (div)
channel_length_textarea = Div(
    text="""
          <p>L (Channel Length):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
channel_length_text_input = TextInput(
    width = 100,
    height = 30,
)
L = row(channel_length_textarea,channel_length_text_input)

# set up textarea (div)
channel_width_textarea = Div(
    text="""
          <p>b (Channel Width):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
channel_width_text_input = TextInput(
    width = 100,
    height = 30
)
b = row(channel_width_textarea,channel_width_text_input)

# set up textarea (div)
Q_textarea = Div(
    text="""
          <p>Q (Discharge):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
Q_text_input = TextInput(
    width = 100,
    height = 30
)
Q = row(Q_textarea,Q_text_input)

# set up textarea (div)
C_textarea = Div(
    text="""
          <p>C (Chezy Coefficient):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
C_text_input = TextInput(
    width = 100,
    height = 30
)
C = row(C_textarea,C_text_input)

# set up textarea (div)
h0_textarea = Div(
    text="""
          <p>Water Depth at downstream:</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
h0_text_input = TextInput(
    width = 100,
    height = 30
)
h0 = row(h0_textarea,h0_text_input)

# set up textarea (div)
S0_textarea = Div(
    text="""
          <p>S0 (Slope):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
S0_text_input = TextInput(
    width = 100,
    height = 30
)
S0 = row(S0_textarea,S0_text_input)

# set up textarea (div)
dx_textarea = Div(
    text="""
          <p>dx (Distance Step):</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,30],
)
dx_text_input = TextInput(
    width = 100,
    height = 30
)
dx = row(dx_textarea,dx_text_input)

input = column(subtitle1,L,b,Q,C,h0,S0,dx)

graph= Div(
    text="""
          <img src="BWC.png" style="align:center" left = 50px>
          """,
    width = 400,
    height = 300,
    margin = [0,0,0,30],
)
subtitle2 = Div(
    text="""
          <p>Output</p>
          """,
    width=150,
    height=30,
    margin = [0,0,0,15],
)
ouput = column(subtitle2,graph)
main = row(input,ouput)

button1 = Button(label="Calculate",
    width = 50,
    height = 30,
    margin=[0,0,0,30]
)
button2 = Button(label="Display Graph",
    width = 100,
    height = 30,
    margin=[0,0,0,53]
)
button3 = Button(label="Exit",
    width = 50,
    height = 30,
    margin=[0,0,0,30]
)

buttons = row(button1,button2,button3,width = 650,height = 40,margin=[0,0,0,160])

# show result
show(column(top,main,buttons))