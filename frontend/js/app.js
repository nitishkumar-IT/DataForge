let currentFile=null

async function handleFileUpload(e){

let file=e.target.files[0]

if(!file)return

currentFile=file

setStatus("Uploading")

let res=

await apiUpload(file)

console.log(res)

setStatus("Uploaded")

alert("Dataset uploaded")

}

async function runClean(){

setStatus("Cleaning")

let res=

await apiClean()

console.log(res)

setStatus("Clean complete")

alert("Cleaning done")

}

async function runEDA(){

setStatus("Analyzing")

let res=

await apiEDA()

console.log(res)

setStatus("EDA ready")

alert("EDA ready")

}

async function trainModel(){

setStatus("Training")

let res=

await apiTrain()

console.log(res)

setStatus("Model trained")

alert(

"Accuracy: "+

res.accuracy

)

}

async function predict(){

let values=[

25,

3,

70000

]

let res=

await apiPredict(

values

)

console.log(res)

alert(

"Prediction: "+

res.prediction

)

}