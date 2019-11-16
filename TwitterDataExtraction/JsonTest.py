import json
from json import JSONEncoder

class MobilePhone:

    contacts = None
    apps     = None
    def __init__(self, contacts, apps):

        self.contacts   = contacts

        self.apps       = apps


class MobilePhoneEncoder(JSONEncoder):

    def default(self, object):

        if isinstance(object, MobilePhone):

            return object.__dict__

        else:

            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return json.JSONEncoder.default(self, object)



contacts = {"xxx-xxx-xxxx": "Joe",

            "yyy-yyy-yyyy": "Joe",

            "zzz-zzz-zzzz": "Ane",

            "aaa-aaa-aaaa": "Rod",

            }

apps     = ["facebook",

            "linkedin",

            "twitter"]



myMobile = MobilePhone(contacts, apps)

jsonString      = MobilePhoneEncoder().encode(myMobile)

print(jsonString)