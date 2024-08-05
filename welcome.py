def welcome_message():
    print(art)
    print(controls)


art = r"""
_________                                     
\_   ___ \  ____ _____    ___________ _______ 
/    \  \/_/ __ \\__  \  /  ___/\__  \\_  __ \
\     \___\  ___/ / __ \_\___ \  / __ \|  | \/
 \______  /\___  >____  /____  >(____  /__|   
        \/     \/     \/     \/      \/       
_________               .__                   
\_   ___ \___.__.______ |  |__   ___________  
/    \  \<   |  |\____ \|  |  \_/ __ \_  __ \ 
\     \___\___  ||  |_> >   Y  \  ___/|  | \/ 
 \______  / ____||   __/|___|  /\___  >__|    
        \/\/     |__|        \/     \/.        
"""

controls = r"""
[1] - Santize input text, removes all spaces and sets characters to lowercase.
[2] - Encrypt input text, choose amount of characters to shift in encryption.
[3] - Decrypt input text, use this option when character shift is known.
[4] - Brute force encrypted text outputting all posibilities.
[H] - Show all options available
[Q] - Quit the program
"""