console.log('api script on load')

async function uploadSelfie() {
    const selfieData = document.getElementById("file").files[0]
    console.log(selfieData)

    let form_data = new FormData()
    form_data.enctype = "multipart/form-data"
    form_data.append("file_give", selfieData)
    console.log(form_data.get("file_give"))

    const response = await fetch('http://127.0.0.1:5000/saveselfie', {
        method: 'POST',
        body: form_data,
    })

    console.log('셀피를 보내고 받아옵시다')
    response_json = await response.json()
    console.log(response_json)
    const filename = response_json['filename']
    const recent_selfie_id = response_json['recent_selfie_id']

    handleGif(filename, recent_selfie_id)
}

async function handleGif(filename, recent_selfie_id) {
    // request
    let form_data = new FormData()
    form_data.append("filename", filename)
    form_data.append("recent_selfie_id", recent_selfie_id)
    console.log(form_data.get("filename"), form_data.get("recent_selfie_id"))
    // ajax
    const response = await fetch('http://127.0.0.1:5000/savegif', {
        method: 'POST',
        body: form_data
    })

    // response
    console.log(response.json())
}


async function load_gif() {

    let response = await fetch('http://127.0.0.1:5000/loadgif', {
        method: 'GET'
    })
    let response_json = await response.json()
    console.log(response_json)

    // 뿌려주기
    // 스테이터스 코드 활용 해서 작업
    // 얼러트, 리플레이스, 콘솔로그, temp_html appending
}
