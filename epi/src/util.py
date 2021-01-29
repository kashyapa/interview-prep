from constants import *
from django.http import HttpResponse
import json

# # to be when updating DB
# def is_db_up():
#
#     f = open("system_status.json")
#     db_status = f.read().encode()
#     print "The system status is " + db_status
#     if db_status in DB_DOWN:
#         return db_status, HttpResponse(json.dumps(HTTP_503_DB_DOWN_RESPONSE), content_type='application/json', status=503)
#     elif db_status in DB_READ_ONLY:
#         return db_status, HttpResponse(json.dumps(HTTP_503_DB_READ_ONLY_RESPONSE), content_type='application/json', status=503)
#     else:
#         return DB_UP, None

def is_db_up():

    db_status = ''.join(open("system_status.json").readline())
    print "The system status is " + db_status
    if db_status == DB_DOWN:
        return db_status, HttpResponse(json.dumps(HTTP_503_DB_DOWN_RESPONSE), content_type='application/json', status=503)
    elif db_status in DB_READ_ONLY:
        return db_status, HttpResponse(json.dumps(HTTP_503_DB_READ_ONLY_RESPONSE), content_type='application/json', status=503)
    else:
        return DB_UP, None

if __name__ == "__main__":
    ret, http_response = is_db_up()
    print http_response
