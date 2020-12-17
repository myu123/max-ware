import pymem
import pymem.process
from cs_offsets import *

def no_flash():
    print("MaxWare has launched!")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                # Sets flash value to 0.
                pm.write_float(flash_value, float(0))


if __name__ == '__main__':
    no_flash()