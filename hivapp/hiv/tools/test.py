import requests
import json

url = 'http://127.0.0.1:8000/login'
s = {'code': "003blGnd0LyAhv1GFapd0u3Jnd0blGnp",
     'encrypt_data': "4k3Ox84qT4t09xKYYt9GNOyi0bXt/6o9IP97l4BJi4EXrAq6TWjEMt6d0s4cICj7CWk0EhndQAx7NGpCm2h1SChAYIZRyCJqdmeO3uXa/06hrRqXL62LUUKrY05hrwkFUfEkwNuynPD7LuMGWosuawJr3psJ95fkObgsIMP098HyW63HvfAlEXD9G38qw5oijXUea1Di5z5bMesdgnf2t4dLIQghgFfuXU857NQpqJiFqfYbcjRvWKaY4k1SV0OsqwhedUqOp2TjmBlAdh66fvtBGpH7mkLLpryPhAePY+cLrtfwE/7xDh6ohTkQMhCji2wqRiE57ocd7M7Xr6rhUrK7XyYQ3noWHKV25MDP/j5GP/SRYCAt86k6i2JA8H6EzXssVKRUhMvsf2pSr50xVcVV1dZXzwSqtMjuOZA1y12avkeWZapOCU7DKk+NY0cumVdWK/Jbvhn7CN1l+ftO+Q==",
     'iv':"J6X217ESxWWH4Bch+2Ss+Q==",
     }
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(url, data=s, headers=headers)
print(r.text)