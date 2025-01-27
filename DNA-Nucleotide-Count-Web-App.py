# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:33:29 2023

@author: MohammadRasoulSahibz
"""

import pandas as pd
import streamlit as st
import numpy as np
# this library is using for graphs
import altair as alt
# for importing images
from PIL import Image
import requests
from io import BytesIO

# Load image from URL
url = "https://raw.githubusercontent.com/rasoul1234/DNA-Nucleotide-Count-Web-App/main/DNA.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
st.image(image, use_container_width=True)

st.write("""
        # DNA Nucleotide Count Web App
        This app counts the nucleotide composition of query DNA!
        ***
         """)

st.header('Enter DNA Sequence')   
sequence_input = "DNA> Query \nGACATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCCGACATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCCGAC\nATGGGAGGGGGTTTTAAAAGGTTTAAAACCCCC"    
sequence = st.text_area('Sequence input', sequence_input, height=250)  
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write('***')

# 1. Print the input DNA Sequence
st.header('Input (DNA Query)')
sequence

# DNA nucleotide Count
st.header("OUTPUT (DNA Nucleotide Count)")
# 1. Print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

x = DNA_nucleotide_count(sequence)
x_label = list(x)
x_values = list(x.values())
x

# 2. Print text
st.subheader('2. Print text')
st.write('There are '+ str(x['A'])+ ' adenine (A)')
st.write('There are '+ str(x['T'])+ ' thymine (T)')
st.write('There are '+ str(x['G'])+ ' guanine (G)')
st.write('There are '+ str(x['C'])+ ' cytosine (C)')

# 3. Display the Data Frame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0 : 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

# 4. Display Bar Chart Using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
