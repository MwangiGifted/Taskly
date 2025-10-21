// var message_timeout = document.getElementById('message-timer');


// setTimeout(function() 

// {

//     message_timeout.style.display = 'none';

// }, 5000);

// document.addEventListener('DOMContentLoaded', function () {

//     var messages = document.querySelectorAll('.message-timer');
//     setTimeout(function() {
//         messages.forEach(function(msg) {
//             msg.style.display = 'none';
//         });
//     }, 3000); // hides after 5 seconds
// });

// document.addEventListener('DOMContentLoaded', function() {
//     const messageTimeout = document.querySelector('.message-timer');
//     if (messageTimeout) {
//         setTimeout(() => {
//             messageTimeout.style.display = 'none';
//         }, 3000); // hides after 3 seconds
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    var messages = document.querySelectorAll('.message-timer');
    setTimeout(function() {
        messages.forEach(function(msg) {
            msg.style.transition = 'opacity 0.5s ease';
            msg.style.opacity = '0';
            setTimeout(() => msg.style.display = 'none', 500);
        });
    }, 3000);
});





