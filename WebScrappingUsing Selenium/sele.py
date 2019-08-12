from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv

class Student:
    def __init__(self,reg,naam,cgpa):
        self.naam=naam
        self.reg=reg
        self.cgpa=cgpa

browser=webdriver.Chrome("/home/abhinay9955/Downloads/chromedriver_linux64/chromedriver")

browser.get("http://14.139.205.172/web_new/Default.aspx")


show=browser.find_element_by_id('btnimgShow')

ans=[]

cheat=[1,10,44]

abs=[3,40,88,90,96]
for i in range(1,101):
    if i in abs:
        continue
    if i in cheat:
        continue
    roll = browser.find_element_by_id('txtRegno')
    show = browser.find_element_by_id('btnimgShow')
    if i>0 and i<10:
        reg='2017UGCS00'+ str(i)
    elif i>9 and i<100:
        reg='2017UGCS0'+str(i)
    else:
        reg='2017UGCS'+str(i)

    roll.send_keys(reg)
    show.click()
    name = browser.find_element_by_id('lblSName')
    naam=name.text
    sem = Select(browser.find_element_by_id('ddlSemester'))
    sem.select_by_index(4)
    result = browser.find_element_by_id('btnimgShowResult')
    result.click()
    cgpa=browser.find_element_by_id('lblCPI').text
    ans.append(Student(reg,naam,cgpa))
    roll = browser.find_element_by_id('txtRegno')
    roll.clear()


with open('student.csv','w') as writefile:
    writer=csv.writer(writefile)
    for obj in ans:
        if obj.cgpa<6.0:
            writer.writerow([obj.reg,obj.naam,obj.cgpa])
writefile.close()



