#!/usr/bin/python3
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from py532lib.mifare import *
import binascii
import subprocess
import os.path

def main():
  card = Mifare()
  uid_old = False
  while True:
    card.SAMconfigure()
    card.set_max_retries(MIFARE_SAFE_RETRIES)
    uid = card.scan_field()

    if uid != uid_old:
      uid_old = uid
      if uid:
        try:
          address = card.mifare_address(0,1)
          card.mifare_auth_a(address, MIFARE_FACTORY_KEY)
          data = card.mifare_read(address)
          card.in_deselect() # In case you want to authorize a different sector.
          cardid=''.join('{:02x}'.format(x) for x in uid)

          print(cardid + ": " + ''.join('{:02x}'.format(x) for x in data) + " ")
          os.system("festival -b '(SayText \"Card " +cardid+ " inserted\")'")
          if(os.path.isfile("./cards/"+cardid+".mp3")):
            if('player' in vars() or 'player' in globals()):
              player.terminate()
            player = subprocess.Popen(["mplayer", "./cards/"+cardid+".mp3", "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          else:
            print("File not found: " + "./cards/"+cardid+".mp3")
        except MifareException:
          print(sys.exc_info()[1])
          pass
        except IOError:
          print("Unexpected error:", sys.exc_info()[0], " ", sys.exc_info()[1])
          pass
      else:
        print("Card removed")
        if('player' in vars() or 'player' in globals()):
          player.terminate()
        os.system("festival -b '(SayText \"Card removed\")'");

if __name__ == '__main__': 
    main()
