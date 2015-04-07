__author__ = 'alay'

from src.basehandler import BaseHandler


class GetfeedbackHandler(BaseHandler):

    def get(self, *args, **kwargs):
        counter = self.client.get('counter')
        counter = counter.decode('utf-8-')
        self.response['counter'] = counter
        self.response['data'] = {}
        for i in range(0, int(counter)):
            data = self.client.hgetall('voter:' + str(i))
            for each_data in data:
                data[each_data.decode('utf-8')] = data[each_data].decode('utf-8')
                del data[each_data]
                self.response['data']['voter:' + str(i)] = data
        self.send_error(200)
