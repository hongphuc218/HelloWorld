var example = document.getElementById('example')
console.log(example);
// example.addEventListener("click", )
var button = document.getElementsByClassName('remove_button')
console.log(button); // getByClass => nó là 1 list

//event n la có sẵn của js. CHỈ CẦN BIẾT DÙNG/ KHÔNG CẦN HIỂU
function Clicked(event) {
    console.log(event.target.parentNode);
    event.target.parentNode.remove()
    
}
for (var i = 0; i < button.length; i ++) {
    console.log(button[i]);
    button[i].addEventListener('click', Clicked)
    
}