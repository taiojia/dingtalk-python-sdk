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

    def send_link(self, title, text, message_url, pic_url):
        """
        the link type

        :param title: message title
        :param text: message text
        :param message_url: message url
        :param pic_url: image url
        :return: dingtalk api response
        """
        data = {
            "msgtype": "link",
            "link": {
                "text": text,
                "title": title,
                "picUrl": pic_url,
                "messageUrl": message_url
            }
        }
        return self._post(data)

    def send_markdown(self, title, text, mobiles=[], at_all=False):
        """
        the markdown type

        :param title:  message title
        :param text: markdown contents
        :param mobiles: the phone number to @
        :param at_all: @ everybody
        :return: dingtalk api response
        """

        data = {
            "msgtype": "markdown",
            "markdown": {"title": title,
                         "text": text
                         },
            "at": {
                "atMobiles": mobiles,
                "isAtAll": at_all
            }
        }
        return self._post(data)
