import requests
import json
import re
import os
from tqdm import tqdm
import pandas as pd

headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "cookie":'_trackity=8696091e-f76b-b306-1e23-da0a85adf480; _gcl_au=1.1.1750823129.1667055175; _fbp=fb.1.1667055175488.1329747993; __RC=4; __R=1; _hjSessionUser_522327=eyJpZCI6IjdmNjc4YjY5LTk4Y2QtNTY2YS1hYWYwLWQzYjNmOGU1NjBmYyIsImNyZWF0ZWQiOjE2NjcwNTUxNzUzNTUsImV4aXN0aW5nIjp0cnVlfQ==; __UF=-1; __tb=0; _bs=21f6550d-137f-27bd-f56e-a1258a13ccda; __IP=1952460427; rl_page_init_referrer=StackityEncrypt:U2FsdGVkX1/Hr1air3EcLRKdkELmiRmERDN+G3YLehaOuc+t+skW5zIQTFGua1uw; rl_page_init_referring_domain=StackityEncrypt:U2FsdGVkX19wls0Ll3k8dFKk/AAaYXINvLaLrc2fBOpzFC3RGntfynjAT0IYg2M1; rl_group_id=StackityEncrypt:U2FsdGVkX19v42npyQrwBbWfBfth+3DEBHEdhAfwL7g=; rl_group_trait=StackityEncrypt:U2FsdGVkX1+WhJ0Dn4KHuAS9r24O3Yv1JwKC+VkcFZw=; rl_anonymous_id=StackityEncrypt:U2FsdGVkX1/M3rjRnNA5470lMMe4sxNkinSwg22y2nMPLLo7o1znsgD4OotsImITQMnPtPwPiGNm5Lx4zqe1kw==; rl_user_id=StackityEncrypt:U2FsdGVkX19vURNNX7Ulv8Q0M2BbbEvR6WYER4cIKi0=; rl_trait=StackityEncrypt:U2FsdGVkX19SrxirxGwbZUkFz7OSz+EeaDH0iBeTTTFHhCM7Z+zHgfExVzaOoe4C/aXjfHNW+wWac7VPMRyqhA==; __uidac=231be8277114f6a140fadb2be756fb2e; amp_99d374=EyOGNBnT7ei63RJgdsAbfL.MTY2OTA3Mw==..1giv2crm4.1giv2ctt3.g4.js.140; cto_bundle=1j0JNV9Wa05sdzVNZHpOVlJ1T1A2ZWhJOSUyQlBCUmFibER3OXFRaXVNbEtSTjdadmtOcUZZWXpZaHc2ck5Rc0k2a0Fia3F2NzhWaUZiVVl1UzNjWXVJSHA5UnNIQnozaE41JTJCc2FCQWw5N0t2elolMkZHZjEzN1VjZXNya3NtVXZSbm5HZmZiY0slMkJnNkxSSThPekFDY2g2eHptQ1RFZyUzRCUzRA; OTZ=6869312_28_28__28_; TOKENS={"access_token":"MmxEUvj2DePqa6kdJT5husHzR0N4K3BA"}; _gid=GA1.2.1158998007.1674464207; tiki_client_id=317787655.1667055171; TIKI_RECOMMENDATION=7ecacc695e97c436a4e65235cd7a7652; delivery_zone=Vk4wMzQwMjQwMTM=; TKSESSID=10f3a1bf4ea5403e60627397321caf20; _gat=1; _ga_GSD4ETCY1D=GS1.1.1674487200.34.1.1674488094.48.0.0; _ga=GA1.1.317787655.1667055171'
        }

shop_api = 'https://tiki.vn/api/shopping/v2/widgets/seller?seller_id={}'

def parser_shop(json):
    d = dict()
    d['shop_id'] = json.get('id')
    d['name'] = json.get('name')
    d['avg_rating_point'] = json.get('avg_rating_point')
    d['days_since_joined'] = json.get('days_since_joined')
    d['is_official'] = json.get('is_official')
    d['review_count'] = json.get('review_count')
    d['store_id'] = json.get('store_id')
    d['store_level'] = json.get('store_level')
    d['total_follower'] = json.get('total_follower')
    return d

def get_shop_information(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']['seller']
    return 0
shop_inf = []
seller_id = pd.read_csv('C:\\D\\Doan\\data-platform\\data\\seller_id4.csv')

for i in seller_id["seller_id"][0:4000]:
    json_seller = get_shop_information(f'https://tiki.vn/api/shopping/v2/widgets/seller?seller_id={i}')
    print(i)
    shop_inf.append(parser_shop(json_seller))

shop_inf = pd.DataFrame(shop_inf)
shop_inf.to_csv('C:/D/Doan/data-platform/data/shopinfo.csv', index=False)
