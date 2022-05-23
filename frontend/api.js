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
    alert("모델이 돌아가는 중입니다 10초만 대기해주세요")
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

    window.location.replace('http://127.0.0.1:5500/frontend/result.html')
}


async function load_gif() {

    let response = await fetch('http://127.0.0.1:5000/loadgif', {
        method: 'GET'
    })
    let response_json = await response.json()
    console.log(response_json)

    // 의사코드 작성
    // 뿌려주기
    // 스테이터스 코드 활용 해서 작업
    // 얼러트, 리플레이스, 콘솔로그, temp_html appending
}
