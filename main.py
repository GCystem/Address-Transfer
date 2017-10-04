# GoogleMap API Keys
# AIzaSyCkKz_YpH-Rk5lJs959DAeH5EnubO_347Q - George
# AIzaSyA78uY-pger-1sEMfR30Nvb9PyS3mDbUd0 - Mia
# AIzaSyBO0dIx8jmoFKbtXUtmfgvdceXLo0fDoeE - Dylan
# AIzaSyCdZ-2ov_zOysY_7o-VTY6tnlvKSrf1810 - Dylan

# Free up to 2,500 requests per day.
# $0.50 USD / 1,000 additional requests, up to 100,000 daily, if billing is enabled.

import requests
import time
import csv

api_key = 'AIzaSyCkKz_YpH-Rk5lJs959DAeH5EnubO_347Q'
splitter = '#'


def input_addr(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = int(row['id'])
            if id <= 2400:
                print(row)

    print('DONE')



def send_req(addr):
    # https: // maps.googleapis.com / maps / api / geocode / json?address = 2829 + Centerwood + Court, +San + Jose, +CA & key = AIzaSyCkKz_YpH - Rk5lJs959DAeH5EnubO_347Q
    time.sleep(0.1)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '& key =' + api_key
    r = requests.get(url)
    r_json = r.json()

    lat = str(r_json['results'][0]['geometry']['location']['lat'])
    lng = str(r_json['results'][0]['geometry']['location']['lng'])
    print("lat is " + lat)
    print("lng is " + lng)

def send_coor(lat, lng):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + lng + '& key =' + api_key
    print(url)
    r = requests.get(url)
    r_json = r.json()

    addr = r_json['results'][0]['formatted_address']

    print(addr)


def output_addr():



    print()

if __name__ == '__main__':
    # send_req('1246 Curtiss Av San Jose, CA 95125')
    # 37.329326, -121.791156    34140430.0	-118625364.0
    input_addr('property-address.csv')

    # send_coor('34.1404300','-118.6253640')


    print('DONE')