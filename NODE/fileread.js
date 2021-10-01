/* import fs from 'fs';
 */const fs=require('fs');

/* export const Router = {
 */ 
    const routes = fs.readdirSync(__dirname)
      .filter(file => {
		  file !== 'index.js'
	  })
      .filter(file => {
		  file.match(/^(?!.*\.test\.js$).*\.js$/)
	  })
      .map(file => {
	  file.split('.')[0]
	  });
	  console.log(routes)

    /* routes.forEach(route => {
      app.use(`/${route}`, this.importSubRouter(`./${route}.js`));
    });
  
  importSubRouter(filePath) {
    return require(filePath);
  } */
/* }; */
