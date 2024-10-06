let boolLog = false;
let boolCreateTeam = false;
let boolSign = false;

function homeLog(){
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

}