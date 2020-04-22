const express=require('express');
const {spawn} = require('child_process')
const axios=require('axios');
app=express()
var response;
var currentData={temperature:"",description:""}
var predictions={maxTemp:"",minTemp:"",humidity:""}
var weatherData;
app.get("/getPrediction",(req,res)=>{
    console.log("request sent")
    const python = spawn('python', ['MultiTargetRegr.py'])
    python.stdout.on('data', function (data) { 
        console.log(data.toString());
        response=data.toString().split(' ');
        currentData.temperature=response[0]
        currentData.description=response[1]+response[2];
        predictions.maxTemp=response[3];
        predictions.minTemp=response[4];
        predictions.humidity=response[5];
        console.log(currentData,predictions)
        weatherData={currentData:currentData,predictions:predictions};
        res.send(weatherData)
       });     
})

app.listen('5000',console.log("listening to port 5000"));