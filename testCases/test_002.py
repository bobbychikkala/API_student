import requests


class Test002:

    def test_002_post(self):
        username = 'demo'
        key = "eGj4BGVTHRn7mGElYyBXQcmNt32cOo5DwTMRzNLI50lUtqnXzhpfBEYkZuBbGGwNSPCCxvibkLgHdEMaTRnXkNvPvyF3FH2GlQgCLHT2lB00tN2p1nvxKNdBaNGX8klX4AXJoNsoYJgq3tD74j2YsbWByWVPrRGeRTAHobMZhYPrYw1hazfv3Zh2sOAjCFTLXRsd2u8nnvP0kw8UAhBK2rrAMph1P55e7USGXsvnpAvc41i6hQuCHbWAdB57mTwr"
        s = requests.Session()
        response =s.post('https://192.168.13.240/index.php?route=api/login',
            data={'username': username, 'key': key})
