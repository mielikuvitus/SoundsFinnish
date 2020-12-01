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
        document.getElementById('eye').style.visibility == "hidden";
        document.getElementById('eyeclosed').style.visibility = "visible";
        document.getElementById('password').type = "text";
    }
}

