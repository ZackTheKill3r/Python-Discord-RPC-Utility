import PySimpleGUI as sg
import time
import languages as txt
import settings as cfg
import darkdetect

#Checks if ManualThemes are enabled and chooses the preferred theme, else it just detects the OS's current theme.
if cfg.ManualTheme is True:
    theme = cfg.Theme
elif darkdetect.isDark() is True:
    theme = "Dark"
elif darkdetect.isDark() is False:
    theme = "Light"

#Dark Theme palette.
if "Dark" in theme:
    #Dark Theme
    sg.theme_background_color("#4d4d4d")
    sg.theme_text_element_background_color("#4d4d4d")
    sg.theme_element_background_color("#4d4d4d")
    sg.theme_button_color("#1a1a1a")
#Light Theme palette
elif "Light" in theme:
    sg.theme_background_color("#dedede")
    sg.theme_text_element_background_color("#dedede")
    sg.theme_text_color("#000000")
    sg.theme_element_background_color("#dedede")
    sg.theme_button_color("#1a1a1a")

#Presence (the main RPC updater)
def presence(title,description,button_enabled,top_title,top_url,bottom_title,bottom_url):
    from pypresence import Presence
    client_id = cfg.client_id
    RPC = Presence(client_id=client_id)
    RPC.connect()
    if button_enabled is True:
     RPC.update(buttons=[{"label": top_title, "url": top_url}, {"label": bottom_title, "url": bottom_url}],state=description,details=title) #Presence **with** Buttons.
    else:
        RPC.update(state=description, details=title) #Presence without buttons.

    while 1:
     time.sleep(15) #Can only update presence every 15 seconds (Presence loop).

#Main GUI Function
def main():
    layout = [  [sg.Text(txt.Title,)],
                [sg.Input(key='title')],
                [sg.Text(txt.Description)],
                [sg.Input(key='description')],
                [sg.Text(txt.Buttons)],
                [sg.Radio('Disabled', "buttons", default=True), sg.Radio('Enabled', "buttons",key='ButtonEnabled')],
                [sg.Text(txt.Top_Button_Title)],
                [sg.Input(key='top_title')],
                [sg.Text(txt.Top_Button_URL)],
                [sg.Input(key='top_url')],
                [sg.Text(txt.Bottom_Button_Title)],
                [sg.Input(key='bottom_title')],
                [sg.Text(txt.Bottom_Button_URL)],
                [sg.Input(key='bottom_url')],
                [sg.Button(txt.Okay), sg.Button(txt.Cancel)]  ]
                
    window = sg.Window('Discord RPC Utility', layout)

    while True: # GUI Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        title=values['title']
        description=values['description']
        button_enabled=values['ButtonEnabled']
        if button_enabled is True:
            top_title=values['top_title']
            top_url=values['top_url']
            bottom_title=values['bottom_title']
            bottom_url=values['bottom_url']
        else:
            top_title=""
            top_url=""
            bottom_title=""
            bottom_url=""

        if event == txt.Okay: 
            window.perform_long_operation(presence(title,description,button_enabled,top_title,top_url,bottom_title,bottom_url)) #Calls the presence function without lagging the GUI itself.
        elif event  == txt.Cancel:
            break

    window.close()

#Checks if it's being executed directly or imported by another script
if __name__ == '__main__':
    main()
else:
    print("Discord RPC Utility (D.R.U) v2.0 beta\n made with <3 by ZackTheKill3r\n using PySimpleGUI , pypresence and darkdetect")

#Made with <3 By ZackTheKill3r using PySimpleGUI, pypresence and darkdetect.
#Beta 2.0, now lag free :)