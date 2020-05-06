{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":39,"position":39,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":[">"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[">"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":[">"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":[">"]}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":[">"],"id":2},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":[">"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[">"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[">"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":[">"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[">"]}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[">"],"id":3},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[">"]},{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":4},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["v"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["v"],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":6}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":71},"action":"remove","lines":["os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":7}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":121},"action":"insert","lines":["mongodb+srv://root:<password>@myfirstcluster-mknew.mongodb.net/test?retryWrites=true&w=majority"],"id":8}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":55},"action":"remove","lines":["<password>"],"id":9},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["r"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["0"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["0"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["t"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["U"]}],[{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["s"],"id":10},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["e"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":87},"end":{"row":7,"column":91},"action":"remove","lines":["test"],"id":11},{"start":{"row":7,"column":87},"end":{"row":7,"column":88},"action":"insert","lines":["t"]},{"start":{"row":7,"column":88},"end":{"row":7,"column":89},"action":"insert","lines":["a"]},{"start":{"row":7,"column":89},"end":{"row":7,"column":90},"action":"insert","lines":["s"]},{"start":{"row":7,"column":90},"end":{"row":7,"column":91},"action":"insert","lines":["k"]},{"start":{"row":7,"column":91},"end":{"row":7,"column":92},"action":"insert","lines":["_"]},{"start":{"row":7,"column":92},"end":{"row":7,"column":93},"action":"insert","lines":["m"]},{"start":{"row":7,"column":93},"end":{"row":7,"column":94},"action":"insert","lines":["a"]},{"start":{"row":7,"column":94},"end":{"row":7,"column":95},"action":"insert","lines":["n"]},{"start":{"row":7,"column":95},"end":{"row":7,"column":96},"action":"insert","lines":["a"]},{"start":{"row":7,"column":96},"end":{"row":7,"column":97},"action":"insert","lines":["g"]}],[{"start":{"row":7,"column":97},"end":{"row":7,"column":98},"action":"insert","lines":["e"],"id":12},{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["\""],"id":13}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["\""],"id":14}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["'"],"id":15}],[{"start":{"row":7,"column":128},"end":{"row":7,"column":129},"action":"insert","lines":["'"],"id":16}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":34},"action":"remove","lines":["mongodb"],"id":17},{"start":{"row":7,"column":65},"end":{"row":7,"column":72},"action":"insert","lines":["mongodb"]}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = '+srv://root:r00tUser@myfirstcluster-mkmongodbnew.mongodb.net/task_manager?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":19},{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":22},"action":"remove","lines":["True"],"id":20},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["F"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["a"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["s"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["l"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["s"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["e"],"id":21},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":["s"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"remove","lines":["l"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"remove","lines":["s"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["l"],"id":22},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["s"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":24},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":22,"column":0},"end":{"row":22,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":23},"action":"remove","lines":["False"],"id":24},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["T"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["r"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["u"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":[","],"id":25}],[{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":47},"action":"insert","lines":["'0.0.0.0'"],"id":27}],[{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":[","],"id":28}],[{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":46},"action":"insert","lines":["\"\""],"id":30}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":46},"action":"remove","lines":["\"\""],"id":31}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":46},"action":"insert","lines":["''"],"id":32}],[{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"insert","lines":["5"],"id":33},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":["0"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":["0"]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["0"]}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"remove","lines":["'"],"id":34}],[{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"remove","lines":["'"],"id":35}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"remove","lines":["'"],"id":36}],[{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["'"],"id":37}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["'"],"id":38}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["'"],"id":39}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"insert","lines":["'"],"id":40}],[{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":["'"],"id":41}]]},"ace":{"folds":[],"scrolltop":194.5,"scrollleft":0,"selection":{"start":{"row":22,"column":12},"end":{"row":22,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1588769738006,"hash":"08c6b06f7bd1e0044101b66fc2c804b9b2dda31f"}