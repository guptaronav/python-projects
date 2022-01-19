##import requests
##
##
##url = "https://discord.com/api/v8/applications/834967964490661908/commands"
##
##json = {
##    "name": "blep",
##    "description": "Send a random adorable animal photo",
##    "options": [
##        {
##            "name": "animal",
##            "description": "The type of animal",
##            "type": 3,
##            "required": True,
##            "choices": [
##                {
##                    "name": "Dog",
##                    "value": "animal_dog"
##                },
##                {
##                    "name": "Cat",
##                    "value": "animal_cat"
##                },
##                {
##                    "name": "Penguin",
##                    "value": "animal_penguin"
##                }
##            ]
##        },
##        {
##            "name": "only_smol",
##            "description": "Whether to show only baby animals",
##            "type": 5,
##            "required": False
##        }
##    ]
##}
##
### For authorization, you can use either your bot token
##headers = {
##    "Authorization": "Bot ODM0OTY3OTY0NDkwNjYxOTA4.YIImgw.hLx3RgyA5AF5j-R9v1Sx_Q23o64"
##}
##
##r = requests.post(url, headers=headers, json=json)
##print(r)


import selfbot

