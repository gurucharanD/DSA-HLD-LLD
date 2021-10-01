import { Router } from 'express'
const router = new Router()

// var express = require('express')
// var router = express.Router();




import { Users } from '../controllers'
// Users = require('../controller');

// const controller = new Users()
Users.buildRoutes(router)
// console.log(Users)



router.get('/', (req, res) => {
    res.send("plz login");
});



router.post('/', (req, res) => {
    var body = req.body
    res.send("welcome" + body.user);
})



// export default router
module.exports = router;