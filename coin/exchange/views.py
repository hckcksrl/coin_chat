from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
import json
import requests

NotFound = Response(data={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": '해당 코인이 존재하지 않습니다.\n코인 약어를 사용해 보세요\nex) BTC, ETH, XRP'
                            }
                        }
                    ]
                }
            })

with open('/home/ubuntu/coin_chat/coin/exchange/config.json', 'r') as f:
    config = json.load(f)


def ko_or_en(name):
    k_count = 0
    for c in name:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count += 1
            break
        elif ord('ㄱ') <= ord(c) <= ord('ㅎ'):
            k_count += 1
            break
    return False if k_count > 0 else True


def korean_to_english(name):
    if name in config:
        return config[name]
    else:
        return False

class CoinOne(APIView):

    def get_coin(self, name):
        api = f'https://api.coinone.co.kr/ticker?currency={name}'
        data = requests.get(api)
        if len(data.json()) == 404:
            return False
        return data.json()

    def post(self, request:Request):

        data = request.data
        name = data['action']['params']['coin']
        check = ko_or_en(name=name)
        if check is False:
            name = korean_to_english(name=name)

        if name is False:
            return NotFound

        coin_data = self.get_coin(name=name)

        if coin_data is False:
            return NotFound

        price = coin_data["last"]
        currency = coin_data["currency"]
        high = coin_data["high"]
        low = coin_data["low"]
        volumn = coin_data["volume"]
        print(type(int(price)))
        return Response(status=status.HTTP_200_OK,data={
            "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": f'{currency}\n\n가격 : {"{:,}".format(price)} 원\n24시간 최고가격 : {"{:,}".format(high)} 원'
                                f'\n24시간 최저가격 : {"{:,}".format(low)}\n24시간 거래량 : {volumn} {currency}'
                            }
                        }
                    ]
                }
        })


class UpBit(APIView):

    def get_coin(self, name):
        name = name.upper()
        if not name.startswith('KRW-'):
            name = f'KRW-{name}'
        api = f'https://api.upbit.com/v1/ticker?markets={name}'
        data = requests.get(api)

        if data.status_code == 404:
            return False
        return data.json()

    def korean(self, name):
        api = f'https://api.upbit.com/v1/market/all'
        data = requests.get(api)
        check = data.json()

        for i in check:
            if name == i['korean_name']:
                s = i['market']
                if s.startswith('KRW'):
                    return s

        return False

    def post(self, request:Request):

        data = request.data
        name = data['action']['params']['coin']
        check = ko_or_en(name=name)

        if check is False:
            name = self.korean(name=name)

        if name is False:
            return NotFound

        coin_data = self.get_coin(name=name)

        if coin_data is False:
            return NotFound

        return Response(status=status.HTTP_200_OK, data={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f'정답'
                        }
                    }
                ]
            }
        })


class Bithumb(APIView):

    def get_coin(self, name):
        api = f'https://api.bithumb.com/public/ticker/{name}'
        data = requests.get(api)
        if data.status_code == 400:
            return False
        return data.json()

    def post(self, request:Request):

        data = request.data
        name = data['action']['params']['coin']
        check = ko_or_en(name=name)
        if check is False:
            name = korean_to_english(name=name)

        if name is False:
            return NotFound

        coin_data = self.get_coin(name=name)

        if coin_data is False:
            return NotFound

        return Response(status=status.HTTP_200_OK,data={
            "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": f'정답'
                            }
                        }
                    ]
                }
        })
