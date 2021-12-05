#Importing some files
import PySimpleGUI as sg
import maingui as main
import settings as cfg
#---------------------------

#Theme stuff
sg.theme_background_color("#403f3e")
sg.theme_button_color("#303030")
sg.theme_text_color("#ffffff")
sg.theme_element_background_color("#403f3e")
sg.theme_text_element_background_color("#303030")
#---------------------------------------------------------------------------

# All the stuff inside the window.
layout = [  #[sg.Image("smol_logo.png")], #Another beta Unused element, but this time a logo 0_0 (btw it's the logo on Github just a bit smaller)
            #[sg.Text('Settings')], #Beta unused text
            [sg.Text('Title:'), sg.InputText()], #values[0]
            [sg.Text('Description:'), sg.InputText()], #values[1]
            [sg.Text('Buttons')],
            #[sg.Checkbox('Enabled', size=(10,1), default=True),  sg.Checkbox('Disabled', default=False)], #values[2] values[3] #Old method, kinda weird but already idiot-proof
            [sg.Radio('Enabled', "RADIO1", default=True), sg.Radio('Disabled', "RADIO1", default=False)], #much better new method :)
            [sg.Text('Left Button:'), sg.InputText()], #values[3]
            [sg.Text('Left Button Link:'), sg.InputText()], #values[4]
            [sg.Text('Right Button:'), sg.InputText()], #values[5]
            [sg.Text('Right Button Link:'), sg.InputText()], #values[6]
            [sg.Button('Start'), sg.Button('Cancel')] ]
#----------------------------------------------------------------------------

# Create the Window
window = sg.Window('Discord RPC Utility', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #print(f"details:{values[0]} state:,{values[1]}, buttondsenabled:{values[2]},buttonsdisabled{values[3]},button01{values[4]},button01URL{values[5]},button02{values[6]}") #Used only for debugging purposes
    #Transforming the "values" into variables for easier maintence
    state=values[1]
    details=values[0]
    button01=values[4]
    button01URL=values[5]
    button02=values[6]
    button02URL=values[7]
    buttonsenabled=values[2]
    buttonsdisabled=values[3]
    sg.popup_notify("RPC is running, to stop it close the console window") #Little friendly reminder ;)
    main.main(button01,button01URL,button02,button02URL,state,details,buttonsenabled,buttonsdisabled) #that's were the window stutters ;-; (the suffering never ends...)
#-----------------------------------------------------------------------------------------------------

window.close() #close the window when the loop breaks

#------------------------------------------------------------------------------------------------------
#Made with <3 by ZackTheKill3r
#Made using Python and PySimpleGUI <3