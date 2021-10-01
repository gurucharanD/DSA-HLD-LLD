const accountSid = 'ACf909a7063de793cb3d90e6abc4c2177c';
const authToken = 'c3aa204bf587e27428838a8c439acf0d';
const client = require('twilio')(accountSid, authToken);

client.messages
  .create({
    body: 'Hello there!',
    from: 'whatsapp:+917036680050',
    to: 'whatsapp:+918142633108'
  })
  .then(message => console.log(message.sid))
  .done();