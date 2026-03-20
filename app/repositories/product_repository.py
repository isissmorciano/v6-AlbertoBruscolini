from app.db import get_db

def get_all_products():
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM prodotti p
        JOIN categorie c ON c.id = p.categoria_id
        ORDER BY c.nome, p.nome
    ''').fetchall()

def get_products_by_category(category_id):
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM prodotti p
        JOIN categorie c ON c.id = p.categoria_id
        WHERE p.categoria_id = ?
        ORDER BY p.nome
    ''', (category_id,)).fetchall()
    
    
def get_product_by_id(product_id):
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM prodotti p
        JOIN categorie c ON c.id = p.categoria_id
        WHERE p.id = ?
    ''', (product_id,)).fetchone()

def create_product(category_id, nome, prezzo):
    db = get_db()
    db.execute('INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (?, ?, ?)',
               (category_id, nome, prezzo))
    db.commit()
    
def find_products_by_name(search_term):
    db = get_db()
    return db.execute('''
        SELECT p.*, c.nome AS categoria_nome
        FROM prodotti p
        JOIN categorie c ON c.id = p.categoria_id
        WHERE LOWER(p.nome) LIKE LOWER(?)
        ORDER BY c.nome, p.nome
    ''', (f'%{search_term}%',)).fetchall()