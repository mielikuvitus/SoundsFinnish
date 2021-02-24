function startup() {
    var el = document.getElementById("main");
    el.addEventListener("touchstart", handleStart, false);
    el.addEventListener("touchmove", handleMove, false);
}
  
document.addEventListener("DOMContentLoaded", startup);

var xDown = null;                                                        
var yDown = null;

function getTouches(evt) {
  return evt.touches;
}                                                     

function handleStart(evt) {
    const firstTouch = getTouches(evt)[0];                                     
    xDown = firstTouch.clientX;                                      
    yDown = firstTouch.clientY;                                      
};

function handleStart(evt) {
    const firstTouch = getTouches(evt)[0];                                    
    xDown = firstTouch.clientX;                                      
    yDown = firstTouch.clientY;                                      
};        

function handleMove(evt) {
    if ( ! xDown || ! yDown ) {
        return;
    }

    var xUp = evt.touches[0].clientX;                                    
    var yUp = evt.touches[0].clientY;

    var xDiff = xDown - xUp;
    var yDiff = yDown - yUp;

    if ( Math.abs( xDiff ) > Math.abs( yDiff ) ) {/*most significant*/
        var next = document.getElementById("next-word-a");
        var regex = /\/.*/g;
        if (next != null) {
            var value = next.getAttribute("href");
        }else {
            var el = document.getElementById("btn-back");
            if ( xDiff > 0 ) {
                el.click();
            }else {
                var prev = document.getElementById("previous-word-a");
                var value = prev.getAttribute("href");
                if (value.match(regex)) {
                    if (prev != null) {
                        window.history.pushState(null, null, el.href);
                        window.location = el.href;
                    }
                }
            }
        }
    
        if ( xDiff > 0 ) {
            /* left swipe */
            if (value.match(regex)) {
                var el = document.getElementById("next-word-a");
                if (el != null) {
                    window.history.pushState(null, null, el.href);
                    window.location = el.href;
                }
            }
             
        } else {
            /* right swipe */
            if (value.match(regex)) {
                var el = document.getElementById("previous-word-a");
                if (el != null) {
                    window.history.pushState(null, null, el.href);
                    window.location = el.href;
                }
            }
        }                       
    } else {
        if ( yDiff > 0 ) {
            /* up swipe */ 
        } else { 
            /* down swipe */
        }                                                                 
    }
    /* reset values */
    xDown = null;
    yDown = null;                                             
};