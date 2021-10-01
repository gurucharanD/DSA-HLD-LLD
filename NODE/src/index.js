express = require('express')
Parser = require ('body-parser')
const app = express()
require('dotenv').config()

Bootstrap=require('./db');

console.log(Bootstrap)




app.use(Parser.json({ limit: '50mb' }))

app.use(Parser.urlencoded({ limit: '50mb',
  extended: true }))


  app.use((req, res, next) => {
    res.set('Content-Type', 'application/json')
    next()
  })

  require('./routes')(app)



//   app.get('/',(req,res)=>{
//     res.send("hi broh");
//   })


const dBBootstrap = (async () => {
  try {
    await Bootstrap.run()

  } catch (e) {
    console.log('Error bootstraping the database. --> exception -->', e.message, e)
    app.set('HEALTH_STATUS', 'DB_MIGRATION_FAILED')
    throw e
  }
})

dBBootstrap().then(
  console.log('Db bootstrapped')
  )







app.listen(3000, () => console.log(`Example app listening on port`))
