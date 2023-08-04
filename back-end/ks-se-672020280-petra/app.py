import falcon
import json
import psycopg2
import connectdb

app = falcon.App()

class GetUser:
    def on_get(self, req, resp):
        query = 'SELECT * from "672020280_companyprofile_login"'
        dataraw = connectdb.select(query)
        data = []

        for row in dataraw:
            data.append({'username': row[0],'password': row[1]})

        resp.media = data
        resp.status = falcon.HTTP_200

class ReadCollection:
    def on_get(self, req, resp):
        query = 'SELECT * from "672020280_companyprofile_collection"'
        dataraw = connectdb.select(query)
        data = []

        for row in dataraw:
            data.append({'id_collection': row[0],'title': row[1],'artist': row[2],'img': row[3]})

        resp.media = data
        resp.status = falcon.HTTP_200

class AddCollection:
        def on_post(self, req, resp):
        
            data = json.load(req.stream)
        
            print(data)
            query = 'INSERT INTO public."672020280_companyprofile_collection" (title, artist, img) VALUES (%s ,%s ,%s)'
            data2 = connectdb.insert(query,data)
            
            resp.media = str(data2)
            resp.status = falcon.HTTP_200


class UpdateCollection:
    def on_post(self, req, resp):

        data = json.load(req.stream)

        print(data)
        query = 'UPDATE public."672020280_companyprofile_collection" SET title = %s, artist = %s, img= %s WHERE id_collection = %s'
        data2 = connectdb.update(query,data)
        
        resp.media = str(data2)
        resp.status = falcon.HTTP_200

class DeleteCollection:
    def on_post(self, req, resp):

        data = json.load(req.stream)


        query = 'DELETE FROM public."672020280_companyprofile_collection" WHERE id_collection = %s'
        data2 = connectdb.delete(query,data)
        
        resp.media = str(data2)
        resp.status = falcon.HTTP_200

class SelectCollection:
    def on_post(self, req, resp):
        
        data = json.load(req.stream)

        

        query = 'SELECT * from "672020280_companyprofile_collection" WHERE id_collection = %s'
        dataraw = connectdb.selectcollection(query, data)
        data = []

        for row in dataraw:
            data.append({'id_collection': row[0],'title': row[1],'artist': row[2],'img': row[3]})

        resp.media = data
        
        resp.status = falcon.HTTP_200

app.add_route('/getuser', GetUser())
app.add_route('/collection', ReadCollection())
app.add_route('/addcollection', AddCollection())
app.add_route('/selectcollection', SelectCollection())
app.add_route('/updatecollection', UpdateCollection())
app.add_route('/deletecollection', DeleteCollection())



class ReadExhibition:
    def on_get(self, req, resp):
        query = 'SELECT * from "672020280_companyprofile_exhibition"'
        dataraw = connectdb.select(query)
        data = []

        for row in dataraw:
            data.append({'id_exhibition': row[0],'name': row[1],'description': row[2],'img': row[3]})

        resp.media = data
        resp.status = falcon.HTTP_200

class AddExhibition:
        def on_post(self, req, resp):
        
            data = json.load(req.stream)
        
            print(data)
            query = 'INSERT INTO public."672020280_companyprofile_exhibition" (id_exhibition, name, description, img) VALUES (%s, %s ,%s ,%s)'
            data2 = connectdb.insert(query,data)
            
            resp.media = str(data2)
            resp.status = falcon.HTTP_200

class UpdateExhibition:
    def on_post(self, req, resp):

        data = json.load(req.stream)

        print(data)
        query = 'UPDATE public."672020280_companyprofile_exhibition" SET name = %s, description = %s, img= %s WHERE id_exhibition = %s'
        data2 = connectdb.update(query,data)
        
        resp.media = str(data2)
        resp.status = falcon.HTTP_200

class DeleteExhibition:
    def on_post(self, req, resp):

        data = json.load(req.stream)


        query = 'DELETE FROM public."672020280_companyprofile_exhibition" WHERE id_exhibition = %s'
        data2 = connectdb.delete2(query,data)
        
        resp.media = str(data2)
        resp.status = falcon.HTTP_200

class SelectExhibition:
    def on_post(self, req, resp):
        
        data = json.load(req.stream)

        

        query = 'SELECT * from "672020280_companyprofile_exhibition" WHERE id_exhibition = %s'
        dataraw = connectdb.selectexhibition(query, data)
        data = []

        for row in dataraw:
            data.append({'id_exhibition': row[0],'name': row[1],'description': row[2],'img': row[3]})

        resp.media = data
        
        resp.status = falcon.HTTP_200


app.add_route('/exhibition', ReadExhibition())
app.add_route('/addexhibition', AddExhibition())
app.add_route('/selectexhibition', SelectExhibition())
app.add_route('/updateexhibition', UpdateExhibition())
app.add_route('/deleteexhibition', DeleteExhibition())



class AddExhibitions:
    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        print(data)
        
        query = 'INSERT INTO public."672020280_companyprofile_exhibition" (id_exhibition, name, description, img) VALUES (%s, %s, %s, %s)'
        data2 = connectdb.insert(query, (data['id_exhibition'], data['name'], data['description'], data['img']))
        
        resp.media = str(data2)
        resp.status = falcon.HTTP_200

app.add_route('/addexhibitions', AddExhibitions())


class ReadExhibition1:
    def on_get(self, req, resp):
        query = 'SELECT * from "672020280_companyprofile_exhibition" WHERE id_exhibition = {id_exhibition}'
        dataraw = connectdb.select(query)
        data = []

        for row in dataraw:
            data.append({'id_exhibition': row[0],'name': row[1],'description': row[2],'img': row[3]})

        resp.media = data
        resp.status = falcon.HTTP_200
app.add_route('/exhibition/{id_exhibition}', ReadExhibition1())

class AddCollections:
        def on_post(self, req, resp):
        
            data = json.load(req.stream)
            print(data)
            
            query = 'INSERT INTO public."672020280_companyprofile_collection" (title, artist, img) VALUES ({{%s}} ,{{%s}} ,{{%s}})'
            data2 = connectdb.insert(query,data)
            
            resp.media = str(data2)
            resp.status = falcon.HTTP_200

app.add_route('/addcollections', AddCollections())