function setClass()
{
    document.getElementById('next-btn').style.transform = "translateY(6px)";
}

function toggle_visibility() {
    if (document.getElementById('eye').style.visibility == "hidden" || document.getElementById('eyeclosed').style.visibility == "visible") {
        document.getElementById('eye').style.visibility = "visible";
        document.getElementById('eyeclosed').style.visibility = "hidden";
        document.getElementById('password').type = "password";
    } else {
        document.getElementById('eye').style.visibility = "hidden";
        document.getElementById('eyeclosed').style.visibility = "visible";
        document.getElementById('password').type = "text";
    }
}


function toggle_menu_visibility() {
    if (document.getElementById('tab-menu').style.visibility == "hidden" || document.getElementById('tab-close').style.visibility == "visible") {
        document.getElementById('tab-menu').style.visibility = "visible";
        document.getElementById('tab-close').style.visibility = "hidden";
        var icons = document.getElementsByClassName('nav-tab');
        for (var i = 0; i < icons.length; i++){
            icons[i].style.visibility = "hidden";
        }

    } else {
        document.getElementById('tab-menu').style.visibility = "hidden";
        document.getElementById('tab-close').style.visibility = "visible";
        var icons = document.getElementsByClassName('nav-tab');
        for (var i = 0; i < icons.length; i++){
            icons[i].style.visibility = "visible";
        }
    }
}

function calc_scroll_position() {
    var pos = document.getElementById('hsb').scrollLeft;
    var intElemOffsetWidth = document.getElementById('hsb-box').offsetWidth;
    if (intElemOffsetWidth/2 < pos ) {
        document.getElementById('second_dot').style.backgroundColor = "#2690ED";
        document.getElementById('first_dot').style.backgroundColor = "white";
    }else {
        document.getElementById('first_dot').style.backgroundColor = "#2690ED";
        document.getElementById('second_dot').style.backgroundColor = "white";
    }
}

function scroll_to_second() {
document.getElementById('second').scrollIntoView()
document.getElementById('second_dot').style.backgroundColor = "#2690ED";
document.getElementById('first_dot').style.backgroundColor = "white";

}

function scroll_to_first() {
    document.getElementById('first').scrollIntoView()
    document.getElementById('first_dot').style.backgroundColor = "#2690ED";
    document.getElementById('second_dot').style.backgroundColor = "white";
}
