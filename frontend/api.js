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

}