var homeButton = document.querySelector(".homeButton");
var homeReservation = document.querySelector(".homeReservation");
var homeTeam =  document.querySelector(".homeTeam");
var homeUser = document.querySelector(".homeUser");
var homeSign = document.querySelector(".homeSign");
var closeSign = document.querySelector(".closeSign");
var homeLog = document.querySelector(".homeLog");
var closeLog = document.querySelector(".closeLog");
var homeCreateTeam = document.querySelector(".takimOlusturButonu");
var closeCreateTeam = document.querySelector(".closeCreate");


homeButton.addEventListener("click", function() {
    window.location.href = "http://localhost:8000/home";
})

homeReservation.addEventListener("click", function() {
    window.location.href = "http://localhost:8000/reservation";
})

homeTeam.addEventListener("click", function() {
    window.location.href = "http://localhost:8000/team";
})

homeUser.addEventListener("click", function() {
    window.location.href = "http://localhost:8000/user";
})


homeSign.addEventListener("click", function() {
    document.querySelector(".sign-container").style.display = "block";

})


closeSign.addEventListener("click", function() {
    document.querySelector(".sign-container").style.display = "none";
})

homeLog.addEventListener("click", function() {
    document.querySelector(".login-container").style.display = "block";
})

closeLog.addEventListener("click", function() {
     document.querySelector(".login-container").style.display = "none";
})

homeCreateTeam.addEventListener("click", function() {
    document.querySelector(".create-team-button").style.display = "block";
})

closeCreateTeam.addEventListener("click", function() {
     document.querySelector(".create-team-button").style.display = "none";
})
