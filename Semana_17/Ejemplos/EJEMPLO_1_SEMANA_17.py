import PySimpleGUI as sg

# Get the screen width and height in base of my own screen res

screen_width, screen_height = sg.Window.get_screen_size()

#Elements for the window

layout = [

    [sg.Text("What do you want to do?")],
    [sg.Button("storage"), sg.Button("categories"), sg.Button("transactions")],

]

#Create window

window = sg.Window("First program", layout, size=(screen_width, screen_height), resizable=True)  # Open window. Also place window size, it can be resizable
#Open window. Also place window size, it can be resizable

#Event loop for events and values

while True:

    event, values = window.read() #For read elements

    #For close the window (user must do it by clicking the "x")
    if event == sg.WIN_CLOSED:
        break

    if event == "storage":
        pass

    if event == "transactions":
        pass

    if event == "categories":
        pass

window.close() #For close window