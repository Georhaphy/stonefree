# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:40:08 2024

@author: user
"""
import streamlit as st 
from math import exp

st.markdown("<h1 style='text-align: center; color: black ; font-size: 25px ;'>โปรแกรมคำนวณอัตราการเกิดนิ่วในระบบทางเดินปัสสาวะ</h1>", unsafe_allow_html=True)
#st.title(r"$\textsf{\footnotesize โปรแกรมคำนวณอัตราการเกิดนิ่วในระบบทางเดินปัสสาวะ}$")

col1, col2, col3, col4 = st.columns([1,1,1,1]) 
with col1:
     st.write("น้ำหนัก(กิโลกรัม)")
with col2:
    weight = st.number_input('##',value = 60.0 , step = 0.1 ,label_visibility = "collapsed")
with col3:
    st.write("ส่วนสูง(เซนติเมตร)")
with col4:
    height = st.number_input('##', value = 168.0 , step= 0.5 ,label_visibility = "collapsed")

bmi = float(weight)/((float(height)/100)**2)
bmi1 = '%.2f' %(bmi)

gender  = st.radio("เพศ", ["ชาย", "หญิง"])

if gender ==  "ชาย" :
    gender = 1 
else :
    gender = 0

familial  = st.radio("มีคนในครอบครัวเป็นนิ่วหรือไม่", ["มี", "ไม่มี"])

if familial == "มี":
    familial =  1 * 0.962
else:
    familial = 0
    
col5, col6, col7, col8 = st.columns([1,1,1,1]) 

with col5:
    st.write("อาชีพ")

with col6:

    occupation = st.selectbox("##", ("รับราชการ","พนักงานรัฐวิสาหกิจ","พนักงานเอกชน","ค้าขาย/ประกอบกิจการส่วนตัว","แม่บ้าน/พ่อบ้าน","รับจ้าง","กรรมกร","ชาวนา","นักเรียน/นักศึกษา","ว่างงาน"),label_visibility = "collapsed")
    if occupation == 'รับจ้าง' or occupation == 'กรรมกร':
        occupation = 1 * 0.108 
    elif occupation == 'ชาวนา':
        occupation = 1 * 1.597
    else:
        occupation = 0
    
workhour = st.radio("เวลาทำงาน", ["มากกว่า 8 ชั่งโมง", "น้อยกว่าหรือเท่ากับ 8 ชั่วโมง"])

if workhour == 'มากกว่า 8 ชั่งโมง' :
    workhour = 1 * 0.826
else:
    workhour = 0
    
larb = st.radio("กินลาบบ่อยไหม", ("น้อยกว่า 3 ครั้งต่อสัปดาห์", "มากกว่าหรือเท่ากับ 3 ครั้งต่อสัปดาห์")) 
       
if larb == 'น้อยกว่า 3 ครั้งต่อสัปดาห์':
    larb = 0
    
else:
    larb = 1 * 0.693
    

st.markdown(
"""
ให้ท่านประเมินความถี่ของการกินผักดังต่อไปนี้ โดย
- กินประจำ หมายความว่า กินทุกวันอย่างน้อยวันละ 1 มื้อ
- กินบางครั้ง หมายความว่า กินสัปดาห์ละ 1 ครั้งเป็นอย่างน้อย
- กินน้อยมาก หรือไม่กินเลย หมายความว่า กินน้อยกว่าสัปดาห์ละ 1 ครั้ง หรือ ไม่กินอาหารชนิดนี้เลย
"""
)

morning_glory = st.radio("ผักบุ้งไทย", ["กินประจำ", "กินบางครั้ง", "กินน้อยมากหรือไม่กินเลย"])

if morning_glory == 'กินประจำ':
    morning_glory = 1 * 1.032
    
elif morning_glory == 'กินบางครั้ง':
    morning_glory = 1 * 0.214
    
else:
    morning_glory = 0
    
bamboo = st.radio("หน่อไม้", ["กินประจำ", "กินบางครั้ง", "กินน้อยมากหรือไม่กินเลย"])

if bamboo == 'กินประจำ' :
    bamboo = 1*2.581
    
elif bamboo == 'กินบางครั้ง':
    bamboo = 1 * 1.056
    
else:
    bamboo = 0
    

    
degree =  -3.8 + (0.842 * gender) + (0.042 * float(bmi1)) + familial + occupation + workhour + morning_glory + bamboo + larb


result = 100/(1+(1/exp(degree)))

if st.button('ประเมินความเสี่ยง'):
    
    if result < 40 :
        st.write(f"ผู้ป่วยมีความเสี่ยงเป็นนิ่วต่ำ  โอกาสเป็นนิ่วร้อยละ {result:.2f}")
    else : 
        st.write(f"ผู้ป่วยมีความเสี่ยงเป็นนิ่วสูง โอกาสเป็นนิ่วร้อยละ {result:.2f}")
        st.write(":red[คำแนะนำ : คุณมีความเสี่ยงในการเป็นนิ่วในทางเดินปัสสาวะสูง แนะนำให้เข้าการตรวจคัดกรองหานิ่วเพิ่มเติมด้วยการเอ็กซเรย์หรืออัลตราซาวด์ที่โรงพยาบาลใกล้บ้าน ]")