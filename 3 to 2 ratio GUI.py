# py simp GUI for 3:2 ratio solution given total Vol

import PySimpleGUI as sg


def valid_volume(volume_input):
    if (volume_input) != float:
        return True
    sg.popup_error("The total volume of solution to be created\n"
                   "must be a floating point number.\n")
    return False

# create the calculation explaination window
def calc_window():
    layout = [[sg.Text("\n"
        "Total Solution Volume = (Ketamine Vol) + (Dexdomitor Volume)\n"
        "\n"
        "Ketamine Volume   = (Total Volume) * (0.6)\n"
        "\n"
        "Dexdomitor Volume = (Total Volume) * (0.4)\n"
        "\n", 
        key="calc_win")]]
    window = sg.Window("Calculation Explaination", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

# create main window display layout
sg.theme("Darkteal10")

layout = [
    [sg.Text("Enter the total volume of Ketamine/Dexdomitor to be created in mL:")],
    [sg.InputText(key="-TV-", size=(10,1))],

    [sg.Button("Press to calculate required \n"
    "Ketamine and Dexdomitor volumes", size=(30,2))],

    [sg.Text("The volume (mL) of Ketamine in the final solution is:")],
    [sg.Input(key="-KTV-", size=(10, 1))],

    [sg.Text("The volume (mL) of Dexdomitor in the final solution is:")],
    [sg.Input(key="-DTV-", size=(10,1))],

    [sg.Button("Press to view equations for the calculations used"), sg.Push(), sg.Exit()] 
]

# create the main window
window = sg.Window("Welcome to eBot's 3:2 ratio calculator!", layout)
   
# create an event loop
while True:
    event, values = window.read()

    # end program if user closes window
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # convert inputs logic
    if event == "Press to calculate required \n""Ketamine and Dexdomitor volumes":

        volume_input = ["-TV-"]

        if (valid_volume(values["-TV-"])):

            try:
                window["-KTV-"].update((round(float(values["-TV-"])*(float(0.6)),2)))  
                window["-DTV-"].update((round(float(values["-TV-"])*(float(0.4)),2)))

            except ValueError:
                sg.popup_error("Entry field is empty or \n"
                "an integer/floating point number has not been submitted.", title="Value Error")

    # display equations used for conversions    
    if event == "Press to view equations for the calculations used":
        calc_window()
    
window.close()