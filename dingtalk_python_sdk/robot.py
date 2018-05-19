import urllib.request
import json


class Robot(object):
    """DingTalk Robot"""

    def __init__(self, webhook):
        self.webhook = webhook

    def _post(self, data):
        req = urllib.request.Request(self.webhook)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        json_data = json.dumps(data)
        json_bytes = json_data.encode('utf-8')
        req.add_header('Content-Length', len(json_bytes))
        res = urllib.request.urlopen(req, json_bytes)
        return res

    def send_text(self, content, mobiles=[], at_all=False):
        """
        the text message format

        :param content: the message content
        :param mobiles: the phone number to @
        :param at_all: @ the all members
        :returns: dingtalk api response
        """
        data = {
            'msgtype': 'text',
            'text': {
                "content": content
            },
            'at': {
                'atMobiles': mobiles,
                'isAtAll': at_all
            }
        }
        return self._post(data)
