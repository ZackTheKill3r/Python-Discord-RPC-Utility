import os
import settings as cfg

#Checks if ManualLanguage is enabled and chooses the preferred language, else it just detects the OS's current language.
if cfg.ManualLanguage is True: 
    language = cfg.Language
else:
   language = (os.getenv('LANG'))

#Português(Brasil)
if "pt_BR" in language:
    Name="Discord RPC Utility"
    Title="Título"
    Subtitle="Subtítulo"
    Description="Descrição"
    Buttons="Botões"
    Top_Button_Title="Título do Botão Superior"
    Top_Button_URL="Link do Botão Superior"
    Bottom_Button_Title="Título do Botão Inferior"
    Bottom_Button_URL="Link do Botão Inferior"
    Okay="Definir RPC"
    Cancel="Cancelar"

#English(US)
elif "en_US" in language:
    Name="Discord RPC Utility"
    Title="Title"
    Subtitle="Subtitle"
    Description="Description"
    Buttons="Buttons"
    Top_Button_Title="Top Button Title"
    Top_Button_URL="Top Button URL"
    Bottom_Button_Title="Bottom Button Title"
    Bottom_Button_URL="Bottom Button URL"
    Okay="Start RPC"
    Cancel="Cancel"

#Português(Portugal)
elif "pt-pt" in language:
    Name="Discord RPC Utility"
    Title="Título"
    Subtitle="Subtítulo"
    Description="Descrição"
    Buttons="Botões"
    Top_Button_Title="Título do Botão de Cima"
    Top_Button_URL="Link do Botão de Cima"
    Bottom_Button_Title="Título do Botão de Baixo"
    Bottom_Button_URL="Link do Botão de Baixo"
    Okay="Definir RPC"
    Cancel="Cancelar"

#Español(Castellana)
elif "es-es" in language:
    Name="Discord RPC Utility"
    Title="Título"
    Subtitle="Subtítulo"
    Description="Descripción"
    Buttons="Botones"
    Top_Button_Title="Título del botón superior"
    Top_Button_URL="Enlace del botón superior"
    Bottom_Button_Title="Título del botón inferior"
    Bottom_Button_URL="Enlace del botón inferior"
    Okay="Definir RPC"
    Cancel="Cancelar"    

#Falls back to English if the user's language isn't available
else:
    Name="Discord RPC Utility"
    Title="Title"
    Subtitle="Subtitle"
    Description="Description"
    Buttons="Buttons"
    Top_Button_Title="Top Button Title"
    Top_Button_URL="Top Button URL"
    Bottom_Button_Title="Bottom Button Title"
    Bottom_Button_URL="Bottom Button URL"
    Okay="Start RPC"
    Cancel="Cancel"
