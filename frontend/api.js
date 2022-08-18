async function uploadSelfie() {
    const selfieData = document.getElementById("file").files[0]

    let form_data = new FormData()
    form_data.enctype = "multipart/form-data"
    form_data.append("file_give", selfieData)

    const response = await fetch('http://127.0.0.1:5000/saveselfie', {
        method: 'POST',
        body: form_data,
    })


    response_json = await response.json()
    const filename = response_json['filename']
    const recent_selfie_id = response_json['recent_selfie_id']

    handleGif(filename, recent_selfie_id)
}

async function handleGif(filename, recent_selfie_id) {
    alert("모델이 돌아가는 중입니다 10초만 대기해주세요")
    let form_data = new FormData()
    form_data.append("filename", filename)
    form_data.append("recent_selfie_id", recent_selfie_id)
    const response = await fetch('http://127.0.0.1:5000/savegif', {
        method: 'POST',
        body: form_data
    })
    window.location.replace('http://127.0.0.1:5500/frontend/result.html')
}


async function load_gif() {
    let response = await fetch(`http://127.0.0.1:5000/loadgif?current_time`, {
        method: 'GET'
    })
    let response_json = await response.json()
    let current_time = response_json['current_time']
    let path = '../backend/static/image/gif/' + current_time + '.gif'
    const inner_card = document.getElementById("inner_card")
    inner_card.style.backgroundImage = "url(" + path + ")"
    const download = document.getElementById("download")
    download.href = path
}


async function select_music() {
    let response = await fetch('http://127.0.0.1:5000/emotion', {
        method: 'GET'
    })

    let response_json = await response.json()

    const emotional_music = response_json['music_index'] + '.mp3'
    const music_path = '../frontend/audio/' + emotional_music

    const audioSource = document.getElementById("audioSource")
    audioSource.src = music_path
}