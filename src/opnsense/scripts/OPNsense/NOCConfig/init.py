#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>

    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application

"""

import json
import os
import shutil


def modInfo():
    # /usr/local/opnsense/version/core
    '''
    {
        "product_abi": "22.1",
        "product_arch": "amd64",
        "product_copyright_owner": "Deciso B.V.",
        "product_copyright_url": "https://www.deciso.com/",
        "product_copyright_years": "2014-2022",
        "product_email": "project@opnsense.org",
        "product_flavour": "OpenSSL",
        "product_hash": "a8aabc538",
        "product_id": "opnsense",
        "product_name": "OPNsense",
        "product_nickname": "Observant Owl",
        "product_series": "22.1",
        "product_version": "22.1.8_1",
        "product_website": "https://opnsense.org/"
    }
    '''

    try:
        result = {}

        # core
        core_path = "/usr/local/opnsense/version/core"
        core_exists = os.path.exists(core_path)
        core_mod = {
            "product_name": "NOC",
            "product_nickname": "NovaIntechs",
            "product_email": "info@novaintechs.com",
            "product_website": "https://novaintechs.com/",

            # "Nova Intelligent Technology JSC.,",
            "product_copyright_owner": "NovaIntechs JSC.,",
            "product_copyright_url": "https://novaintechs.com/",
            "product_copyright_years": "2021-2022",
        }
        result["core"] = {}
        result["core"]["path"] = core_path
        result["core"]["exist"] = core_exists

        if core_exists:
            with open(core_path) as f:
                data = json.load(f)
                for k in core_mod.keys():
                    if k in data:
                        data[k] = core_mod[k]
                        result["core"][k] = core_mod[k]

        new_data = json.dumps(data, indent=4)
        with open(core_path, "w") as f:
            f.write(new_data)

        result["message"] = "modInfo() ok! 💖"

        return result

    except Exception as e:
        return {
            "message": e,
        }


def copyFiles():
    try:
        src_dir = "/usr/local/opnsense/service/templates/OPNsense/NOCConfig/"

        _json = '''
        [
            {
                "name": "default-logo.svg",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            },
            {
                "name": "icon-logo.svg",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            },
            {
                "name": "favicon.png",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            }
        ]
        
        '''

        _list = json.loads(_json)

        result = {}
        result["pwd"] = os.getcwd()
        result["src_dir"] = src_dir

        for item in _list:
            name = item["name"]

            result[name] = {}

            src = os.path.join(src_dir, name)
            src_exist = os.path.exists(src)

            result[name]["src"] = {}
            result[name]["src"]["path"] = src
            result[name]["src"]["exist"] = src_exist

            dst = os.path.join(item["dest"], name)
            dst_exist = os.path.exists(dst)

            result[name]["dst"] = {}
            result[name]["dst"]["path"] = dst
            result[name]["dst"]["exist"] = dst_exist

            if src_exist and dst_exist:
                result[name]["copy"] = shutil.copyfile(src, dst)

        result["message"] = "copyFiles() ok! 💖"

        return result
    except Exception as e:
        return {
            "message": e,
        }


def main():
    print(">>> copyFiles()")
    print(json.dumps(copyFiles(), indent=4))
    print()
    print(">>> modInfo()")
    print(json.dumps(modInfo(), indent=4))


if __name__ == "__main__":
    main()
