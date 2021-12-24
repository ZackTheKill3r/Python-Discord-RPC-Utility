import os
language = (os.getenv('LANG'))

#Português(Brasil)
if "pt_BR" in language:
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
