from flask import Flask, request, render_template, url_for,redirect
import os
import json
import time

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")
 #   return "Hello World!"

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/javascript")
def hello():
    return render_template("javahello.js")

@app.route("/successful", methods=["POST"])
def displa():
    name = request.form.get("dispy")
    print(f"User entered:'{name}'")
    with open("testUserInputstore.txt","a") as fo:
        fo.write(str(name))
        fo.write("\n")
    time.sleep(5)
    return redirect(url_for("homepage"))
 #   return "Successfully captured user input and saved!!"
 
@app.route("/get", methods=["GET"])
def get_Imag():
    import requests
    url = "http://shelysafrica.com/images/Regional-heads/AdvaniSa.jpg"
    response = requests.get(url)
    headers = response.headers
    header_type = headers.get('content-type')
    Image = response.content
    status = response.status_code
    print(f"Status: {response.status_code}")
    with open("downloadedImage.jpg","wb") as im:
        im.write(Image)
        
    with open("downloadedImage.jpg","rb") as imgIn:
        readImage = imgIn.read()
        #print(readImage)
        return readImage

# post to the browser
@app.route("/read",methods=["GET"])
def readi():
    with open("testUserInputstore.txt","r") as stre:
        openn = stre.readlines()

        data = json.dumps(openn).split(', ',30)

        return render_template("home.html", data=data)

''' delete from list/ Opted
@app.route("/remove", methods=["POST"])
def remove():
    deleteUserWithName = request.form.get("deletUserName")

#    with open("testUserInputstore.txt","r") as rem:
#        removee = rem.readlines()
#        remo = json.dumps(removee)

    for i in deleteUserWithName:
        i = " "
        print(f"Username '{deleteUserWithName}' has been deleted!")
    return redirect(url_for("homepage"))
'''
@app.route("/date", methods=["GET"])
def displayTime():
    import datetime
    class Showdate:
        '''To show date on the browser'''
        def __init__(self,thedateT):
            self.date = thedateT
        def __repr__(self):
            return f"{self.date}"
    dateANDtime = Showdate(datetime.date.today())
    print(isinstance(dateANDtime,Showdate))
    print(dateANDtime.date)
    print(dateANDtime.__repr__())

    return render_template("home.html", dateANDtime=dateANDtime)


if __name__ == "__main__":
    localhost = "127.0.0.1" or "::"
    app.run(
        host = localhost,
        debug = True
        )
