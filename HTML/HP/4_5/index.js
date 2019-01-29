var i = document.getElementById('i')

function leave() {
    i.style.backgroundColor = 'black';
}

function enter() {
    i.style.backgroundColor = 'red'
}

i.addEventListener('mouseleave', leave)
i.addEventListener('mouseenter', enter)