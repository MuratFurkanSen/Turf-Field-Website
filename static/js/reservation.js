function filterCities() {
    var input, filter, div, txtValue;
    input = document.getElementById('search');
    filter = input.value.toUpperCase();
    div = document.querySelectorAll('.dropdown-content div');

    for (var i = 0; i < div.length; i++) {
        txtValue = div[i].textContent || div[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "";
        } else {
            div[i].style.display = "none";
        }
    }
}

function selectCity(city) {
    document.getElementById('selected-city').innerText = city;
}
