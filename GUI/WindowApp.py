from tkinter import *
from tkinter import ttk
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Backend.main import FormulaAlgorithm



#################### GUI ####################################



root = Tk()
root.title('Aplikacja, żeby Harrierek nie musiał dużo szukać')
root.geometry("1400x800")
root.resizable(True,True)

#Labels


Label(root, text="Marcinku, kochamy Cię",font=("Helvetica", 18)).place(x=535, y=25)

Label(root, text="Wybierz rok:",font=("Helvetica", 10)).place(x=20, y=125)
Label(root, text="Wybierz rundę:",font=("Helvetica", 10)).place(x=20, y=175)

Label(root, text="Wyniki wyścigu:",font=("Helvetica", 10)).place(x=20, y=225)
Label(root, text="Tabela konstruktorów danego wyścigu:",font=("Helvetica", 10)).place(x=455, y=225)

Label(root, text="Aktualna tabela kierowców:",font=("Helvetica", 10)).place(x=790, y=225)
Label(root, text="Aktualna tabela zespołów:",font=("Helvetica", 10)).place(x=1100, y=225)

Label(root, text="Ewentualne zmiany kierowców:",font=("Helvetica", 10)).place(x=20, y=505)
Label(root, text="Ewentualne zmiany zespołów:",font=("Helvetica", 10)).place(x=475, y=505)

Label(root, text="Pobierz dane:",font=("Helvetica", 10)).place(x=200, y=125)
Label(root, text="Prześlij dane:",font=("Helvetica", 10)).place(x=200, y=175)


#Year field

year_box = Entry(root, width=6)
year_box.place(x=120, y=125)

#Entry fields

round_box = Entry(root, width=6)
round_box.place(x=120, y=175)


############### Functions ###################


def downloadDataFromBox():

    global year
    global race
    global Result
    global teams_gui

    year = year_box.get()
    race = round_box.get()

    obiekt = FormulaAlgorithm(year,race)

    Result = obiekt.RunAlgorithm()

    teams_gui = Result[0]

############## Tabela 1 #####################


def createTables():

    global my_table
    global my_table_standings
    global driver_name_entry
    global team_name_entry
    global points_entry
    global team_name_entry_main

    downloadDataFromBox()


    my_table = ttk.Treeview(root)


    #Columns

    my_table['columns'] = ['Driver','Team','Points']

    #Formate columns

    my_table.column("#0", stretch=NO,width=0)
    my_table.column("Driver", anchor=CENTER,width=120)
    my_table.column("Team", anchor=CENTER,width=100)
    my_table.column("Points", anchor=CENTER,width=100)

    #Create headings

    my_table.heading("#0", text="",anchor=CENTER)
    my_table.heading("Driver", anchor=CENTER,text="Driver")
    my_table.heading("Team", anchor=CENTER,text="Team")
    my_table.heading("Points", anchor=CENTER,text="Points")

    #Add data


    for x in range(len(Result[3])):

        my_table.insert(parent='', index='end',values=(Result[1][x],Result[2][x],Result[3][x]))

    my_table.place(x=80,y=260)


    ############### Tabela 2 ##########################

    my_table_standings = ttk.Treeview(root)

    #Columns

    my_table_standings['columns'] = ['Team']

    #Formate columns

    my_table_standings.column("#0", stretch=NO,width=0)
    my_table_standings.column("Team", anchor=CENTER,width=100)

    #Create headings

    my_table_standings.heading("#0", text="",anchor=CENTER)
    my_table_standings.heading("Team", anchor=CENTER,text="Team")

    #Add data

    for teams in Result[0]:

        my_table_standings.insert(parent='', index='end',values=teams)

    my_table_standings.place(x=510,y=260)

    ############### Tabela 3 ##########################

    standings_teams = ttk.Treeview(root)

    # Columns

    standings_teams['columns'] = ['Team','Points']

    # Formate columns

    standings_teams.column("#0", stretch=NO, width=0)
    standings_teams.column("Team", anchor=CENTER, width=100)
    standings_teams.column("Points", anchor=CENTER, width=100)

    # Create headings

    standings_teams.heading("#0", text="", anchor=CENTER)
    standings_teams.heading("Team", anchor=CENTER, text="Team")
    standings_teams.heading("Points", anchor=CENTER, text="Points")

    # Add data

    for nr in range(len(Result[4])):
        standings_teams.insert(parent='', index='end', values=(Result[4][nr],Result[5][nr]))

    standings_teams.place(x=1075, y=260)

    ############### Tabela 4 ##########################

    standings_drivers = ttk.Treeview(root)

    # Columns

    standings_drivers['columns'] = ['Driver', 'Points']

    # Formate columns

    standings_drivers.column("#0", stretch=NO, width=0)
    standings_drivers.column("Driver", anchor=CENTER, width=100)
    standings_drivers.column("Points", anchor=CENTER, width=100)

    # Create headings

    standings_drivers.heading("#0", text="", anchor=CENTER)
    standings_drivers.heading("Driver", anchor=CENTER, text="Team")
    standings_drivers.heading("Points", anchor=CENTER, text="Points")

    # Add data

    for nr2 in range(len(Result[6])):
        standings_drivers.insert(parent='', index='end', values=(Result[6][nr2], Result[7][nr2]))

    standings_drivers.place(x=775, y=260)



    ################## Ewentualne zmiany w wynikach ##################

    frame = Frame(root)
    frame.place(x=20,y = 550)

    #labels
    driver_name= Label(frame,text = "Driver")
    driver_name.grid(row=0,column=0 )

    team_name = Label(frame,text="Team")
    team_name.grid(row=0,column=1)

    points = Label(frame,text="Points")
    points.grid(row=0,column=2)

    #Entry boxes
    driver_name_entry= Entry(frame)
    driver_name_entry.grid(row= 1, column=0)

    team_name_entry = Entry(frame)
    team_name_entry.grid(row=1,column=1)

    points_entry = Entry(frame)
    points_entry.grid(row=1,column=2)

    ########## Główne zmiany w zespołach #################

    frame2 = Frame(root)
    frame2.place(x=500, y=550)

    # labels
    team_name_main = Label(frame2, text="Team")
    team_name_main.grid(row=0, column=0)

    team_name_entry_main = Entry(frame2)
    team_name_entry_main.grid(row=1, column=0)


#Upload to excel

def uploadExcel():
    lst = []
    lista2 = []
    iteratorek = 0

    for row_id in my_table_standings.get_children():
        row = my_table_standings.item(row_id, "values")
        lst.append(row)

    start_row = (int(race))*2 + 2

    for x in lst:
        lista2.append(x[0])

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("F1 Obstawiacze 2022").sheet1  # Open the spreadhseet

    for i in range(2,12):
        sheet.update_cell(start_row,i,lista2[iteratorek])
        iteratorek +=1

#Select Record
def select_record():
#clear entry boxes
    driver_name_entry.delete(0,END)
    team_name_entry.delete(0,END)
    points_entry.delete(0,END)

    # grab record
    selected = my_table.focus()
    # grab record values
    values = my_table.item(selected, 'values')
    # temp_label.config(text=selected)

    # output to entry boxes
    driver_name_entry.insert(0, values[0])
    team_name_entry.insert(0, values[1])
    points_entry.insert(0, values[2])

# save Record
def update_record():
    selected = my_table.focus()
    # save new data
    my_table.item(selected, text="", values=(driver_name_entry.get(), team_name_entry.get(), points_entry.get()))

    # clear entry boxes
    driver_name_entry.delete(0, END)
    team_name_entry.delete(0, END)
    points_entry.delete(0, END)

#Select Record Team
def select_record_team():
#clear entry boxes
    team_name_entry_main.delete(0,END)

    # grab record
    selected2 = my_table_standings.focus()
    # grab record values
    values2 = my_table_standings.item(selected2, 'values')
    # temp_label.config(text=selected)

    # output to entry boxes
    team_name_entry_main.insert(0, values2[0])

# save Record Team
def update_record_team():
    selected2 = my_table_standings.focus()
    # save new data
    my_table_standings.item(selected2, text="", values=(team_name_entry_main.get()))
    # clear entry boxes
    team_name_entry_main.delete(0, END)


################ Buttony ####################


#Select button

# Aktualizacja tabeli kierowców

select_button = Button(root,text="Select record", command=select_record)
select_button.place(x=100,y=650)

save_changes_button = Button(root,text="Save changes", command=update_record)
save_changes_button.place(x=225,y=650)

select_button_team = Button(root,text="Select record", command=select_record_team)
select_button_team.place(x=475,y=650)

save_changes_button_team = Button(root,text="Save changes", command=update_record_team)
save_changes_button_team.place(x=575,y=650)



download_button = Button(root,text="Download", command=createTables)
download_button.place(x=300,y=123)

upload_button = Button(root,text="Upload", command=uploadExcel)
upload_button.place(x=300,y=173)




root.mainloop()