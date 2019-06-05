# McFux
### PoC for abusing McDonald's deals system
~~I'm making this public because Plexure version 2.58.0 made this PoC obsolete.~~
Exploiting the fact that any account doesn't require any email confermation and using fuzzed device/account infos, making two requests (one for registering the account and the other one to reedem the code) gets unlimited coupons.

#### Requirements
- Python >= 3.7
- Java >= 8
- Install requests using <code>pip3 install requests</code>

#### Usage
Run via <code>python3 mcfux.py</code>
It opens a webserver on 127.0.0.1:8081 where you can get a coupon code as proof of the generation.

#### TODO 
- Rewrite the x-plexure-api-key generaton in Python

#### Future development
None, as this version works fine.

#### Legal stuff
~~This doesn't work anymore and~~ it is against McD ToS as you can imagine.
But since others have updated their repos, I as well updated this one.


