
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user

            Age=float(request.form['Age'])
            Fare= float(request.form['Fare'])
            Parch = int(request.form['Parch'])
            SibSp = int(request.form['SibSp'])
            Pclass = int(request.form['Pclass'])
            Sex = str(request.form['Sex'])
            if Sex == "Male":
                Sex_ind = 1
            else:
                Sex_ind = 0
            filename = 'decission_tree_model.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Pclass,Sex_ind,Age,SibSp,Parch,Fare]])
            if prediction[0] == 1:
                results = "Survived"
            else:
                results = "not survived"
            # showing the prediction results in a UI
            return render_template('results.html',result=results)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app