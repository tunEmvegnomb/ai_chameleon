console.log('api script on load')

async function uploadSelfie() {
    const selfieData = document.getElementById("file").files[0]
    console.log(selfieData)

    let form_data = new FormData()
    form_data.append("file_give", selfieData)
    console.log(form_data.get("file_give"))


}