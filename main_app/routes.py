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

@app.route('/khare_2025_biodegradation')
def khare_2025_biodegradation():
    return render_template('khare_2025_biodegradation.html')


@app.route('/current_issue')
def current_issue():
    return render_template('Current_issue.html')


@app.route('/archive_issue')
def archive_issue():
    return render_template('archive_issue.html')


@app.route('/meena_nutrient_supplementation')
def meena_nutrient_supplementation():
    return render_template('meena_nutrient_supplementation.html')


@app.route('/bioremediation_fungi')
def bioremediation_fungi():
    return render_template('bioremediation_fungi.html')


@app.route('/mhc_polymorphism_naked_neck')
def mhc_polymorphism_naked_neck():
    return render_template('mhc_polymorphism_naked_neck.html')


@app.route('/Sharnagat')
def Sharnagat():
    return render_template('Sharnagat.html')

@app.route('/group')
def group():
    return render_template('group.html')
