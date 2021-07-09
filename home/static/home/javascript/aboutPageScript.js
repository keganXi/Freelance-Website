var main = function(){
    "use strict";

    var $messageSent = $(".email-message");
    $messageSent.fadeOut(5000)

    var $header = $("header h1");
    $header.hide();

    var $section = $("section");
    $section.hide();

    var $letsTalk = $(".lets-talk-block");
    $letsTalk.hide();

    var $contentBlock = $(".content-block");
    $contentBlock.hide();

    var $footer = $("footer");
    $footer.hide();

    $header.fadeIn(2500, function(){
        $section.fadeIn(1000, function(){
            $contentBlock.fadeIn(1000, function(){
                $letsTalk.slideDown(2000);
                $footer.slideDown();
            });

        });
    });

 };

$(document).ready(main);
