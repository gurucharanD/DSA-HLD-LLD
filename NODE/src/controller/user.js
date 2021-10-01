var uuid = require('uuid/v4');
var knex = require('../db/knex');
    module.exports. buildRoutes=  ( router )=> {

        router.get('/',(req,res)=>{
        res.send("plz login");
        });
        
        router.post('/',async(req,res)=>{
        console.log('body', req.body)

    try{

        var test = await knex('loginuser').insert({ Name: req.body.user, password: req.body.password, loginuser_guid: uuid()});
        // var test = await knex.raw(`insert into sravanproject.loginuser (Name,password,loginuser_guid) values ('user','user','1')`)
        res.send({"test": test});
    }
    catch(err){
        console.log(err);
    }
        });
    }
