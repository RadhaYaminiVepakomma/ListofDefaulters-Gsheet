import tkinter as tk
from tkinter import *
import pandas as pd
import os
import pprint
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

os.chdir('C:\\Users\\pc\\Desktop/Sample')

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Defaulters-GeneTimeLog-2a0444962554.json', scope)

client = gspread.authorize(creds)
sheet = client.open('Time Log Gene').sheet1

pp = pprint.PrettyPrinter()
telemedicine = sheet.get_all_records()

df = pd.DataFrame(telemedicine,columns=['Name','TechM ID','Login Time','Logout Time','Deliverables worked','RM Name'])

# --- functions ---

def on_click(*args):
    #global text
    #,bg = 'peach puff'
    
    text=tk.Text(root,height = 10,width = 25,font=('Calibri 15 bold'),fg='HotPink4')
    #text.config(state=NORMAL)
    #text.tag_configure("center", justify='center')
    #text.insert("1.0", "text")
    #text.tag_add("center", "1.0", "end")
    
    text.delete("1.0","end")
    text.delete("0.0", "end")

        
    val = selected.get()
    a=list()
        
               
    if val == 'All':
        #text.delete('1.0', '2.0')
        df2=df[(df['Login Time']=='')| (df['Logout Time']=='')| (df['Deliverables worked']=='')]
        a=df2['Name'].tolist()
        
        for x in a:
            
            text.tag_configure("center", justify='center')
            text.insert(END, x + '\n')
            text.tag_add("center", "1.0", "end")
         
        text.grid(row=31, column=2, padx=15, pady=15)
        #print(a)
    else:
        #text.delete('1.0', '2.0')
        df2 = df[ df['RM Name'] == str(val) ]
        df3=df2[(df2['Login Time']=='')| (df2['Logout Time']=='')| (df2['Deliverables worked']=='')]
        a=df3['Name'].tolist()
        
        for x in a:
            
            text.tag_configure("center", justify='center')
            text.insert(END, x + '\n')
            text.tag_add("center", "1.0", "end")
            
          
        text.grid(row=31, column=2, padx=15, pady=15) 
        #print(a)
        
 

# --- main ---


root = tk.Tk()
root.geometry('600x450+100+200')  
root.title('Gene Defaulters')  

values = ['All']+list(df['RM Name'].unique())
selected = tk.StringVar()
selected.set('All')

label = tk.Label(root, text="Manager Name: ", font=('Times 25 bold'), fg='blue violet')
label.grid(row=1, column=1, padx=15, pady=15) 

options = tk.OptionMenu(root, selected, *values)
options.config(height = 3,width = 15,bg='light salmon', fg='white')
#selected.trace("w", on_click)
options.grid(row=1, column=2, padx=15, pady=15) 

button = tk.Button(root, text='OK',bg='light slate gray',fg='white' ,height = 2,width = 10,command=on_click) 
          
button.grid(row=16, column=2, padx=15, pady=15)

label = tk.Label(root, text="Defaulters are:",font=('Times 25 bold'), fg='violet red')
label.grid(row=31, column=1, padx=15, pady=15) 


root.mainloop()  
