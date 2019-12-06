import mysql.connector as conn

class dbClient():
    """https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html"""

    def __init__(self, config:dict):

        self.og_conn = og_conn = conn.connect(**config)
        self.cursor = og_conn.cursor()
    
    def set_handle(self, handle):
        self.handle = handle
    def set_email(self, email):
        self.email = email

    def run_query(self, query):
        try:
            response = self.cursor.execute(query)
        except Exception as ex:
            print("THE FOLLOWING QUERY FAILED:", query)
            print("WITH ERROR", str(ex))
            return ex
        result = []
        for row in self.cursor:
            result.append(row)
        return result

    def run_insert_query(self, query):
        try:
            response = self.cursor.execute(query)
            self.og_conn.commit()
        except Exception as ex:
            print("THE FOLLOWING QUERY FAILED:", query)
            print("WITH ERROR", str(ex))
            return ex
        result = []
        for row in self.cursor:
            result.append(row)
        return result