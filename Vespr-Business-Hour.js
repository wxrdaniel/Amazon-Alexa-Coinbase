//
/**
 * @Date:   Jun-17-2017
 * @Project: Alexa Skills
 * @Filename: Vespr-Business-Hour.js
 * @Last modified time: Jun-30-2017
 */
//
//
//                      `-:+poweredo+:-`
//                 `:whmmhyo+/::::/+oyhNmhe:`
//              `+rNh+-               +Nh:ohNe+`
//            :dBy:                 .ve+     :sPr:
//          /mm+`                  :Nd.scafeyo:.+Nd:
//        .dN+`                   sMo     `.:+hNy.oMh.
//       /Nd`                   -dN:           -mm..dN:
//      +Ms                    /Mh`ym           .My  yM/
//     /Ms                   `hM+  hM            Nh   yM:
//    .MN                   -Nm-   hM           -My    dN`
//    yMM-                 oMy.dmy.hM         -sMy/o.  :Ms
//   `MdMh               .dN:   `+.hMold-fashion- .eN.  dN
//   .MsyM-             /Nh.       hM++/s//:.      +Mo  sM.
//   .Ms-Ms           `yMo         hM  :M+         yM-  sM.
//   .Ms dM.         -mm/o.        hM  :M+ ...-:/smm/   yM.
//    Nm :Ms        oMy`:My        hM  :MmddmMMMd/-     Nm
//    sM: mN      .dN/   :Nm+.     hM  :M+   `:omNs.   +M+
//    `mm`+M+    /Nd.      :yNmyo/.+s  :M+       .yMs``Nd
//     -Nd`Nm  `sMo `:        `:oyhmmh+:s.         :NhdN.
//      :MhsM/-mm: +Nh`             `:smmo.         +MN-
//       .mNMmNy` yM/                   -hNs       :Nd.
//        `oMMs  sM/                      /Nh    -hNo
//          .yMy/Md                        +M+ :hNs`
//            `omMm-                       :Mmmm+`
//               -sdNh+:`              `:ohNdo.
//                  `/oydNdhyssssssyhdNdyo:`
//                        `.::::::::.`
//
// Copyright (c) 2017 by wxrdaniel. All Rights Reserved.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.



 'use strict';
 var Alexa = require('alexa-sdk');

 //=========================================================================================================================================
 //TODO: The items below this comment need your attention.
 //=========================================================================================================================================

 //Replace with your app ID (OPTIONAL).  You can find this value at the top of your skill's page on http://developer.amazon.com.
 //Make sure to enclose your value in quotes, like this: var APP_ID = "amzn1.ask.skill.bb4045e6-b3e8-4133-b650-72923c5980f1";
 //Default is undefined
 var APP_ID = " amzn1.ask.skill.7c202ef8-b8cb-41f3-bf28-072c930fadae";

 var SKILL_NAME = "Check Vespr Operation Hours";
 var VESPR_OPERATION_HOURS = "Vespr Coffeebar is open Monday through Friday, from eight a.m. to eleven p.m.! ";
 var VESPR_NOT_YET_OPEN = "Vespr is currently closed. Coffeebar will be opened at eight a.m.! "
 var VESPR_CLOSED = "Vespr is already closed. "
 var VESPR_CLOSING = "Vespr is closing soon! Hurry up! "
 var VESPR_OPENED = "Vespr is serving great coffee right now! Go grab a drink! "
 var HELP_MESSAGE = "You can ask me for vespr coffeebar business hours.";
 var date = new Date();
 var current_hour = date.getHours();
 var current_minute = date.getMinutes();


 exports.handler = function(event, context, callback) {
     var alexa = Alexa.handler(event, context);
     alexa.APP_ID = APP_ID;
     alexa.registerHandlers(handlers);
     alexa.execute();
 };

 var handlers = {
     'LaunchRequest': function () {
         this.emit('VesprOperationHours');
    },
     'VesprOperationHours': function () {
         var speechOutput = VESPR_OPERATION_HOURS;
         if (8 < current_hour < 23) {
             speechOutput = VESPR_OPERATION_HOURS + VESPR_OPENED;
         } else if (3 < current_hour < 8) {
             speechOutput = VESPR_NOT_YET_OPEN;
         } else if (current_hour == 22 ) {
             speechOutput = VESPR_CLOSING;
         } else if ( current_hour >= 23 ){
             speechOutput = VESPR_CLOSED + VESPR_OPERATION_HOURS;
         }
         this.emit(':tell', speechOutput);
     },
     'AMAZON.HelpIntent': function () {
         var speechOutput = HELP_MESSAGE;
         this.emit(':tell', speechOutput);
     },
     'AMAZON.StopIntent': function () {
         this.emit(':tell', speechOutput);
     },
     'AMAZON.CancelIntent': function () {
         this.emit(':tell', specchOutput);
     },
 };
