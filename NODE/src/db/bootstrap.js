knex = require('./knex')


const run=async () => {
    if (process.env.NODE_ENV === 'development' || process.env.NODE_ENV === 'test') {
        let isDBUp = false;
        let response;
        console.log('Checking DB connectivity...');
        do {
          try {
            await new Promise((resolve) => {
              console.log('waiting for 1000!!!', new Date());
              setTimeout(() => {
                console.log('waited for 1000!!!', new Date());
                resolve(true);
              }, 1000);
            });
            //console.log(knex)
            response = await knex.raw('select 1+1 as result');
            isDBUp = parseInt((JSON.parse(JSON.stringify(response)))[0][0]['result'], 10) === 2;
          } catch (ex) {
            console.log('DB connectivity failed!!!');
          }
        } while (!isDBUp);
        console.log('DB is up and running. DB is connected!!!');
      }
    try {
    await runMigrations()
    } catch(e){
        console.log('migrations',e)
    }
}

const runMigrations= async () => {
    try {
        console.log('running migrations')
        await knex.migrate.latest()
        console.log('running migrations complete.')
    } catch (err) {
        console.error('running migrations failed. See Log.child.errorMessage.',err)
        throw err
    }

}

module.exports={run,runMigrations}