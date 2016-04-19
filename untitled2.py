from flask import Flask,render_template
app = Flask(__name__)
import requests

@app.route('/')
def hello_world():
    return 'Hello World!'
class Movie:
   def __index__(self, title,img):
       self.title = title
       self.img = img
       self.href = ""
movies = [
    Movie("Batman",
          "http://vignette2.wikia.nocookie.net/batman/images/4/4a/BatmanChristianBale.jpg/revision/latest?cb=20080223195115",
          ),
    Movie("Superman",
          "http://wegotthiscovered.com/wp-content/uploads/man-of-steel-review-579x360.jpg"),
    Movie("Nivea",
          "http://www.beiersdorf.vn/~/media/Beiersdorf/brands/teaser/NIVEA-Product-Beiersdorf.png"),
         ]
@app.route('/movie/<movie_idx>')
def get_movie(movie_idx):
    index = int(movie_idx)
##    return render_template("web_an.html,title=movies[index].title,img=movies[index].img")
    if index in range(len[movies]):
        return render_template("web_an.html,title=movies[index].title,img=movies[index].img ")
    return "<h1>Movie not found<h1>"
@app.route('/movie_2/<movie_idx>')
def get_movie_2(movie_idx):
    index = int(movie_idx)
    if index in range(len(movies)):
        return render_template("web_2.html", movie=movies[index])
    return "<h1>Movie not found<h1>"
if __name__ == '__main__':
    app.run()




