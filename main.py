# GoogleMap API Keys

# AIzaSyCkKz_YpH-Rk5lJs959DAeH5EnubO_347Q - George TEST
# AIzaSyA78uY-pger-1sEMfR30Nvb9PyS3mDbUd0 - Mia TEST
# AIzaSyBO0dIx8jmoFKbtXUtmfgvdceXLo0fDoeE - Dylan
# AIzaSyCdZ-2ov_zOysY_7o-VTY6tnlvKSrf1810 - Dylan
# AIzaSyBtjsAaMB79mYY8Fz2CsR85fPfhR1Z4RQM - MPudge TEST 10/4/17

# AIzaSyBwQPC59fau2aggLlGZeLiUWPfh2xajKtg - George Proteus (NEW)
# AIzaSyAc_8udLe21uyv225X8IFjzOOa3a9uwL6M - George SJSU (NEW)
# AIzaSyA_KjwyuZ6NhU9e5xxr7KcwCQyYybhL_jc - George 814 (NEW)
# AIzaSyALKz4fzUlBkjPWhdmThaVOs9w9uNBtdOM - George 343 (NEW)

# Free up to 2,500 requests per day. 50 per second.
# $0.50 USD / 1,000 additional requests, up to 100,000 daily, if billing is enabled.

import requests
import time
import csv


api_keys = ['AIzaSyCkKz_YpH-Rk5lJs959DAeH5EnubO_347Q', 'AIzaSyA78uY-pger-1sEMfR30Nvb9PyS3mDbUd0', 'AIzaSyBO0dIx8jmoFKbtXUtmfgvdceXLo0fDoeE', 'AIzaSyCdZ-2ov_zOysY_7o-VTY6tnlvKSrf1810']

blah = 'AIzaSyBwQPC59fau2aggLlGZeLiUWPfh2xajKtg'


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

                if id < 2400:
                    api_key = blah
                    res = send_req(address, api_key)
                    writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                    print(row)
                # elif id < 4800:
                #     api_key = api_keys[3]
                #     res = send_req(address, api_key)
                #     writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                #     print(row)
                # elif id < 7500:
                #     api_key = api_keys[2]
                #     res = send_req(address, api_key)
                #     writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                #     print(row)
                # elif id < 10000:
                #     api_key = api_keys[3]
                #     res = send_req(address, api_key)
                #     writer.writerow([id, p_id, address, res[0], res[1], '\n'])
                #     print(row)
                else:
                    print(row)

    print('IO DONE')



def send_req(addr, api_key):
    # https://maps.googleapis.com/maps/api/geocode/json?address=2829+Centerwood+Court,+San+Jose,+CA&key=AIzaSyCkKzYpH-Rk5lJs959DAeH5EnubO_347Q
    time.sleep(0.05)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '& key =' + api_key
    r = requests.get(url)
    r_json = r.json()
    try:
        print r_json
        lat = str(r_json['results'][0]['geometry']['location']['lat'])
        lng = str(r_json['results'][0]['geometry']['location']['lng'])
        print("lat is " + lat)
        print("lng is " + lng)
    except:
        lat = ''
        lng = ''
        print('ERROR send req')

    return [lat, lng]


if __name__ == '__main__':
    # send_req('1246 Curtiss Av San Jose, CA 95125')
    # 37.329326, -121.791156    34140430.0	-118625364.0
    input_addr('property-address.csv')

    # send_coor('34.1404300','-118.6253640')


    print('DONE')