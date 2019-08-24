# McFux
### PoC for abusing McDonald's deals system

Exploiting the fact that any account doesn't require any email confermation and using fuzzed device/account infos, making two requests (one for registering the account and the other one to reedem the code) gets unlimited coupons.

24/08/2019 Update: McD updated their backend, so this PoC is no longer working.

#### Requirements
- Python >= 3.7
- Java >= 8
- Install requests using <code>pip3 install requests --user</code>

#### Usage
Run via <code>python3 mcfux.py</code>

It opens a webserver on 127.0.0.1:8081 where you can get a coupon code (15916) as proof of the generation.

#### TODO 
- Make this work with the new >=2.0 McD app update
- Rewrite the x-plexure-api-key generaton in Python

#### Future development
An updated version of this PoC will be done eventually.

#### Legal stuff
Is a PoC not inteded to harm/be used in any circumstances other than testing.
I take no responsibilities for any usage of this code. It was fun to make, that's it.
