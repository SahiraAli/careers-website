from flask import Flask, json, render_template,jsonify
app=Flask(__name__)

RECIPES =  [
  {
    'id':1,
    'Title': 'Dal Tadka',
    'Type': 'Veg',
    'Origin':'Gujarat, India',
    'Total Time' : '40 min'
  },
  {
    'id':2,
    'Title': 'Paratha',
    'Type': 'Veg',
    'Origin':'Jaffna, Sri Lanka',
    'Total Time' : '60 min'
  },
  {
    'id':3,
    'Title': 'Chicken Kosha',
    'Type': 'Non-Veg',
    'Origin':'West Bengal, India',
    'Total Time' : '60 min'
  },
  {
    'id':4,
    'Title': 'Lumpia',
    'Type': 'Non-Veg',
    'Origin':'Fujian, China',
    'Total Time' : '70 min'
  }
]

@app.route('/')
def hello_world():
  return render_template("home.html", recipes= RECIPES, company_name="Food Hunt")


@app.route("/api/recipes")
def list_recipes():
    return jsonify("RECIPES")

if(__name__ == "__main__"):
  app.run(host='0.0.0.0',debug=True)

        
