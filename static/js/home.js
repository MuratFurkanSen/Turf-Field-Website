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