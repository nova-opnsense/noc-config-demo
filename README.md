# noc-config

A plugin for OPNsense

---

## Development guidelines

### pull plugins

```sh
opnsense-code plugins
```

### pull noc source code

```sh
cd /usr/plugins/devel
git clone https://thanhhai135@bitbucket.org/novaintechs/noc-demo.git

cd noc-demo
git checkout develop
```

### build

install

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make install clean
```

using `upgrade` for reinstalling

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make upgrade clean
```

build the package `/usr/plugins/devel/noc-demo/work/pkg/os-noc-demo-1.0_1.txz`

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make package
ls work/pkg/
```

### running

restart config daemon

```sh
service configd restart
```

run command

```sh
configctl nocconfig init

configctl nocconfig ezmesh

configctl nocconfig startbroker
configctl nocconfig stopbroker

configctl nocconfig startclient
configctl nocconfig stopclient
```

### testing

Test ezmesh config

```sh
ezmesh.py
```

Test mqtt connection

```sh
mqtt-test.py
```

Test API

`usage: api.py [-h] [-m METHOD] -a API [-d DATA] [-t CONTENTTYPE]`

Ezmesh API

```sh
api.py \
    -m post \
    -a nocconfig/ezmesh/set \
    -d '{
            "nocconfig": {
                "ezmesh": {
                    "Enabled": "1",
                    "SSID": "NovaIntechs",
                    "Password": "123"
                }
            }
        }'


api.py \
    -a nocconfig/ezmesh/get
```

Segment API

```sh
# get all segments
api.py \
    -a nocconfig/segment/searchItem

# search segment
api.py \
    -m post \
    -a nocconfig/segment/searchItem \
    -d 'current=1&rowCount=1&searchPhrase=<search phrase>' \
    -t 'application/x-www-form-urlencoded'

api.py \
    -a nocconfig/segment/getItem/<uuid>


api.py \
    -m post \
    -a nocconfig/segment/addItem \
    -d '{
            "segment":{
                "enabled":"1",
                "hubId":"123",
                "name":"123",
                "lastUpdate":"123",
                "status":"123"
            }
        }'
```

## python develop environment

Check python version

```sh
python3 --version
```

Build/Install pip

```sh
cd /usr/ports/devel/py-pip
make install clean

# checking
pip --version
```

Generates requirements

```sh
pip install pipreqs
pipreqs --force src/opnsense/scripts/OPNsense/NOCConfig
```

Install dependencies from requirements.txt

```sh
pip install -r src/opnsense/scripts/OPNsense/NOCConfig/requirements.txt
```

---

## About

hai.nt <hai.nt@novaintechs.com>

---
