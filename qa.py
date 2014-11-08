#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import urllib
import urllib2
import json
 
APP_URL = 'https://api.apigw.smt.docomo.ne.jp/knowledgeQA/v1/ask'
 
class DocomoQA(object):
    def __init__(self, api_key):
        super(DocomoQA, self).__init__()
        self.api_url = APP_URL + '?APIKEY=%s'%(api_key)
        self.context, self.mode = None, None
 
    def __send_message(self, input_message=''):
        encode_input = urllib.quote(input_message)
        request = urllib2.Request(self.api_url + '&q=%s' % input_message)
        request.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(self.api_url + '&q=%s' % encode_input)
        except Exception as e:
            print e
            sys.exit()
        return response
 
    def __process_response(self, response):
        resp_json = json.load(response)
        return resp_json['message']['textForSpeech'].encode('utf-8')
 
    def send_and_get(self, input_message):
        response = self.__send_message(input_message)
        received_message = self.__process_response(response)
        return received_message
 

def get_answer(question):
    self.logger.info('Question is %s' % question)
    api_key = '39766e56706c465152392e5a4a784757417a4e2f4e45436257314a6f6c68645a5648786d7253354f4d6842'
    chat = DocomoQA(api_key)
    resp = chat.send_and_get(message)
    self.logger.info('Answer is %s' % resp)
    return resp

 
def main():
    api_key = '39766e56706c465152392e5a4a784757417a4e2f4e45436257314a6f6c68645a5648786d7253354f4d6842'
    chat = DocomoQA(api_key)
    message = ''
    while message != 'バイバイ':
        message = raw_input('あなた : ')
        resp = chat.send_and_get(message)
        print '相手　 : %s'%(resp)
 
 
if __name__ == '__main__':
    main()

