# VERIFICA: Negozio Online - Flask App da Zero

## Scenario
Devi creare un'applicazione Flask per gestire un **negozio online** con categorie di prodotti e i relativi prodotti. L'applicazione deve permettere di visualizzare i dati, crearli, e fornire funzionalità di ricerca e analisi.

## Relazione Dati
- **Categoria**: id, nome
- **Prodotto**: id, categoria_id, nome, prezzo
- Relazione: Una categoria ha molti prodotti

---

## Schema del Database (Fornito)

```sql
DROP TABLE IF EXISTS prodotti;
DROP TABLE IF EXISTS categorie;

CREATE TABLE categorie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL
);

CREATE TABLE prodotti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categoria_id INTEGER NOT NULL,
  nome TEXT NOT NULL,
  prezzo REAL NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categorie (id)
);

-- Dati di esempio
INSERT INTO categorie (nome) VALUES ('Elettronica');
INSERT INTO categorie (nome) VALUES ('Libri');
INSERT INTO categorie (nome) VALUES ('Abbigliamento');

INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (1, 'Laptop', 999.99);
INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (1, 'Mouse', 29.99);
INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (2, 'Python 101', 39.99);
INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (2, 'Flask Guida', 34.99);
INSERT INTO prodotti (categoria_id, nome, prezzo) VALUES (3, 'Maglietta', 19.99);
```

---

## Esercizi

### 1. Implementa CRUD da Zero

**Struttura richiesta:**

1. **File `app/repositories/categoria_repository.py`:**
   - `get_all_categories()` → lista di tutte le categorie ordinate per nome
   - `get_category_by_id(category_id)` → una singola categoria
   - `create_category(nome)` → inserisce nuova categoria

2. **File `app/repositories/product_repository.py`:**
   - `get_all_products()` → lista di tutti i prodotti (con nome categoria tramite JOIN)
   - `get_products_by_category(category_id)` → prodotti di una categoria specifica
   - `get_product_by_id(product_id)` → un singolo prodotto
   - `create_product(category_id, nome, prezzo)` → inserisce nuovo prodotto

3. **Route in `main.py`:**
   - `GET /` → lista della categorie (index)
   - `GET /categoria/<id>` → dettaglio categoria con lista prodotti
   - `GET /crea_categoria` → form per nuova categoria
   - `POST /crea_categoria` → salva categoria nel DB
   - `GET /crea_prodotto` → form per nuovo prodotto (select categoria)
   - `POST /crea_prodotto` → salva prodotto nel DB

4. **Template:**
   - `index.html` → lista categorie (link a dettagli)
   - `categoria_detail.html` → nome categoria + lista prodotti (nome, prezzo)
   - `crea_categoria.html` → form con input nome
   - `crea_prodotto.html` → form con select categoria, input nome/prezzo

**Checklist:**
- [ ] Due repository creati con funzioni CRUD
- [ ] 6 route implementate
- [ ] 4 template creati
- [ ] Navigazione funzionante tra categorie e dettagli
- [ ] Creazione di categorie e prodotti operativa

---

### 2. Ricerca Prodotti

**Cosa fare:**

- **Funzione in `product_repository.py`:**
  - `find_products_by_name(search_term)` → cerca per nome prodotto (case-insensitive, LIKE)
  - Restituisce prodotti con nome categoria (tramite JOIN)
  - Ordina per categoria, poi per nome

- **Route in `main.py`:**
  - `GET /ricerca` → mostra form ricerca vuoto
  - `POST /ricerca` → recupera termine, chiama funzione, passa risultati

- **Template `ricerca.html`:**
  - Form di ricerca (sempre visibile)
  - Lista risultati: nome prodotto | categoria | prezzo
  - Messaggio "Nessun prodotto trovato" se vuota
  - Link al dettaglio categoria per ogni risultato

**Checklist:**
- [ ] Funzione `find_products_by_name()` in product_repository
- [ ] Route GET `/ricerca` (form vuoto)
- [ ] Route POST `/ricerca` (risultati)
- [ ] Template `ricerca.html` creato
- [ ] Ricerca case-insensitive funzionante

---

### 3. Ranking Categorie

**Cosa fare:**

- **Funzione in `categoria_repository.py`:**
  - `get_categories_stats()` → raggruppa tutte le categorie con:
    - nome categoria
    - numero di prodotti
    - prezzo totale (somma di tutti i prodotti)
    - prezzo medio
  - Ordina per numero di prodotti (decrescente)
  - Restituisce lista di dizionari

- **Route in `main.py`:**
  - `GET /statistiche` → mostra il ranking

- **Template `statistiche.html`:**
  - Tabella con colonne: **Rank** | **Categoria** | **# Prodotti** | **Prezzo Tot.** | **Prezzo Med.**
  - Usa `loop.counter` per il ranking auto
  - Se nessuna categoria, mostra "Nessuna categoria"

**Checklist:**
- [ ] Funzione `get_categories_stats()` in categoria_repository
- [ ] Route `GET /statistiche`
- [ ] Template `statistiche.html` creato
- [ ] Tabella con 5 colonne funzionante
- [ ] Formattazione prezzi a 2 decimali

---

## Struttura Progetto Attesa

```
negozio_online/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   ├── schema.sql
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── categoria_repository.py
│   │   └── product_repository.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── categoria_detail.html
│       ├── crea_categoria.html
│       ├── crea_prodotto.html
│       ├── ricerca.html
│       └── statistiche.html
├── instance/
├── run.py
├── setup_db.py
└── README.md
```

