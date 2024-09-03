import requests

SERVER1 = "http://127.0.0.1:5000/stop_server"
SERVER2 = "http://127.0.0.1:5001/stop_server"

def stop_server_one():
    try:
        requests.get(SERVER1)
        print("Server stopped")
    except Exception as error:
        print(error)

def stop_server_tow():
    try:
        requests.get(SERVER2)
        print("Server stopped")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    stop_server_one()
    stop_server_tow()