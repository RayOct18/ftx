from ftx import FtxClient
from secret import api_key, api_secret

if __name__ == '__main__':
    client = FtxClient(api_key, api_secret)
    print(client.list_markets())
