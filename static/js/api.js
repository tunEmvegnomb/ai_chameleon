console.log('api script on load')
let recent_selfie_id
let filename

async function uploadSelfie() {
    const selfieData = document.getElementById("file").files[0]
    console.log(selfieData)

    let form_data = new FormData()
    form_data.append("file_give", selfieData)
    console.log(form_data.get("file_give"))

    // const response = await fetch(`http://127.0.0.1:5000/saveselfie`, {
    //     method: 'POST',
    //     headers: {"Access-Control-Allow-Origin":"*"},
    //     body: JSON.stringify(selfieData),
    //     contentType: false,
    //     processData: false
    // })

    // console.log('셀피를 보내고 받아옵시다')
    // response_json = await response.json()
    // console.log(response_json)

    $.ajax({
        type: "POST",
        url: "/saveselfie",
        data: form_data,
        // json을 배열로 보내려고 해서 생기는 오류 방지
        contentType: false,
        processData: false,
        success: function (response) {
            console.log('response :  ' + response)
            alert('셀피 잘 받았습니다! ^~^')
            // window.location.replace("/result")

            filename = response['filename']
            console.log('파일 네임' + filename)
            recent_selfie_id = response['recent_selfie_id']
            console.log('리센트 아이디' + recent_selfie_id)

            handleGif(filename, recent_selfie_id)
        }
    });

}

async function handleGif(filename, recent_selfie_id) {
    console.log('filename ' + filename)
    console.log('recent_selfie_id ' + recent_selfie_id)
    $.ajax({
        type: "POST",
        url: "/savegif",
        data: { "filename": filename, "recent_selfie_id": recent_selfie_id },
        success: function (response) {
            console.log('response' + response)
            alert('machine learning well done!')
            window.location.replace("/result")
        }
    });
}