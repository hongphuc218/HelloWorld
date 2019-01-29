var song = document.getElementById('song_container')
// console.log(song.children)

function clickDelete(event) {
    //event de phan biet cac thang delete
    console.log(event.target.parentNode)
    event.target.parentNode.remove()
}

for (var i = 0; i < song.children.length; i++) {
    // console.log(song.children[i])
    // console.log(song.children[i].className)

    if (song.children[i].className == "song") {
        console.log(song.children[i].children[1].innerHTML)        
        console.log(song.children[i].children[0].innerHTML)
        // Tim the <i> delete </i>
        console.log(song.children[i].children[2])

        //gan su kien cho tung the delete
        song.children[i].children[2].addEventListener("click", clickDelete)

    }
}