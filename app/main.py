
from flask import Blueprint, render_template, request, redirect, url_for
from app.repositories import categoria_repository, product_repository

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    categories = categoria_repository.get_all_categories()
    return render_template('index.html', categories=categories)

@bp.route('/categoria/<int:id>')
def categoria_detail(id):
    category = categoria_repository.get_category_by_id(id)
    if category is None:
        return "Categoria non trovata", 404
    products = product_repository.get_products_by_category(id)
    return render_template('categoria_detail.html', category=category, products=products)

@bp.route('/crea_categoria', methods=['GET', 'POST'])
def crea_categoria():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        if nome:
            categoria_repository.create_category(nome)
            return redirect(url_for('main.index'))
    return render_template('crea_categoria.html')



@bp.route('/crea_prodotto', methods=['GET', 'POST'])
def crea_prodotto():
    categories = categoria_repository.get_all_categories()
    if request.method == 'POST':
        category_id = request.form['categoria_id']
        nome = request.form['nome'].strip()
        prezzo = request.form['prezzo']
        if category_id and nome and prezzo:
            product_repository.create_product(category_id, nome, float(prezzo))
            return redirect(url_for('main.index'))
    return render_template('crea_prodotto.html', categories=categories)

@bp.route('/ricerca', methods=['GET', 'POST'])
def ricerca():
    return render_template('ricerca.html', results=results, search_term=search_term, searched=searched)

@bp.route('/ricerca', methods=['GET', 'POST'])
def ricerca():
    results = []
    search_term = ''
    searched = False
    if request.method == 'POST':
        search_term = request.form.get('q', '').strip()
        searched = True
        if search_term:
            results = product_repository.find_products_by_name(search_term)
    return render_template('ricerca.html', results=results, search_term=search_term, searched=searched)

@bp.route('/statistiche')
def statistiche():
    stats = categoria_repository.get_categories_stats()
    return render_template('statistiche.html', stats=stats)


