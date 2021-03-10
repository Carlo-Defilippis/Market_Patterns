$(document).ready(function () {

$('.message').hide()
$('.results').show()

let myVar = $('.message')
let myValue = parseInt(myVar[0].attributes[1].nodeValue)

if (myValue === 502) {
    console.log('No stocks found')
    $('.message').show()
    $('.results').hide()
} 

})