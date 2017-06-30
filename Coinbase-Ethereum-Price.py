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
