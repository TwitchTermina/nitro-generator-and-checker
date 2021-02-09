import random, string
print("> imported random")
print("> imported string")
import webbrowser
print("> imported webbrowser")
import time
print("> imported time")
import requests
print("> imported requests")
time.sleep(2)
print("Creator  -  Ichiro#0001 ")
time.sleep(0.3)
print("https://github.com/ichirod-japan   \n")
time.sleep(0.2)

nitroamount=input('Input How Many Codes to Generate and Check: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Wait, Generating for you!")  

for n in range(int(float(nitroamount))):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
