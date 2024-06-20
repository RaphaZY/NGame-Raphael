var like = 0;
function liked(){
    var svg = document.getElementById('btlike').querySelector("svg");
    if(like == 0){
        svg.style.fill = "red";
        svg.style.stroke = "red";
        like = 1;
    } else {
        svg.style.fill = "white";
        svg.style.stroke = "red";
        like = 0;
    }
}