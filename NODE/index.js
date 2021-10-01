// import express from 'express'
// import Parser from 'body-parser'



// express = require('express')
// Parser = require ('body-parser')
// const app = express()

// app.use(Parser.json({ limit: '50mb' }))

// app.use(Parser.urlencoded({ limit: '50mb',
//   extended: true }))


//   app.use((req, res, next) => {
//     res.set('Content-Type', 'application/json')
//     next()
//   })

//   app.get('/',(req,res)=>{
//     res.send("hi broh");
//   })


//   app.listen(3000, () => console.log(`Example app listening on port`))



  const env = process.env.NODE_ENV = process.env.NODE_ENV || 'development';
if (env === 'production') {
  module.export = require('./dist/');
} else {
  //  require('@babel/register');
  module.export = require('./src');
}
