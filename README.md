# McFux
### PoC for abusing McDonald's deals system
I'm making this public because Plexure version 2.58.0 made this PoC obsolete.
Exploiting the fact that any account doesn't require any email confermation and using fuzzed device/account infos, making two requests (one for registering the account and the other one to reedem the code) gets unlimited coupons.

#### Requirements
- Python >= 3.7 
- Install requests using <code>pip3 install requests</code>

#### Usage
Run via <code>python3 mcfux.py</code>

#### TODO 
There is nothing to add, yolo.

#### Future development
The new Plexure uses a time-based x-plexure-api-key and device registration.
If you know something about encryption look for the generation methods (DES encryption using first 8 bytes of co.vmob.sdk.android.encrypt.key as key)

#### Legal stuff
This doesn't work anymore and it is against McD ToS as you can imagine. 

