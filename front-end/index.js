var i = 0;
const original = document.getElementById("demo").innerHTML
var txt = 'It\'s better before, the best before.';
var speed = 100;

function typeWriter(){
  if (i < txt.length){
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

function reverse(){
    if(i >= 0){
        document.getElementById("demo").innerHTML -= txt.charAt(i);
        i = i - 1;
        setTimeout(reverse, speed);
    }
}


typeWriter();





