const daysTags = document.querySelectorAll(".days"),
    currentDates = document.querySelectorAll(".current-date"),
    prevNextIcon = document.querySelectorAll(".icons span");

// getting new date, current year and month
let date = new Date(),
    currYear = date.getFullYear(),
    currMonth = date.getMonth();

// storing full name of all months in array
const months = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"];

const renderCalendar = (daysTag, currentDate) => {

    let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(), // getting first day of month
        lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(), // getting last date of month
        lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(), // getting last day of month
        lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate(); // getting last date of previous month
    let liTag = "";
    for (let i = firstDayofMonth; i > 0; i--) { // creating li of previous month last days
        liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) { // creating li of all days of current month
        // adding active class to li if the current day, month, and year matched
        let isToday = i === date.getDate() && currMonth === new Date().getMonth()
        && currYear === new Date().getFullYear() ? "selected" : "";

        liTag += `<li class="active ${isToday}" data-title="${i}">${i}</li>`;
    }

    for (let i = lastDayofMonth; i < 6; i++) { // creating li of next month first days
        liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`
    }
    currentDate.innerText = `${months[currMonth]} ${currYear}`; // passing current mon and yr as currentDate text


    daysTag.innerHTML = liTag;
    Array.from(daysTag.getElementsByClassName("active")).forEach((item) => {
        item.addEventListener("click", () => {
            daysTag.getElementsByClassName("selected")[0].classList.remove("selected");
            item.classList.add("selected");

            let facility_id = item.parentElement.parentElement.parentElement.parentElement.parentElement.dataset.facilityId;
            console.log(facility_id);
            let field_id = document.getElementById(`field_select_${facility_id}`).value;
            fetch(`/reservation/get_reservation_options?field_id=${field_id}&selected_date=${currYear}-${currMonth + 1}-${item.innerText}`)
                .then(response => response.json())
                .then(data => {
                    let parent = item.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector("#Anan");
                    parent.innerHTML = "";
                    data.date_options.forEach((hour) => {
                        let new_button = document.createElement("button");
                        new_button.textContent = `${hour}:00-${Number(hour) + 1 === 24 ? "00" : String(Number(hour) + 1)}:00`;
                        new_button.addEventListener("click", () => {
                            let team_id = document.getElementById("Cool").value
                            window.location.href = `/reservation/create?field_id=${field_id}&team_id=${team_id}&selected_date=${currYear}-${currMonth + 1}-${item.innerText}-${hour}`;
                        });
                        parent.appendChild(new_button);
                    });
                    let new_select = document.createElement("select");
                    new_select.id = "Cool"
                    data.team_options.forEach((team) => {
                        let pieces = team.split(',');

                        let new_option = document.createElement("option");
                        new_option.value = pieces[0];
                        new_option.textContent = pieces[1];
                        new_select.appendChild(new_option);
                    });
                    parent.appendChild(new_select);

                });
        });
    });

}
document.querySelectorAll('.denemeli').forEach(element => {
    element.addEventListener('change', () => {
        document.querySelector('#Anan').innerHTML = "";
    });
});
for (let i = 0; i < daysTags.length; i++) {
    renderCalendar(daysTags[i], currentDates[i]);
}
prevNextIcon.forEach(icon => {
    // getting prev and next icons
    icon.addEventListener("click", () => { // adding click event on both icons
        // if clicked icon is previous icon then decrement current month by 1 else increment it by 1
        currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

        if (currMonth < 0 || currMonth > 11) { // if current month is less than 0 or greater than 11
            // creating a new date of current year & month and pass it as date value
            date = new Date(currYear, currMonth, new Date().getDate());
            currYear = date.getFullYear(); // updating current year with new date year
            currMonth = date.getMonth(); // updating current month with new date month
        } else {
            date = new Date(); // pass the current date as date value
        }
        let daysTag = icon.parentElement.parentElement.parentElement.getElementsByClassName("days")[0];
        let currentDate = icon.parentElement.parentElement.getElementsByClassName("current-date")[0];
        renderCalendar(daysTag, currentDate); // calling renderCalendar function
    });
});
