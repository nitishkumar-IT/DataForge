const API="https://dataforge-p8nc.onrender.com/"

async function apiUpload(file){

let form=new FormData()

form.append("file",file)

let res=

await fetch(

API+"/upload",

{

method:"POST",

body:form

}

)

return res.json()

}

async function apiClean(){

let res=

await fetch(

API+"/clean",

{

method:"POST"

}

)

return res.json()

}

async function apiEDA(){

let res=

await fetch(

API+"/eda"

)

return res.json()

}

async function apiTrain(target){

let res=

await fetch(

API+"/train",

{

method:"POST",

headers:

{

"Content-Type":"application/json"

},

body:

JSON.stringify({

target:target

})

}

)

return res.json()

}

async function apiPredict(data){

let res=

await fetch(

API+"/predict",

{

method:"POST",

headers:

{

"Content-Type":"application/json"

},

body:

JSON.stringify({

data:data

})

}

)

return res.json()

}