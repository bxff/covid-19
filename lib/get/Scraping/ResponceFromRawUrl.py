import requests

def getResponceFromRawUrl(raw_url:str):
    # using requests instent of client.get_memento(raw_url) as its buggy in the time of the creation of this code
    x = True
    c = 0
    while x:  # loop to keep trying...
        try:
            c+=1
            response = requests.get(raw_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                "Host": "web.archive.org"
            })
            if response != None:
                x = False
        except:
            print("[!] Failed to get the responce of `raw_url`, tring again.")
            print(f"[!] Count: {c}")
            pass
    return response

    # # using client.get_memento with a loop doesnt help, but you could try this when its fixed
    # x = True
    # while x:
    #     try:
    #         response = client.get_memento(raw_url)
    #         if response != None:
    #             x = False
    #     except:
    #         print(raw_url)
    #         pass
    # return response
