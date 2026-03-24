#setup code
from selenium import webdriver   
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import pandas as pd 
import time

#start browser 
driver_path = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

#Open website
driver.get("https://www.timeshighereducation.com/world-university-rankings/latest/world-ranking")  

#execute
time.sleep(5)

#required findings:
table = driver.find_element(By.CLASS_NAME, "css-iowbcb")
rows = table.find_elements(By.CSS_SELECTOR, "tr")


# table_body:
print("All rows:::::")
all_data = []

for row in rows[1:]:
   Contents = row.find_elements(By.TAG_NAME, "td")

   row_data = []

#Get text:
   for content in Contents:
       text = content.text.strip().replace("\n", " ,") 
       if text:
          row_data.append(text)

#Get links:
       try:
           first_link = content.find_element(By.TAG_NAME, "a").get_attribute("href")

           if first_link:
              row_data.append(first_link)
       except:
            pass
     
#append inside row_data:

   if len(row_data) == 0 or row_data == ['']:
        continue
   all_data.append(row_data)

#print all rows:
for row in all_data:
 print(row)

print("1st row:::::")

first_row = all_data[0]  # first row

print("First row elements with index:")
for idx, value in enumerate(first_row):
    print(f"Index {idx}: {value}")


#table header:
print("1st row of all_rows_dict:::::")

column_name = ["World Rank", "University Name", "Country",  "University Website", "Overall Score", "Teaching Quality", "Research Environment", "Reasearch Quality", "Industy", "International Outlook"]

all_rows_dict =[]

for row in all_data:
    row_dict = {}

    row_dict["World Rank"] = row[0]
    row_dict["University Name"] = row[1].split(',')[0 ]
    row_dict["Country"] = row[1].split(',')[1]
    row_dict["University Website"] = row[2]
    row_dict["Overall Score"] = row[3]
    row_dict["Teaching Quality"] = row[4]
    row_dict["Research Environment"] = row[5]
    row_dict["Reasearch Quality"] = row[6]
    row_dict["Industy"] = row[7]
    row_dict["International Outlook"] = row[8]

    all_rows_dict.append(row_dict)

print(all_rows_dict[0])


print("convert to dataframe::::::")

df = pd.DataFrame(all_rows_dict)  
print(df.head())


#convert to dictionary:
print("a) convert to column-oriented dictionary::::::")

col_dict = df.to_dict(orient="list")
print(col_dict)

print("b) convert to Row-oriented dictionary::::::")
row_dict = df.to_dict(orient="records")
print(row_dict[:2])

#Save the DataFrame to CSV
df.to_csv("times_higher_education_updated.csv", index=False)


#Save the DataFrame to JSON
df.to_json("times_higher_education_updated.json", orient="records", indent=4)


driver.quit()




#Split 2nd col:

#for row in rows [1:]:
  #elements = row.find_elements(By.TAG_NAME, "td") 

  #if len(elements) < 2:
      #first_part = ""
       #second_part = ""   

  #else:        
       #parts = elements[1].text.split("\n")

       #first_part = parts[0] if len(parts) > 0 else ""
       #second_part = parts[1] if len(parts) > 1 else ""

  #print(f"university: {first_part}  country: {second_part}")