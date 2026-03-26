let chart=null

function createChart(labels,data){

let ctx=

document.getElementById(

"main-chart"

)

if(chart){

chart.destroy()

}

chart=new Chart(

ctx,

{

type:"bar",

data:

{

labels:labels,

datasets:[

{

data:data

}

]

}

}

)

}