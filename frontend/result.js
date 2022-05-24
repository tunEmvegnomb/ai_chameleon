console.log('here is result')
load_gif()


function start_music() {
    console.log('MUSIC START')
    const audioContainer = document.querySelector('#audioContainer');
    audioContainer.loop = true
    audioContainer.play()
}