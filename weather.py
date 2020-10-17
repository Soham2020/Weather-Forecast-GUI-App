import tkinter
from tkinter import BOTH
root = tkinter.Tk()
root.title('Weathe App')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#define colors and fonts
sky_color = "#9FC2CC"
grass_color = "#20BF55"
input_color = "#548C2F"
output_color = "#01BAEF"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#define functions

#define layout
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)
output_frame = tkinter.Frame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.Frame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)
#output frame layout
city_info_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
weather_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
feels_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_min_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
temp_max_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
humidity_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
photo_label = tkinter.Label(output_frame, bg=output_color, text='Testing')
city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)


root.mainloop()