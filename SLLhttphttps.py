
print("\033[31mYOU'RE USING: \033[34mSLLhttphttps")

print(""" \033[34m _________.____    .____    .__     __    __         .__     __    __                
 /   _____/|    |   |    |   |  |___/  |__/  |_______ |  |___/  |__/  |_______  ______
 \_____  \ |    |   |    |   |  |  \   __\   __\____ \|  |  \   __\   __\____ \/  ___/
 /        \|    |___|    |___|   Y  \  |  |  | |  |_> >   Y  \  |  |  | |  |_> >___ \ 
/_______  /|_______ \_______ \___|  /__|  |__| |   __/|___|  /__|  |__| |   __/____  >
        \/         \/       \/    \/           |__|        \/           |__|       \/ """ + "version 1.0 ")
print(f"\033[34mThis program its offline, the list of the trusted websites are on the file if you want to update this you can check mygithublink for updates")

red = ("\033[31m")
green = ("\033[32m")
blue = ("\033[34m")
yellow = "\033[33m"
cyan = "\033[36m"
magenta = "\033[35m"
white = "\033[37m"
black = "\033[30m"
orange = "\033[38;5;208m"
purple = "\033[38;5;129m"
pink = "\033[38;5;218m"
brown = "\033[38;5;94m"
light_blue = "\033[38;5;45m"
light_green = "\033[38;5;120m"
light_gray = "\033[38;5;251m"
dark_gray = "\033[38;5;238m"
gold = "\033[38;5;214m"
silver = "\033[38;5;254m"
dark_red = "\033[38;5;88m"
dark_green = "\033[38;5;22m"

reset_color = "\033[0m"
print(reset_color)

http_link = "http://"
https_link = "https://"
print(f"{red}I DO NOT HAVE IN THE LIST:{blue} {http_link} links {light_green}USE=> {blue}{https_link} links, {light_green}WE ACCEPT:{blue} .com {green}and{blue} .org {green}sites.  "+reset_color)
print(f"{green}THIS CODE WILL NOT WORK IF YOU DON'T USE THE MAIN PAGE OF AN WEBSITE {light_green}EXAMPLE: USE: https://google.com {red}NOT: https://google.com/page ")
user_input = input(f"{green}ENTER your WEBSITE there & press ENTER =>: ")

if user_input.startswith(http_link):
    print(f"This is your website: {user_input}")
    print(f"{red}I DON'T LIKE HTTP LINKS {green}|=> {light_green}TRY USING: {blue}https://  links")
    print(f"{blue}If you want {green}you can run the file again to put another link")
    exit()

if not user_input:
    print(f"{red}You haven't entered any link")
    print(f"{blue}If you want {green}you can run the file again to put a link")
    exit()

trusted_websites = ("https://reddit.com", "https://google.com", "https://youtube.com", "https://wikipedia.com", "https://github.com", "https://mail.google.com", "https://www.geeksforgeeks.org")
if user_input in trusted_websites:
    print(f"YOUR {blue}WEB SITE IS ONE OF OUR{green} TRUSTED{blue} LINKS {green}IN OUR LIST")
    print(f"If you don't trust this response or the link, you can search the short form of the link on the internet and find out if it's legit: \033[94m{user_input[8:-4]}")
    print(reset_color)
    exit()

print(f"{red}YOUR WEBSITE ISN'T IN THE LIST OF TRUSTED LINKS OR IT ISN'T CORRECT")
print(f"If you don't trust this response or the link, you can search the {blue}SHORT FORM=>: \033[94m{user_input[8:-4]}" + f"{blue}<=on the internet" + f"{red} if you don't see the short form corectly means that you don't have entered the link like how did i mention to enter it ")
exit()
