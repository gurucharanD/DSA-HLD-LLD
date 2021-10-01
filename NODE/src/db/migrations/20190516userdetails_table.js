exports.up = function (knex, Promise) {
    return Promise.all(
      [
      knex.schema.hasTable('loginuser').then(async (isTableExist) => {
        if (!isTableExist) {
        console.log('here at table creation started')
          await knex.schema.createTable('loginuser', table => {
            table.uuid('loginuser_guid').primary().defaultTo(null)
            table.string('Name')
            table.string('password')
            table.dateTime('created_date').defaultTo(knex.fn.now())
            table.dateTime('modified_date')
            table.dateTime('deleted_date')
          console.log('here at table creation end')
          });
        }
        console.log('here at before return true')
        return true;
      })
    ]);
  };
  exports.down = function (knex, Promise) {
    return Promise.resolve(true);
  };
  































