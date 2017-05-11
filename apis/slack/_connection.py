import requests
import urllib
import json
from apis import token

class SlackConnection():
    
    def _request(self, slack_token, method = '?', params = {}):
        headers = {'Connection': 'close'}
        domain = 'slack.com'
        params['token'] = slack_token
        data = urllib.parse.urlencode(params)
        
        url = 'https://{0}/api/{1}?{2}'.format(domain, method, data)
        return requests.post(url, headers=headers).text