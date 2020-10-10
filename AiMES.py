
"""
The most powerful script ever.
WINDOWS ONLY

"""
try:
    import save_logs
    import eel
    import concurrent.futures
    import photon
    import time
    import re
    import tasks_manager
    import datetime

except:

    files = [
        'photon.py',
        'collect_data.py',
        'email_finder.py',
        'chromedriver_update.py',
        'output.txt',
        'future_proof.py',
        'save_logs.py',
        'testing.py',
        'tasks_manager.py'
    ]

    web_files = [
        'index.html',
        'main.js',
        'style.css'
    ]

    for file in files:
        try:
            location = f"..\\backup\\{file}"
            with open(location, 'r') as f:
                with open(file, 'w') as g:
                    g.write(f.read())
        except:
            print(f'Cannot localise {file}')

    for web_file in web_files:
        try:
            location = f"..\\backup\\web\\{web_file}"
            ext_location = f"web\\{web_file}"
            with open(location, 'r') as f:
                with open(ext_location, 'w') as g:
                    g.write(f.read())
        except:
            print(f'Cannot localise {web_file}')

    print("Files localised successfully")

    import save_logs
    import eel
    import concurrent.futures
    import photon
    import time
    import re
    import tasks_manager
    import datetime


def restore_backup():

    files = [
        'photon.py',
        'collect_data.py',
        'email_finder.py',
        'chromedriver_update.py',
        'output.txt',
        'future_proof.py',
        'save_logs.py',
        'testing.py',
        'tasks_manager.py'
    ]

    web_files = [
        'index.html',
        'main.js',
        'style.css'
    ]

    for file in files:
        try:
            location = f"..\\backup\\{file}"
            with open(location, 'r') as f:
                with open(file, 'w') as g:
                    g.write(f.read())
        except:
            print(f'Cannot localise {file}')

    for web_file in web_files:
        try:
            location = f"..\\backup\\web\\{web_file}"
            ext_location = f"web\\{web_file}"
            with open(location, 'r') as f:
                with open(ext_location, 'w') as g:
                    g.write(f.read())
        except:
            print(f'Cannot localise {web_file}')

    print("Files localised successfully")

    import save_logs
    import eel
    import concurrent.futures
    import photon
    import time
    import re
    import tasks_manager
    import datetime


eel.init('web')


@eel.expose
def start_printing(start, end):

    if format_response(start, end):
        cons = f"Running AI. Start Date = {start} End Date= {end}"
        printed_update(cons)
        stat_update("Process Started")
        stat_deets_update("Scanning...")
        tasks_manager.main(start, end)

    else:
        cons = "Format input error. Please check and try again."
        printed_update(cons)
        eel.changeBack()


def format_response(start, end):

    if re.search(r'\w\w/\w\w/\w{4}', start) and re.search(r'\w\w/\w\w/\w{4}', end):
        return True
    else:
        return False


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


def start_gui():

    eel.start('index.html', size=(1100, 650))

def call_for_update():
    # Calls Photon to Update the Files
    photon.main()
    try:
        # Attempts to save logs (If file indeed exists and is working, should be fine)
        save_logs.log("Checking files...")
        printed_update("Files Verified. System is ready.")
    except:
        # Restores files from local backup because error detected in updated files
        restore_backup()
        printed_update("Localised Verified. System is ready.")


save_logs.log_init()
t1 = time.perf_counter()
start_time = datetime.datetime.now()

# Starts Updating Files from server
try:
    # Calls Photon main to update
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(call_for_update)
        executor.submit(start_gui)



finally:
    t2 = time.perf_counter()
    cons = f'Task completed in {"{:.2f}".format(t2 - t1)} seconds'
    stat_update("Success!")
    printed_update(cons)
    save_logs.execute(start_time, cons)
