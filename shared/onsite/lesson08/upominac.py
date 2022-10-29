import os
import time
import schedule


def spust_oznamovac_prestavky():
    """
    Zapne oznamovací zvuk, jak nastane konkrétní čas.
    """
    os.system("mpg123 announcer.mp3")
    

schedule.every().day.at("11:30").do(spust_oznamovac_prestavky)
while True:    
    schedule.run_pending()
    time.sleep(1)
