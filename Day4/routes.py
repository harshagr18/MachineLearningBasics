from flask import Blueprint,request,jsonify
import pickle

flowers = ['setosa','versicolor','virginica']

model = pickle.load(open('FirstMlMachine.model','rb'))

model_predictor = Blueprint('model_predictor',__name__)
@model_predictor.route('/predict',methods=['POST'])
def predict_value():
    sepal_length = request.get_json()['sepal_length']   
    sepal_width = request.get_json()['sepal_width']
    petal_length = request.get_json()['petal_length']
    petal_width = request.get_json()['petal_width']
    ans = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    print("Hulahul")
    print(ans)
    return jsonify(
        {
            'flower' : flowers[ans[0]]
        }

    )
