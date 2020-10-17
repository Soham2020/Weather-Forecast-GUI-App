import tkinter

root = tkinter.Tk()
root.title('Weathe App')
root.iconbitmap('weather.ico')
root.geometry('300x300')
root.resizable(0,0)
root.config(bg="#F9A620")

#define colors and fonts
input_color = "#548C2F"
output_color = "#1B5299"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

root.mainloop()