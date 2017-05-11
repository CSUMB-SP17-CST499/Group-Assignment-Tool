import requests
import urllib
import json
from apis import token

class Connection:
    
    def _request(self, slack_token, method = '?', params = {}):
        headers = {'Connection': 'close'}
        domain = 'slack.com'
        params['token'] = token
        data = urllib.parse.urlencode(params)
        
        url = 'https://{1}/api/{2}'.format(domain, method)
        return requests.post(url, headers=headers, data=params).text