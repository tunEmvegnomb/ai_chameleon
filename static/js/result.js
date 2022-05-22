console.log('haha')
$(document).ready(function(){
    load_gif()
})

function load_gif(){
    $.ajax({
        type: "GET",
        url: "/loadimage",
        data: {},
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert('피드 불러오기!')
            data = response['find_gif']
            console.log(data)
        }
    })
}