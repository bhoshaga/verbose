import requests
import datetime
import os
import time
import concurrent.futures
import future_proof
import save_logs
import eel
import re
from time import sleep



files = {

    # 'AiMES.py': "https://drive.google.com/uc?export=download&id=1M72NPLsVZJQ52jixNWrGBuIRX6Obi_6A",
    # 'collect_data.py': "https://drive.google.com/uc?export=download&id=1dXfQh2WVpYUAXqQeIZ8Oiwk0_ZniLtiz",
    # 'email_finder.py': "https://drive.google.com/uc?export=download&id=17VwjWPzDIwJkXNnjQ7cHee6zS4UQkQIH",
    # 'chromedriver_update.py': "https://drive.google.com/uc?export=download&id=1gxzDLUrVgo-jXWnmDiPT0mJSbkwtckNJ",
    # 'future_proof.py': "https://drive.google.com/uc?export=download&id=1O0Oe5xhP_0GNxo864SO_hwgYdQWmzyOL",
    # 'save_logs.py': "https://drive.google.com/uc?export=download&id=1YxinXi7HRD9GrJtOxuIoVouYJzsE4hiQ",
    # 'testing.py': "https://drive.google.com/uc?export=download&id=1TaaeJdsGzCagO11hUFBXE1qkqli5wmqi",
    # 'tasks_manager.py': "https://drive.google.com/uc?export=download&id=1TrPcdR3MXIaRa53OBBePaEbdV0AnUcLI",
    # 'index.html': "https://drive.google.com/uc?export=download&id=1x5qCnJwzo1m5WpY8RH3zkspUa5BRLbO8",
    # 'main.js': "https://drive.google.com/uc?export=download&id=1SYFlW0AK2cNIOfDzYm-hyW4Na3_bYSnC",
    # 'style.css': "https://drive.google.com/uc?export=download&id=1MVVIwyYUdpBjm4-Ot6sqsI1KX_D_oY2B"


}

"""eel parts reacting with the ui"""


def printed_update(update):
    print(update)
    main_update(update)
    save_logs.log(update)


def main_update(update):
    eel.mainUpdate(update)


def stat_update(status):
    eel.statUpdate(status)


def stat_deets_update(deets):
    eel.statDeetsUpdate(deets)


def update_files(x, y):

    file_name = x
    print(file_name)
    save_logs.log(file_name)
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0"
    }
    r = requests.get(y, allow_redirects=True, headers=headers, timeout=10)
    web_documents = ['index.html', 'main.js', 'style.css']
    if file_name in web_documents:
        location = f"web\\{file_name}"
        with open(location, 'wb') as f:
            f.write(r.content)
    else:
        with open(file_name, 'wb') as f:
            f.write(r.content)
    printed_update(f"{file_name} updated")


def execute():
    cons = "System is ready"
    printed_update(cons)
    try:
        future_proof.main()
    except:
        cons = "future proof error..."
        printed_update(cons)


def start_here():

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(update_files, x, y) for x, y in files.items()]
        for f in concurrent.futures.as_completed(results):
            cons = f.result()
            printed_update(cons)

        cons = "Update Complete"
        printed_update(cons)

    execute()


def main():
    sleep(2)
    cons = "System initialising..."
    printed_update(cons)
    try:
        start_here()
    except:
        pass


if __name__ == "__main__":
    main()
