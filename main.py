import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime

def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_detail():
    url = "https://worldometers.info/coronavirus"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""


    for tag in info_div:
        if (tag.find('a') != None):
            break
        if(tag.find('h1')!=None):
            text = tag.find("h1").text
        if(tag.find('span')!=None):
            count = tag.find("span").text
        all_detail = all_detail + text + " " + count + "\n"

    return all_detail

def get_country_data():
    name=textfield.get()
    url = "https://worldometers.info/coronavirus/country/"+name+'/'
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""

    for tag in info_div:
        if (tag.find('a') != None):
            break

        if (tag.find('h1') != None):
            text = tag.find("h1").text
        if (tag.find('span') != None):
            count = tag.find("span").text
        all_detail = all_detail + text + " " + count + "\n"

    mainlabel['text']=all_detail


def reload():
    new_data = get_covid_detail()
    mainlabel['text']=new_data



get_covid_detail()

root = tk.Tk()
root.geometry("900x700")
root.title("IVAN THE COVID TRACKER")
f = ("poppins", 25, "bold")

banner = tk.PhotoImage(file="ivan.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

mainlabel = tk.Label(root, text = get_covid_detail(), font=f)
mainlabel.pack()

textfield=tk.Entry(root,width=50)
textfield.pack()

gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

gbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
gbtn.pack()

root.mainloop()

