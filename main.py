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


api_keys = ['AIzaSyCkKz_YpH-Rk5lJs959DAeH5EnubO_347Q', 'AIzaSyA78uY-pger-1sEMfR30Nvb9PyS3mDbUd0', 'AIzaSyBO0dIx8jmoFKbtXUtmfgvdceXLo0fDoeE', 'AIzaSyCdZ-2ov_zOysY_7o-VTY6tnlvKSrf1810']

def input_addr(file):
    with open(file, 'rb') as csvfile:
        with open('output.csv', 'wb') as output:
            reader = csv.DictReader(csvfile)
            writer = csv.writer(output)
            writer.writerow(['ID', 'Parcel ID', 'Property address', 'Lat', 'Lng', '\n'])
            for row in reader:
                id = int(row['ID'])
                p_id = row['Parcel ID']
                address = row['Property address']

                if id <= 2499:
                    api_key = api_keys[0]
                    res = send_req(address, api_key)
                    writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                    print(row)
                elif id <= 4999:
                    api_key = api_keys[1]
                    res = send_req(address, api_key)
                    writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                    print(row)
                elif id <= 7499:
                    api_key = api_keys[2]
                    res = send_req(address, api_key)
                    writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                    print(row)
                elif id <= 9999:
                    api_key = api_keys[3]
                    res = send_req(address, api_key)
                    writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                    print(row)
                else:
                    continue

    print('IO DONE')



def send_req(addr, api_key):
    # https: // maps.googleapis.com / maps / api / geocode / json?address = 2829 + Centerwood + Court, +San + Jose, +CA & key = AIzaSyCkKz_YpH - Rk5lJs959DAeH5EnubO_347Q
    time.sleep(0.05)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '& key =' + api_key
    r = requests.get(url)
    r_json = r.json()
    try:
        lat = str(r_json['results'][0]['geometry']['location']['lat'])
        lng = str(r_json['results'][0]['geometry']['location']['lng'])
        print("lat is " + lat)
        print("lng is " + lng)
    except:
        lat = ''
        lng = ''

    return [lat, lng]


if __name__ == '__main__':
    # send_req('1246 Curtiss Av San Jose, CA 95125')
    # 37.329326, -121.791156    34140430.0	-118625364.0
    input_addr('property-address.csv')

    # send_coor('34.1404300','-118.6253640')


    print('DONE')