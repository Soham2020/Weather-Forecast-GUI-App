import tkinter
from tkinter import BOTH
root = tkinter.Tk()
root.title('Weathe App')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg="#F9A620")

#define colors and fonts
sky_color = "#9FC2CC"
grass_color = "#20BF55"
input_color = "#548C2F"
output_color = "#1B5299"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#define functions

#define layout
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

root.mainloop()