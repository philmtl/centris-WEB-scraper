import csv

with open ('filename.cv','wb') as file:
   writer=csv.writer(file)
   for row in course_list:
      writer.writerow(row)
      

courses_list=[]

for item in g_data2:
   try:
      name=item.contents[1].find_all("div",{"class":"views-field-title"})[0].text
   except:
       name=''
   try:
      address1=item.contents[1].find_all("div",{"class":"views-field-address"})[0].text
   except:
      address1=''
   try:
      address2=item.contents[1].find_all("div",{"class":"views-field-city-state-zip"})[0].text
   except:
      address2=''

   course=[name,address1,address2]
   courses_list.append(course)
