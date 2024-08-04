import requests
import pymysql.cursors
import creds


URL = "http://127.0.0.1:5000/users/"
id = "100"
user_name = "wabalabadabdab"
data = {"user_name":user_name}
headers = {"Content-Type": "application/json"}

def Rpost():
    try:
        p = requests.post(url=URL+id,headers=headers,json=data)
        if p.status_code != 200:
            raise Exception("test failed :(")
        else:
            print("Posted seccesfully")
    except Exception as error:
        print("We have {error} exeption and test failed")
        

def Rget():
    try:
        g = requests.get(url=URL + id)
        if g.status_code != 200:
            raise Exception("test failed :(")
        else:
            print("Get request successed")
    except Exception as error:
        print("We have {error} and test faild")


def checking_in_db():
    try:
        connection = pymysql.connect(host=creds.MYSQLHOST,
            user=creds.DBUSERNAME,
            password=creds.DBPASS,
            db=creds.MYSQLDB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as error:
        raise Exception(f"Database connection failed: {error}")

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if not result:
                raise Exception(f"no user found with id {id}")
            print(result)
    finally:
        connection.close()


if __name__ == "__main__":
    Rpost()
    Rget()
    checking_in_db()