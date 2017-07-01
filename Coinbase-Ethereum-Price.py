# @Date:   Jun-30-2017
# @Project: Alexa Skills
# @Filename: Coinbase-Ethereum-Price.py
# @Last modified time: Jun-30-2017
#
#
#                      `-:+poweredo+:-`
#                 `:whmmhyo+/::::/+oyhNmhe:`
#              `+rNh+-               +Nh:ohNe+`
#            :dBy:                 .ve+     :sPr:
#          /mm+`                  :Nd.scafeyo:.+Nd:
#        .dN+`                   sMo     `.:+hNy.oMh.
#       /Nd`                   -dN:           -mm..dN:
#      +Ms                    /Mh`ym           .My  yM/
#     /Ms                   `hM+  hM            Nh   yM:
#    .MN                   -Nm-   hM           -My    dN`
#    yMM-                 oMy.dmy.hM         -sMy/o.  :Ms
#   `MdMh               .dN:   `+.hMold-fashion- .eN.  dN
#   .MsyM-             /Nh.       hM++/s//:.      +Mo  sM.
#   .Ms-Ms           `yMo         hM  :M+         yM-  sM.
#   .Ms dM.         -mm/o.        hM  :M+ ...-:/smm/   yM.
#    Nm :Ms        oMy`:My        hM  :MmddmMMMd/-     Nm
#    sM: mN      .dN/   :Nm+.     hM  :M+   `:omNs.   +M+
#    `mm`+M+    /Nd.      :yNmyo/.+s  :M+       .yMs``Nd
#     -Nd`Nm  `sMo `:        `:oyhmmh+:s.         :NhdN.
#      :MhsM/-mm: +Nh`             `:smmo.         +MN-
#       .mNMmNy` yM/                   -hNs       :Nd.
#        `oMMs  sM/                      /Nh    -hNo
#          .yMy/Md                        +M+ :hNs`
#            `omMm-                       :Mmmm+`
#               -sdNh+:`              `:ohNdo.
#                  `/oydNdhyssssssyhdNdyo:`
#                        `.::::::::.`
#
# Copyright (c) 2017 by wxrdaniel. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import print_function
import urllib, json

spot_price_url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
buy_price_url = 'https://api.coinbase.com/v2/prices/ETH-USD/buy'
sell_price_url = 'https://api.coinbase.com/v2/prices/ETH-USD/sell'

spot_response = urllib.urlopen(spot_price_url)
spot_data = json.loads(spot_response.read())
spot_price = spot_data[u'data'][u'amount']

buy_response = urllib.urlopen(buy_price_url)
buy_data = json.loads(buy_response.read())
buy_price = buy_data[u'data'][u'amount']

sell_response = urllib.urlopen(sell_price_url)
sell_data = json.loads(sell_response.read())
sell_price = sell_data[u'data'][u'amount']


# ASK response Functions
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# ====================== Skill Functions =======================

def welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hi, feel free to ask me for Ethereum price."
    reprompt_text = "Hi, you can try asking me, how much is ethereum cost right now?"
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Bye!"
    session_attributes = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def check_ethereum_price(intent, session):
    # ================ General JSON Values ==================
    card_title = intent['name']
    session_attributes = {}
    should_end_session = True

    # ================ Speech Out Price ===================
    speech_output = "The Ethereum price right now is " + spot_price + " dollars. " \
                    "You can buy Ethereum now with " + buy_price + " dollars. " \
                    "Or you could sell your Ethereum with " + sell_price + " dollars. "

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, None, should_end_session))



# ============= Events ==============

def session_started(session_started_request, session):
    print('on_session_started requestId=' + session_started_request['requestId'] + ', sessionId=' + session['sessionId'])


def on_launch(intent_request, session):
    return welcome_response()


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "GetEthereumPrice":
        return check_ethereum_price(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")



def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
    ", sessionId=" + session['sessionId'])


# ================== Lambda Handler ==================

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
        event['session']['application']['applicationId'])

    if (event['session']['application']['applicationId'] != "[some-applicationId]"):
        raise ValueError("Invalid Application ID!!!")

    if event['session']['new']:
        session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
