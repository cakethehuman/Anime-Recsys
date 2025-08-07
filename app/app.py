from flask import Flask, request, render_template 
from rec import get_recommendations
# Flask constructor
app = Flask(__name__)   

@app.route('/')
def index():
    return render_template(r'index.html')
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def getting_anime():
   if request.method == "POST":
      watch_list = []
      anime_name = request.form.get("anim")
      df = get_recommendations(anime_name, 5)
      
      for index,anime in enumerate(df["Anime Title"], start=1):
         watch_list.append(str(f"{index} ': ' {anime}"))
         
      answer = "you should watch these :" + str(watch_list)
   return render_template("index.html", anime_end = answer)
#Cowboy Bebop

if __name__=='__main__':
   app.run()