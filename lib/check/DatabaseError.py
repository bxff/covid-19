def checkDatabaseError(raw_html:str, raw_url:str):
    check_for_server_error = raw_html.find('Database connection failed: Too many connections (1040)')
    if check_for_server_error >= 0:
        with open('scrap_error.txt', '+a') as f:
            f.write(f"[!] couldent fetch from {raw_url} because of database error 1040(too many connections)")
            print("[!] 1040 Database Error")
            print("[!] Exiting without Scraping this `raw_url`")
        exit(0)
    else: print("[!] No errors found")
