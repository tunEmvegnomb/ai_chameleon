console.log('here is result')
load_gif()

select_music()

function start_music() {
    const audioContainer = document.querySelector('#audioontainer');
    audioContainer.loop = true
    audioContainer.play()
}