from tkinter import messagebox as mb
import random
import tkinter as tk

root = tk.Tk()
root.title('игра в кости')
root.iconbitmap("130dice.ico")
root.geometry("1280x720")
root.resizable(width=False, height=False)

def roll_dice():
    global bttn_clicks
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    d = {"\u2680":1, "\u2681":2, "\u2682":3, "\u2683":4, "\u2684":5, "\u2685":6}
    dice1 = random.choice(dice)
    dice2 = random.choice(dice)
    ldice.configure(text=f"{dice1} {dice2}")
    res = d[dice1] + d[dice2]
    label2.configure(text="Очки:  "+str(res))
    bttn_clicks += 1
    label3["text"] = "Кости брошены " + str(bttn_clicks) + " раз(а)"
    if (bttn_clicks == 10 and res != 10):
        btnRoll.configure(state="disabled")
        mb.showerror("Поражение", "Вы проиграли. Попробуйте еще раз.")
    elif (res == 10):
        btnRoll.configure(state="disabled")
        mb.showinfo("Победа", "Вы победили!")

def restart():
    global bttn_clicks
    bttn_clicks = 0
    btnRoll.configure(state="normal")

btnStart = tk.Button(root, text = "Начать игру", font = ("Hattori Hanzo", 20, "italic"), background="red", foreground="black", activebackground="green", activeforeground="lime", height=1, width=15, command=restart)
btnStart.pack()
btnRoll = tk.Button(root, text = "Бросить кость", font = ("PHattori Hanzo", 20, "italic"), background="red", foreground="black", activebackground="green", activeforeground="lime", height=1, width=15, command=roll_dice)
btnRoll.pack()
label1 = tk.Label(root, text = "Чтобы победить, нужно получить сумму точек на костях, равную 10. Всего дается 10 бросков.", font = ("Playfair Display", 20, "italic"), background="green", foreground="lime")
label1.pack(side="bottom")
label2 = tk.Label(root, text = "", font = ("Hattori Hanzo", 20, "bold"), foreground="red")
label2.pack(side="bottom")
label3 = tk.Label(root, text = "", font = ("Hattori Hanzo", 20, "italic"), background="lime", foreground="black", width=20)
label3.pack(side="bottom")
ldice = tk.Label(root, text = "", font = ("Times", 250), foreground="lime")
ldice.pack()

root.mainloop()