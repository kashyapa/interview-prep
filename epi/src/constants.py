DB_DOWN = ["db_down", "dbdown", "db-down"]
DB_READ_ONLY = [ "db_read_only", "dbreadonly", "db-read-only" ]
DB_UP = "db_up"

HTTP_503_DB_DOWN_RESPONSE = {
    "code": 503,
    "message": "System Under Maintenance - Database is unavailable temporarily. Please check back later."
}

HTTP_503_DB_READ_ONLY_RESPONSE = {
    "code": 503,
    "message": "System Under Maintenance - Database is in read only mode. Updates to database are disabled temporarily. \
    Please check in back later"
}