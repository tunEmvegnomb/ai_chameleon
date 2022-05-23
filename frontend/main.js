function start_music() {
    const audioContainer = document.querySelector("#audioContainer");
    audioContainer.loop = true
    audioContainer.play()
}

function preview_selfie() {
    let innerCard = document.getElementsByClassName("inner_card")
    let selfieData = document.getElementById("file").files[0]
    
    console.log(innerCard)
    console.log(selfieData)

    let reader = new FileReader();

    reader.addEventListener("load", function() {
        innerCard[0].style.backgroundImage = "url("+ reader.result +")"
    }, false);

    if (file) {
        reader.readAsDataURL(selfieData);
    }
}