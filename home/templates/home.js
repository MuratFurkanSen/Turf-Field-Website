var homeButton = document.querySelector(".homeButton");
var homeReservation = document.querySelector(".homeReservation");
var homeTeam =  document.querySelector(".homeTeam");
var homeUser = document.querySelector(".homeUser");


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
