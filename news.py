import requests
import tkinter as tk

def getNews():
    api = '5bbbcc12181440328e164ea4b768b9b9'
    url = 'https://newsapi.org/v2/everything?q=Apple&from=2022-04-04&sortBy=popularity&apiKey='+api
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(20):
        my_news = my_news + my_articles[i] + "\n"

    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas,font = 18, justify = "left")
label.pack(pady = 20)

getNews()
canvas.mainloop()

