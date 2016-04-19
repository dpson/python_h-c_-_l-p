from flask import Flask, render_template
from mongoengine import *
import requests

connect("c4e3", host= "mongodb://admin:admin@ds015919.mlab.com:15919/c4e3")
app = Flask(__name__)
class Movie(Document):
    title = StringField()
    img = StringField()
# movie = Movie(title= "Spiderman Son",
#               img= " http://kinhtenongthon.com.vn/data/data/diepbachle/2016/Thang03/18/rung%20ngapman.jpg")
# movie.save()
movies =  restaurants.objects
@app.route('/')
def hello_world():
    return 'Hello World!'
class Movies:
   def __index__(self, title,img):
       self.title = title
       self.img = img
for movie in movies:
    @app.route('/movie_2/<movie_idx>')
    def get_movie_2(movie_idx):
        return render_template("web_3.html", movies=movie)


    if __name__ == '__main__':
        app.run()


