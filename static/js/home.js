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

const home = document.querySelector(".home"),
    formContainer = document.querySelector(".form_container"),
    signupBtn = document.querySelector("#signup"),
    loginBtn = document.querySelector("#login"),
    pwShowHide = document.querySelectorAll(".pw_hide");


function loginOpen(){
    home.classList.add("show");

}

function loginClose(){
    home.classList.remove("show");
}

function handleSignup(e) {
    e.preventDefault(); // Varsayılan davranışı engelle
    formContainer.classList.remove("active"); // "active" sınıfını ekle
}

function handleLogin(e) {
    e.preventDefault(); // Varsayılan davranışı engelle
    formContainer.classList.add("active"); // "active" sınıfını ekle
}

pwShowHide.forEach((icon) => {
    icon.addEventListener("click", ()=> {
        let getPwInput = icon.parentElement.querySelector(("input"));
        if (getPwInput.type === "password") {
            getPwInput.type = "text";
            icon.classList.replace("uil-eye-slash", "uil-eye");
        }else{
            getPwInput.type = "password";
            icon.classList.replace("uil-eye", "uil-eye-slash");
        }
    });

});






function createTeamButton() {
    document.querySelector(".homeForum").style.display = "block";
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



const swiper = new Swiper('.slider-wrapper', {
    loop: true,
    grabCursor: true,
    spaceBetween: 10,

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullet: true,
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    breakpoints: {
        0:{
            slidesPerView: 1,
        },
        620:{
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        }

    }

})




const playerTeam = document.querySelectorAll('.playerButton');




let newX = 0, newY = 0, startX = 0, startY = 0;
let currentButton = null; // Hangi butonun sürüklendiğini takip etmek için


playerTeam.forEach(button => {
    button.addEventListener('mousedown', (e) => mouseDown(e, button)); // her bir buton için mousedown olayı ekle
});

function mouseDown(e, button) {
    currentButton = button; // Sürüklenen butonu belirle
    startX = e.clientX;
    startY = e.clientY;

    document.addEventListener('mousemove', mouseMove); // document üzerinde mousemove olayını dinle
    document.addEventListener('mouseup', mouseUp); // document üzerinde mouseup olayını dinle
}

function mouseMove(e) {
    if (currentButton) {
        newX = startX - e.clientX;
        newY = startY - e.clientY;

        startX = e.clientX;
        startY = e.clientY;

        currentButton.style.top = (currentButton.offsetTop - newY) + 'px';
        currentButton.style.left = (currentButton.offsetLeft - newX) + 'px';
    }
}

function mouseUp() {
    document.removeEventListener('mousemove', mouseMove); // mousemove olayını dinlemeyi bırak
    document.removeEventListener('mouseup', mouseUp); // mouseup olayını dinlemeyi bırak
    currentButton = null; // Sürükleme işlemi tamamlandığında butonu sıfırla
}
