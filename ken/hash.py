import hashlib
import hmac
import base64


def make_digest(message, key):
    key = bytes('ae3e2cfc-c950-461f-93fc-86613ce0cbc2', 'UTF-8')
    message = bytes('/v3/departures/route_type/0/stop/1125/route/5?date_utc=2018-01-10%2022%3A39%3A59&max_results=3&include_cancelled=false&devid=3000271', 'UTF-8')

    digester = hmac.new(key, message, hashlib.sha1)
    # signature1 = digester.hexdigest()
    signature1 = digester.digest()
    # print(signature1)

    # signature2 = base64.urlsafe_b64encode(bytes(signature1, 'UTF-8'))
    signature2 = base64.urlsafe_b64encode(signature1)
    # print(signature2)

    return str(signature2, 'UTF-8')


result = make_digest('message', 'private-key')
print(result)

