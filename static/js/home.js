function homeLog(){
        document.querySelector(".user-container").style.display = "block";
        document.getElementById("loginForm").style.display = "block";
}
function getRegisterForm(){
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("registerForm").style.display = "block";
}
function getLoginForm(){
        document.getElementById("registerForm").style.display = "none";
        document.getElementById("loginForm").style.display = "block";
}

function xButtonCloseLogHome() {
        document.querySelector(".user-container").style.display = "none";
        document.getElementById("registerForm").style.display = "none";
        document.getElementById("loginForm").style.display = "none";
}

let teamClickCounter = 0;

document.querySelector('.createTeamHover').addEventListener('click', function() {
    teamClickCounter += 1;
    if (teamClickCounter % 2 === 0) {
        document.querySelector('.homeForum').style.display = 'none';
    }
    else {
        document.querySelector('.homeForum').style.display = 'block';
    }
});


document.querySelector('.mainPhoto').addEventListener('click', function() {
    document.querySelector('.homeCards').style.visibility = 'visible';
});


document.querySelector('.iconPhoto').addEventListener('click', function() {
    document.querySelector('.homeCards').style.visibility = 'hidden';
});
