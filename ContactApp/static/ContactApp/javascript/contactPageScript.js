var main = function(){
    "use strict";

    var $messageSent = $(".email-message");
    $messageSent.fadeOut(5000)

    var $contactMain = $("main");
    $contactMain.hide();

    $contactMain.fadeIn(2500);
};

$(document).ready(main);