from flask import Flask, render_template, url_for, redirect, request, session, flash
import requests

app = Flask(__name__)

app.secret_key = 'abcd1234'

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/exhibition")
def exhibition():
        # Ambil data dari API
        try:
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/exhibition')
        except Exception as e:
            print("ERROR | Get exhibition data |", e)

        return render_template("exhibition.html", exhibition=data.json())

@app.route("/collection")
def collection():
     # Ambil data dari API
        try:
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/collection')
        except Exception as e:
            print("ERROR | Get collection data |", e)

        return render_template("collection.html", collection=data.json())

@app.route("/blog-detail")
def blog_detail():
    return render_template("blog-detail.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Ambil data dari API
        try:
            users = requests.get(
                'https://backend-petra-5zn7xh2gqq-et.a.run.app/getuser')
            # users = requests.get(
            #     'http://127.0.0.1:5000/users')
        except Exception as e:
            print("ERROR | Get products data |", e)

        for user in users.json():
           if user["username"] == username:
                if password == user['password']:
                    session["user"] = user["username"]

                    return redirect(url_for('admin_home'))
        error = "Username atau Password tidak valid!"

    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

@app.route("/admin", methods=['GET'])
def admin_home():
    if "user" in session:
        # Ambil data dari API
        try:
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/collection')
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/exhibition')
        except Exception as e:
            print("ERROR | Get collection data |", e)
        return render_template("admin-home.html", user=session["user"], collection=data.json(), exhibition=data.json())
    else:
        return redirect(url_for('login'))

@app.route("/admin-collection", methods=['GET'])
def admin_collection():
    if "user" in session:
        # Ambil data dari API
        try:
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/collection')
        except Exception as e:
            print("ERROR | Get collection data |", e)

        return render_template("admin-collections.html", user=session["user"], collection=data.json())
    else:
        return redirect(url_for('login'))
     
    
@app.route("/admin-exhibition", methods=['GET'])
def admin_exhibition():
    if "user" in session:
        # Ambil data dari API
        try:
            data = requests.get('https://backend-petra-5zn7xh2gqq-et.a.run.app/exhibition')
        except Exception as e:
            print("ERROR | Get exhibition data |", e)

        return render_template("admin-exhibitions.html", user=session["user"], exhibition=data.json())
    else:
        return redirect(url_for('login'))

@app.route("/add-collection", methods=['GET','POST'])
def add_collection():
        #if "user" in session:
                
                title = request.form['title']
                artist = request.form['artist']
                img = request.form['img']

                requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/addcollection', json=(title, artist, img))
        
                return redirect(url_for('admin_collection'))
        #else:
            #return redirect(url_for('login'))
        
@app.route("/admin/addcollectionpage", methods=['GET'])
def addcollectionpage():
    #if "user" in session:
        return render_template("add-collection.html", user=session["user"])
    #else:
       # return redirect(url_for('login'))
   
@app.route("/add-exhibition", methods=['GET', 'POST'])
def add_exhibition():
        if "user" in session:  
                id_exhibition = request.form['id_exhibition']
                name = request.form['name']
                description = request.form['description']
                img = request.form['img']

                requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/addexhibition', json=(id_exhibition, name, description, img))
        
                return redirect(url_for('admin_exhibition'))
        else:
            return redirect(url_for('login'))
        
@app.route("/admin/addexhibitionpage", methods=['GET'])
def addexhibitionpage():
    if "user" in session:
        return render_template("add-exhibition.html", user=session["user"])
    else:
        return redirect(url_for('login'))

@app.route("/admin/delete<id_collection>", methods=['GET','POST'])
def deletecollection(id_collection):

    requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/deletecollection', json=(id_collection))
    
    return redirect(url_for('admin_collection'))

@app.route("/admin/delete2<id_exhibition>", methods=['GET','POST'])
def deleteexhibition(id_exhibition):

    requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/deleteexhibition', json=(id_exhibition))
    
    return redirect(url_for('admin_exhibition'))

@app.route("/admin/collection<id_collection>", methods=['GET','POST'])
def editcollectionpage(id_collection):

    if "user" in session:
        data = requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/selectcollection', json=(id_collection))
    

        return render_template("edit-collection.html", collection=data.json(), user=session["user"])
    else:
        return redirect(url_for('login'))
    

@app.route("/admin/update<id_collection>", methods=['GET','POST'])
def update_collection(id_collection):
    if "user" in session:
        if request.method == 'POST':
                title = request.form['title']
                artist = request.form['artist']
                urlimg = request.form['urlimg']
                

                requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/updatecollection', json=(title, artist, urlimg, id_collection))
            
        return redirect(url_for('admin_collection'))
    else:
        return redirect(url_for('login'))  
    
@app.route("/admin/exhibition<id_exhibition>", methods=['GET','POST'])
def editexhibitionpage(id_exhibition):

    if "user" in session:
        data = requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/selectexhibition', json=(id_exhibition))

        return render_template("edit-exhibition.html", exhibition=data.json(), user=session["user"])
    else:
        return redirect(url_for('login'))
    

@app.route("/admin/update2<id_exhibition>", methods=['GET','POST'])
def update_exhibition(id_exhibition):
    if "user" in session:
        if request.method == 'POST':
                name = request.form['name']
                description = request.form['description']
                img = request.form['img']
                

                requests.post('https://backend-petra-5zn7xh2gqq-et.a.run.app/updateexhibition', json=(name, description, img, id_exhibition))
            
        return redirect(url_for('admin_exhibition'))
    else:
        return redirect(url_for('login'))  

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080, debug=True)
    