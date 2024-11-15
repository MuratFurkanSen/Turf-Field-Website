function homeLog() {
    document.querySelector(".user-container").style.display = "block";
    document.getElementById("loginForm").style.display = "block";
}

function getRegisterForm() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("registerForm").style.display = "block";
}

function getLoginForm() {
    document.getElementById("registerForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}

function xButtonCloseLogHome() {
    document.querySelector(".user-container").style.display = "none";
    document.getElementById("registerForm").style.display = "none";
    document.getElementById("loginForm").style.display = "none";
}

function waitingReservationOnClick() {
    document.querySelector(".paymentTeam").style.display = 'block';
}

function homecardOpen() {
    document.querySelector('.homeCards').style.visibility = 'visible';
}

function homecardClose() {
    document.querySelector('.homeCards').style.visibility = 'hidden';
}

function toggleButton(button) {
    button.classList.toggle("active");
}

function scrollDown() {
    window.scrollBy({
        top: 200, // Y ekseninde 20px kaydırır
        left: 0, // X ekseninde 0 kaydırır
        behavior: 'smooth' // Yumuşak kayma efekti
    });
}

function xButtonClosePayment() {
    document.querySelector(".paymentTeam").style.display = "none";
}

function voteScreen(){
    document.querySelector('.homeCards1').style.visibility = 'visible';
}
function voteScreenClose() {
    document.querySelector('.homeCards1').style.visibility = 'hidden';
}


let teamClickCounter = 0;

document.querySelector('.createTeamHover').addEventListener('click', function () {
    teamClickCounter += 1;
    if (teamClickCounter % 2 === 0) {
        document.querySelector('.homeForum').style.display = 'none';
    } else {
        document.querySelector('.homeForum').style.display = 'block';
    }
});



