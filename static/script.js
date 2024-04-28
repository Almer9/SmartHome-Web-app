function toggleLight(room){
    lightElement = document.getElementById(room+"lightimg")
    console.log(room)
    $.ajax({
        url: `/${room}/light/toggle`,
        type: 'GET',
        success: function(response) {
            console.log(response)
            if(response.state){
                lightElement.src = "static/light-bulb-on.png"
            }
            else{
                lightElement.src = "static/light-bulb.png"
            }
    },
    error: function (jqXHR, exception){
        console.log(jqXHR,exception)
    }
    })

}
function changeBrightness(room){
    lightBrightness = document.getElementById(room+"Brightness")
    brightnessField = document.getElementById(room+"brightnessfield")
    serverData = {
        'brightness': brightnessField.value
    }
    if (brightnessField.value > 0 && brightnessField.value <=100){
    $.ajax({
        url: `/${room}/light/brightness`,
    type: 'POST',
    data: serverData,
    success: function(response) {
        lightBrightness.innerText = `Brightness: ${response.brightness}`
        brightnessField.value = ""
    }
    })
    }


}
function toggleTemp() {
    $.ajax({
        url: '/none/temp/update',
        type: 'GET',
        success: function(response) {
            var elements = document.querySelectorAll('.temp');
            elements.forEach(function(element) {
                element.innerText =`Temp: ${response[element.id].toFixed(2)}`
            });
        }
    });
}