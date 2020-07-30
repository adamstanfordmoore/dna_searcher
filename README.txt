Branch for deployment on heroku:


deploy docker container:
heroku login
heroku container:login
heroku container:push web -a enigmatic-temple-51399
heroku container:release web -a enigmatic-temple-51399
heroku open


or build on heroku:

git push heroku main





Now deployed to heroku at https://enigmatic-temple-51399.herokuapp.com
First turn on dyno at https://dashboard.heroku.com/apps/enigmatic-temple-51399/resources