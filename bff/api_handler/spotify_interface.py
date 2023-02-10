"""SpotifyAPIに対する操作を実装するインターフェース

Get Recommendationsが返すjsonに対応
https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
"""
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os
from os import path


def dummy_APIcall():
    """仮のjsonレスポンスを返す

    ここのexample:responceを参照
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
    """

    json_path = path.join(path.dirname(__file__), 'dummy.json')
    with open(json_path, 'r') as f:
        d = json.load(f)
    print(d)
    return jsonable_encoder(d)


if __name__ == "__main__":
    dummy_APIcall()
