from flask import Flask,jsonify,request
import pandas as pd

animes_data = pd.read_csv('anime.csv')

app = Flask(__name__)

allanimes = animes_data[["name","genre","episodes","rating","type"]]

likedanimes=[]
dislikedanimes=[]
watchlateranimes=[]

def animesdetails():
    anime_data={"name":allanimes.iloc[0,0],"genre":allanimes.iloc[0,1],"episodes":allanimes.iloc[0,2],"rating":allanimes.iloc[0,3],"type":allanimes.iloc[0,4]}
    return anime_data

@app.route("/gettheanimes",methods=["GET"])
def getanimes():
    animesname=animesdetails()
    
    return jsonify({
        "data":animesname,
        "status":"success"
    })

@app.route("/liked")
def likeanimes():
    global allanimes
    animes=animesdetails()
    likedanimes.append(animes)

    allanimes.drop([0],inplace=True)
    allanimes=allanimes.reset_index(drop=True)
    return jsonify({
        "status":"success"
    }) 
@app.route("/disliked")
def dislikeanimes():
    global allanimes
    animes=animesdetails()
    dislikedanimes.append(animes)

    allanimes.drop([0],inplace=True)
    allanimes=allanimes.reset_index(drop=True)
    return jsonify({
        "status":"success"
    }) 

@app.route("/watchlater")
def watchedlateranimes():
    global allanimes
    animes=animesdetails()
    watchlateranimes.append(animes)

    allanimes.drop([0],inplace=True)
    allanimes=allanimes.reset_index(drop=True)
    return jsonify({
        "status":"success"
    }) 
app.run()