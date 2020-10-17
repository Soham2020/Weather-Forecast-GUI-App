import tkinter, requests
from tkinter import BOTH, IntVar
root = tkinter.Tk()
root.title('Weathe App')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#define colors and fonts
sky_color = "#9FC2CC"
grass_color = "#20BF55"
input_color = "#50FFB1"
output_color = "#01BAEF"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#define functions
def search():
    global response

    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "a21df2a0766cf894f487aedc536bc0e4"
    if search_method.get() == 1:
        querystring = {"q" : city_entry.get(), "appid":api_key}
    elif search_method.get() == 2:
        querystring = {"q" : city_entry.get(), "appid":api_key}

    response = requests.request("GET", url, params=querystring)
    response = response.json()
        
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

#input frame layout
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text="Submit", bg=input_color, font=large_font, command=search)
search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text="Submit Search City", variable=search_method, value=1, bg=input_color, font=small_font)
search_zip = tkinter.Radiobutton(input_frame, text="Submit by Zip Code", variable=search_method, value=2, bg=input_color, font=small_font)
city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, pady=2)

root.mainloop()