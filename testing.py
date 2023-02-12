import PyUtls as main
from time import sleep as wait
import random
import shutil
import threading as thr
import sys


lines = 22
columns = shutil.get_terminal_size().columns
lines = int(round(shutil.get_terminal_size().lines/2, 0))



main.settings.logo = '''
██████╗░██╗░░░██╗░░░░░░██╗░░░██╗████████╗██╗██╗░░░░░░██████╗
██╔══██╗╚██╗░██╔╝░░░░░░██║░░░██║╚══██╔══╝██║██║░░░░░██╔════╝
██████╔╝░╚████╔╝░█████╗██║░░░██║░░░██║░░░██║██║░░░░░╚█████╗░
██╔═══╝░░░╚██╔╝░░╚════╝██║░░░██║░░░██║░░░██║██║░░░░░░╚═══██╗
██║░░░░░░░░██║░░░░░░░░░╚██████╔╝░░░██║░░░██║███████╗██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═════╝░'''

main.settings.centerLogo = True
main.settings.logoOnClear = True
main.settings.startmsg = 'Haram code'

main.projectDetails.owner = 'GS'
main.projectDetails.projectName = 'Py-Utils'
main.projectDetails.version = '0.0.2 - Beta'

def e():
    main.bprint('elo')

# main.makeMenu(opt1=e, opt2=e, opt3=e)

# while True:
#     main.bprint('test')
#     wait(.1)

# main.startUp(True)
main.log('sexy')