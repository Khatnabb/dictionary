function alert(top_message = 'Successful', message = 'Success', icon = 'success'){
    Swal.fire(top_message,
              message,
              icon)
            }

function alert_info(message = "info"){
    var contribute = "Please click here to contribute"
    var tocontribute = contribute.link('http://localhost:5000/contribute')
    Swal.fire("Word Not Found ", message + "<BR>" +  tocontribute, "info")
}

function flag_toggle() {
    var x = $(".lang-menu option:selected").text();
if (x === "EN-MN") {
    $('.eng-flag').show();
    $('.mng-flag').hide();
} else {
    $('.eng-flag').hide();
    $('.mng-flag').show();
}};