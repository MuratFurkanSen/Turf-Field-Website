function addMember(team_id){
    user_id = document.getElementById("userIdInput").value;
    window.location.href = `${team_id}/edit_team/add/${user_id}`;
}