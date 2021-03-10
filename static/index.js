$(document).ready(function () {

$('.message').hide()
$('.results1').hide()
$('.results2').hide()
$('.results3').hide()

let myVar = $('.message')
let myValue = parseInt(myVar[0].attributes[1].nodeValue)

if (myValue === 502) {
    console.log('No stocks found')
    $('.message').show()
    $('.results1').hide()
    $('.results2').hide()
    $('.results3').hide()
} else {
    $('.results1').show()
    $('.results2').show()
    $('.results3').show()
}

})