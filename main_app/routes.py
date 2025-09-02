from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/peer_reviewed')
def peer_reviewed():
    return render_template('peer_reviewed.html')


@app.route('/ugc_care')
def ugc_care():
    return render_template('ugc_care.html')


@app.route('/DOI_Allocation')
def DOI_Allocation():
    return render_template('DOI_Allocation.html')


@app.route('/Payment')
def Payment():
    return render_template('Payment.html')

@app.route('/narmada_revier')
def narmada_revier():
    return render_template('Narmada_revier.html')


@app.route('/current_issue')
def current_issue():
    return render_template('Current_issue.html')


@app.route('/leaf_beetle_research')
def leaf_beetle_research():
    return render_template('Leaf_beetle_research.html')


@app.route('/genetic_fidelity')
def genetic_fidelity():
    return render_template('Genetic_fidelity.html')


@app.route('/mining_activities')
def mining_activities():
    return render_template('Mining_activities.html')


@app.route('/groundwater_levels')
def groundwater_levels():
    return render_template('Groundwater_levels.html')

@app.route('/group')
def group():
    return render_template('group.html')
