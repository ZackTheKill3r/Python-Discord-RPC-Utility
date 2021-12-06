import PySimpleGUI as sg
from pypresence import Presence
import settings as cfg
import time

def main(button01,button01URL,button02,button02URL,state,details,buttonsenabled,buttonsdisabled):
 client_id = cfg.client_id  # Enter your Application ID here.
 RPC = Presence(client_id=client_id)
 RPC.connect()
 
 if buttonsenabled is True:
     RPC.update(buttons=[{"label": f"{button01}", "url": f"{button01URL}"}, {"label": f"{button02}", "url": f"{button02URL}",}],state=f"{state}", details=f"{details}") # Can specify up to 2 buttons
 elif buttonsdisabled is True:
     RPC.update(state=f"{state}", details=f"{details}")

 while 1:
     time.sleep(15) #Can only update presence every 15 seconds



     
