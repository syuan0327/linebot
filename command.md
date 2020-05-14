heroku login
git init
heroku git:remote -a '你的Heroku所設的App名稱'
git add .
git commit -m "Add code"
git push heroku master

