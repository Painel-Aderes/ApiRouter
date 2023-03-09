from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/users', methods=['POST', 'GET', 'DELETE'])
def users():
    # gets all users
    if request.method=='GET':

        df = pd.read_csv('Planilha1.csv')
        
        return {'status carteira': df.to_dict()}, 200
     
    
