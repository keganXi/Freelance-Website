var main = function(){
    "use strict";

    var $emailMessage = $(".email-message");
    $emailMessage.fadeOut(5000)


    var $header = $(".header-wrapper h1");
    $header.hide();

    var $section = $("section");
    $section.hide();

    var $sectionHead = $(".div-block h1 .container");

    var $sectionInfo = $(".div-block .container p");
    $sectionInfo.hide();

    var $contactUsBtn = $(".swa-block");
    $contactUsBtn.hide();

    var $footer = $("footer");
    $footer.hide();

    $header.fadeIn(2500, function(){
        $section.fadeIn(1000, function(){
            $sectionInfo.fadeIn(2000, function(){
                $contactUsBtn.slideDown(2000);
                $footer.slideDown(1000)
            });
        });
    });

};

$(document).ready(main);