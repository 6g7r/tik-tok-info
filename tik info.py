import os
clear = lambda: os.system('cls')
clear()
try:
 
    import requests
 
    
except ImportError: 
 
    print("No module named 'requests' found")
    try:
      os.system('pip install requests')
    except :
      print("pip install requests")
      input("Enter For Exit")
   
try:
 
    from re import search
 
    
except ImportError:
 
    print("No module named 're' found")
    try:
      os.system('pip install re')
    except :
      print("pip install re")
      input("Enter For Exit") 
   
   
try:
 
    from colorama import Fore
 
    
except ImportError:
 
    print("No module named 'colorama' found")
    try:
      os.system('pip install colorama')
    except :
      print("pip install colorama")
      input("Enter For Exit") 
print("""
╔╦═╦╦═╦═╗╔══╦╦╦╗╔══╦═╦╦╗ 𝐵𝑦 6G7R 
║║║║║╔╣║║╚╗╔╣║═╣╚╗╔╣║║═╣  Insta @6g7r
╚╩╩═╩╝╚═╝..╚╝╚╩╩╝..╚╝╚═╩╩╝. Telegram : https://t.me/l_6g7r
""")
class info:
  def requests(self):
    while 1:
      
      self.se=input(f"<{Fore.CYAN}+{Fore.WHITE}> Sessionid : ")
      self.r=requests.post("https://api16-normal-c-alisg.tiktokv.com/2/user/info/?version_code=13.5.0&pass-region=1&pass-route=1&language=ar&app_name=musical_",headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'keep-alive','User-Agent': 'TikTok 13.5.0 rv:135011 (iPhone; iOS 13.4; ar_SA@calendar=gregorian;numbers=latn) Cronet'},cookies={'sessionid':f"{self.se}"}).text
      if '"message":"success"' in self.r:
      
        self.user_id=search(r'"user_id":(.*?),',self.r).groups()[0]
        self.email=search(r'"email":"(.*?)"',self.r).groups()[0]
        self.mobile=search(r'"mobile":"(.*?)"',self.r).groups()[0]
        self.name=search(r'"name":"(.*?)"',self.r).groups()[0]
        self.ver=search(r'"user_verified":(.*?)}',self.r).groups()[0]
        print(f"""
<{Fore.GREEN}1{Fore.WHITE}> User Id :  {self.user_id}

<{Fore.GREEN}2{Fore.WHITE}> Email : {self.email}

<{Fore.GREEN}3{Fore.WHITE}> Mobile :  {self.mobile}

<{Fore.GREEN}4{Fore.WHITE}> Name :  {self.name}
        
<{Fore.GREEN}5{Fore.WHITE}> verified ✔︎ : {self.ver}
        """)
      elif '"message":"error"' in self.r:
        print(f"<{Fore.RED}+{Fore.WHITE}> Sessionid Error login !  ") 
i=info()
i.requests()
