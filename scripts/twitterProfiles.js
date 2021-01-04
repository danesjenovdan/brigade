var Twitter = require('twitter');
fs = require('fs');

const arr = [
  "karolinasemjaz"
];

var client = new Twitter({
    consumer_key: process.env.consumer_key,
    consumer_secret: process.env.consumer_secret,
    bearer_token: process.env.bearer_token,
    //access_token_secret: 'hA1XykBywJrSL4JFEDvHsyPs5WRczuRlL0ucG6dyBzwoi'
});

const func = async (screen_name) => {
  const params = {screen_name};
  await client.get('users/show', params, function(error, user, response) {
    console.log('error: ', error);
    if(!error) {
      fs.readFile("trolls/"+screen_name+".json", (err, data) => {
       const trollData = !err || err !== null ? JSON.parse(data) : {};
       trollData.accountInfo = {
         name: user.name,
         followers: user.followers_count,
         following: user.friends_count,
         location: user.location,
         created: user.created_at,
         tweets: user.statuses_count,
         imageUrl: user.profile_image_url_https
       }
           fs.writeFile("trolls/"+screen_name+"info"+".json", JSON.stringify(trollData), function (err) {
             console.log('write: ', screen_name);
             if (err) return console.log(err);
              return 0
           });
       });
    }
   });
}

 (async () => {
   for (screen_name of arr) {
   screen_name = screen_name.toLowerCase()
   await delay(1000)
   await func(screen_name)
   }
 })()

 function delay(t, val) {
  return new Promise(function(resolve) {
      setTimeout(function() {
          resolve(val);
      }, t);
  });
}