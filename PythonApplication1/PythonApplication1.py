# -*- coding: cp1251 -*-

import webbrowser

from win10toast_click import ToastNotifier 



def open_eyes_healtcare():
    website = "https://www.wikihow.com/Exercise-Your-Eyes"
    try:
        webbrowser.open(website)
    except:
        print("Failed to open the download page.")
              
toast = ToastNotifier() #так будут реализованы уведомления, нужен UI вместе с окном чтобы настроить инфу для такого
toast.show_toast("Please make your eyes heathy", "Look into distance, then take a close loot at ur finger, close your eyes fo 20s", duration=30, callback_on_click=open_eyes_healtcare)
                          
print (webbrowser._tryorder)
