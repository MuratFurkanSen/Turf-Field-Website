var homeReservation = document.querySelector(".homeReservation");
var closeSign = document.querySelector(".closeSign");
var homeLog = document.querySelector(".homeLog");
var closeLog = document.querySelector(".closeLog");
var homeCreateTeam = document.querySelector(".takimOlusturButonu");
var closeCreateTeam = document.querySelector(".closeCreate");
let boolLog = false;
let boolCreateTeam = false;


homeLog.addEventListener("click", function() {
    if (!boolCreateTeam){
        boolLog = true;
        document.querySelector(".login-container").style.display = "block";
    }
    else {
        boolCreateTeam = false;
        boolLog = true;
        document.querySelector(".create-team-button").style.display = "none";
        document.querySelector(".login-container").style.display = "block";
    }

})

closeLog.addEventListener("click", function() {
    boolLog = false;
    document.querySelector(".login-container").style.display = "none";
})

homeCreateTeam.addEventListener("click", function() {
    if (!boolLog){
        boolCreateTeam = true;
        document.querySelector(".create-team-button").style.display = "block";
    }
    else {
        boolLog = false;
        boolCreateTeam = true;
        document.querySelector(".login-container").style.display = "none";
        document.querySelector(".create-team-button").style.display = "block";
    }
})

closeCreateTeam.addEventListener("click", function() {
    boolCreateTeam = false;
    document.querySelector(".create-team-button").style.display = "none";
})
