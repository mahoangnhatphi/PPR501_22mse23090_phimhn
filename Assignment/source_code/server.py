from flask import Flask, flash, render_template, request

from LaptopBestSeller import LaptopBestSeller
from module.database import Database

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()


@app.route('/', methods=['GET'])
def index():
    return laptopBestSeller()


@app.route('/laptopBestSeller', methods=['GET'])
def laptopBestSeller():
    bestSellerLaptops = db.get_laptops_best_seller()
    print(bestSellerLaptops)
    return render_template('laptopBestSeller.html', bestSellerLaptops=bestSellerLaptops)


@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_laptop():
    form = request.form
    Id = form.get('Id')
    Brand = form.get('Brand')
    Name = form.get('Name')
    OldPrice = form.get('OldPrice')
    NewPrice = form.get('NewPrice')
    PercentDiscount = form.get('PercentDiscount')
    BestSeller = form.get('BestSeller')
    laptop_best_seller = LaptopBestSeller(Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller)
    if db.insert(laptop_best_seller):
        flash("A post has been added")
    else:
        flash("A post can not be added")
    return laptopBestSeller()


@app.route('/edit/<int:id>/', methods=['GET'])
def edit(id):
    laptop_best_seller = db.get_laptop_by_id(id)
    return render_template('edit.html', laptop_best_seller=laptop_best_seller)


@app.route('/edit/<int:id>/', methods=['POST'])
def update_edit(id):
    form = request.form
    Id = form.get('Id')
    Brand = form.get('Brand')
    Name = form.get('Name')
    OldPrice = form.get('OldPrice')
    NewPrice = form.get('NewPrice')
    PercentDiscount = form.get('PercentDiscount')
    BestSeller = form.get('BestSeller')
    laptop_best_seller = LaptopBestSeller(Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller)
    if db.update(laptop_best_seller):
        flash("A laptop has been updated")
    else:
        flash("A laptop can not be updated")
    laptop_best_seller = db.get_laptop_by_id(id)
    return render_template('edit.html', laptop_best_seller=laptop_best_seller)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if db.delete(id):
        flash("A post has been deleted")
    else:
        flash("A post can not be deleted")
    return laptopBestSeller()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
