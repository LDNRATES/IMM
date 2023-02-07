import streamlit as st
import datetime as dt
import calendar as cl
from ipywidgets import interact

def imm(MONTH,YEAR):
    if MONTH == 'H':
        m = 3
    elif MONTH == 'M':
        m = 6
    elif MONTH == 'U':
        m = 9
    elif MONTH == 'Z':
        m = 12
    else:
        return 'Not an IMM Month'
    y = 2000 + int(YEAR)
    third = dt.date(y,m,15)
    w = third.weekday()
    if w != 2:
        third = third.replace(day = (15 + (2 - w) % 7))
        
    return third.strftime('%A, %d %B %Y')
    
m = st.selectbox('Month',['H','M','U','Z'])
y = st.selectbox('Year',[i for i in range(22,100)])    
st.write(imm(m,y))

