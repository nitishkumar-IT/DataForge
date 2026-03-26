function showPage(id){

document

.querySelectorAll(".page")

.forEach(

p=>p.classList.remove("active")

)

document

.getElementById(

"page-"+id

)

.classList.add("active")

}

function setStatus(text){

document

.getElementById(

"status-chip"

).innerText=text

}