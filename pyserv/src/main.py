from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# # user: id, name
# # invoice: user_id, description,
# # line_item: invoice_id, description, unit_cost, quantity
# def inv_cost(invoice):
#     line_items=sql("select * from line_item where id=" + invoice.id)
#     total=0
#     for li in line_items:
#         total+= li.unit_cost*li.quantity
#     return total

@app.route("/db_test")
def test():
    con = psycopg2.connect(host="db", database="testdb", user="postgres", password="pass123")
    cur=con.cursor()
    cur.execute("select * from invoices;")
    elems=cur.fetchall()
    return f"""
    <html>
      <body>
        <ul>
          <li>
            {"</li><li>".join(e[1] for e in elems)}
          </li>
        </ul>
      </body>
    </html>
    """

@app.route("/invoices")
def invoices():
    invoices={}
    # invoice_cost=defaultdict(0)
    for i in sql('select * from users'):
        current_invoice=sql('select from invoices where user_id=' + i.id)
        invoices[i.name]+=current_invoice
        # invoice_cost[i.id]+=current_invoice.cost
        # invoice_cost[i.id]+=inv_cost(current_invoice)

    # costs={}
    # for k, v in invoices:
    #     costs[k]+=v.cost
    return 1
