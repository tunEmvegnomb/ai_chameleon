console.log('here is result')
load_gif()


function start_music() {
    const audioContainer = document.querySelector('#audioContainer');
    audioContainer.loop = true
    audioContainer.play()
}