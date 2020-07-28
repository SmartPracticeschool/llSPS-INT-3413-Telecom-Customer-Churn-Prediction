from flask import Flask, request, render_template
from joblib import load
app = Flask(__name__)
model= load('RandomForestModel')
sc=load('StandardScaler')


@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    state=request.form['State']
    if(state=="KS"):
        state1=16
    if(state=="OH"):
        state1=35
    if(state=="NJ"):
        state1=31
    if(state=="OK"):
        state1=36
    if(state=="AL"):
        state1=1
    if(state=="MA"):
        state1=19
    if(state=="MO"):
        state1=24
    if(state=="LA"):
        state1=18
    if(state=="WV"):
        state1=49
    if(state=="IN"):
        state1=15
    if(state=="RI"):
        state1=39
    if(state=="IA"):
        state1=12
    if(state=="MT"):
        state1=26
    if(state=="NY"):
        state1=34
    if(state=="ID"):
        state1=13
    if(state=="VT"):
        state1=46
    if(state=="VA"):
        state1=45
    if(state=="TX"):
        state1=43
    if(state=="FL"):
        state1=9
    if(state=="AZ"):
        state1=3
    if(state=="SC"):
        state1=40
    if(state=="NE"):
        state1=29
    if(state=="WY"):
        state1=50
    if(state=="HI"):
        state1=11
    if(state=="IL"):
        state1=14
    if(state=="NH"):
        state1=30
    if(state=="GA"):
        state1=10
    if(state=="AK"):
        state1=0
    if(state=="MD"):
        state1=20
    if(state=="AR"):
        state1=2
    if(state=="WI"):
        state1=48
    if(state=="MI"):
        state1=22
    if(state=="DE"):
        state1=8
    if(state=="UT"):
        state1=44
    if(state=="CA"):
        state1=4
    if(state=="MN"):
        state1=23
    if(state=="SD"):
        state1=41
    if(state=="NC"):
        state1=27
    if(state=="WA"):
        state1=47
    if(state=="NM"):
        state1=32
    if(state=="NV"):
        state1=33
    if(state=="DC"):
        state1=7
    if(state=="OR"):
        state1=37
    if(state=="CO"):
        state1=5
    if(state=="KY"):
        state1=17
    if(state=="ME"):
        state1=21
    if(state=="MS"):
        state1=25
    if(state=="PA"):
        state1=38
    if(state=="TN"):
        state1=42
    if(state=="CT"):
        state1=6
    
    accountlength=request.form['account length']
    areacode=request.form['area code']
    internationalplan=request.form['International Plan']
    if(internationalplan=="Yes"):
        internationalplan1=1
    if(internationalplan=="No"):
        internationalplan1=0
    
    voicemailplan=request.form['Voice Mail Plan']
    if(voicemailplan=="Yes"):
        voicemailplan1=1
    if(voicemailplan=="No"):
        voicemailplan1=0
        
    nvm=request.form['number vmail messages']
    tdm=request.form['total day minutes']
    tdcalls=request.form['total day calls']
    tdch=request.form['total day charge']
    tem=request.form['total eve minutes']
    tecalls=request.form['total eve calls']
    tech=request.form['total eve charge']
    tnm=request.form['total night minutes']
    tncalls=request.form['total night calls']
    tnch=request.form['total night charge']
    tim=request.form['total intl minutes']
    ticalls=request.form['total intl calls']
    tich=request.form['total intl charge']
    csc=request.form['customer service calls']
    
    test=[[int(state1),int(accountlength),int(areacode),int(internationalplan1),int(voicemailplan1),int(nvm),float(tdm),int(tdcalls),float(tdch),float(tem),int(tecalls),float(tech),float(tnm),int(tncalls),float(tnch),float(tim),int(ticalls),float(tich),int(csc)]]
    
    x_test = sc.transform(test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('index2.html', prediction_text='Churn {}'.format(output))




if __name__ == "__main__":
    app.run(debug=True)