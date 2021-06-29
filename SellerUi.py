from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout,QTableWidget,QTableWidgetItem,QAbstractItemView,QComboBox

class store(QWidget):
  def __init__(self, seller):
    super().__init__()
    self.seller=seller
    products=seller.products
    label=QLabel('current products')
    table=QTableWidget()
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setColumnCount(2)
    table.setRowCount(len(products))
    self.boxlayout=QVBoxLayout()
    self.setLayout(self.boxlayout)
    for i, product in enumerate(products.keys()):
      table.setItem(i,0,QTableWidgetItem(product.name))
      table.setItem(i,1,QTableWidgetItem(str(product.stock(self.seller))))
    self.boxlayout.addWidget(label)
    self.boxlayout.addWidget(table)


      
  

class incom(QWidget):
  def __init__(self, seller):
    super().__init__()
    sells=seller.sells
    Label=QLabel('seller incom')
    table=QTableWidget()
    button=QPushButton("calculate Profit")
    button.clicked.connect(self.calc_profit)
    self.lineedit1=QLineEdit()
    self.lineedit1.setPlaceholderText('start date')
    self.seller=seller
    self.profit_lbl=QLabel()
    self.lineedit2=QLineEdit()
    self.lineedit2.setPlaceholderText('end date')

    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setColumnCount(5)
    table.setRowCount(len(sells))
    self.boxlayout=QVBoxLayout()
    self.setLayout(self.boxlayout)
    self.boxlayout.addWidget(Label)
    self.boxlayout.addWidget(table)
    self.boxlayout.addWidget(self.lineedit1)
    self.boxlayout.addWidget(self.lineedit2)
    self.boxlayout.addWidget(button)
    self.boxlayout.addWidget(self.profit_lbl)




    for i, sell in enumerate(sells):
      table.setItem(i,0,QTableWidgetItem(sells[0]))
      table.setItem(i,0,QTableWidgetItem(sells[1]))
      table.setItem(i,0,QTableWidgetItem(sells[2]))
      table.setItem(i,0,QTableWidgetItem(sells[3]))
      table.setItem(i,0,QTableWidgetItem(sells[4]))





  def calc_profit(self):
    profits=self.seller.profit(self.lineedit1.text(), self.lineedit2.text())
    self.profit_lbl.setText(str(profits))


 

       
       
    self.boxlayout.addWidget(self.LineEdit1)
    self.boxlayout.addWidget(self.LineEdit2)   









class  makecommodity(QWidget):
  def __init__(self, store, seller):
    self.products=store.products
    self.seller = seller
    super().__init__()

    self.boxlayout=QVBoxLayout()
    self.lineedit1=QLineEdit()
    self.lineedit2=QLineEdit()
    self.lineedit3=QLineEdit()
    self.lineedit4=QLineEdit()
    self.lineedit5=QLineEdit()
    label1=QLabel("Create New Product:")
    self.boxlayout.addWidget(label1)
    self.boxlayout.addWidget(self.lineedit1)
    self.boxlayout.addWidget(self.lineedit2)
    self.boxlayout.addWidget(self.lineedit3)
    self.lineedit1.setPlaceholderText('name')
    self.lineedit2.setPlaceholderText('description')
    self.lineedit3.setPlaceholderText('picture')
    self.lineedit4.setPlaceholderText('Price')
    self.lineedit5.setPlaceholderText('Number_of_goods')
    self.button1=QPushButton('Create Product')
    self.button1.clicked.connect(self.send_applying_for)
    self.boxlayout.addWidget(self.button1)

    label2=QLabel("Add Stock:")
    self.boxlayout.addWidget(label2)
    self.product_combobox=QComboBox()
    for product in self.products:
      self.product_combobox.addItem(product.name)
    self.boxlayout.addWidget(self.product_combobox)
    self.boxlayout.addWidget(self.lineedit4)
    self.boxlayout.addWidget(self.lineedit5)

 
  
    button2=QPushButton("Add")
    button2.clicked.connect(self.add_stock_price)
    self.boxlayout.addWidget(button2)

    self.setLayout(self.boxlayout)

  


  def send_applying_for(self):
    name=self.lineedit1.text()
    description=self.lineedit2.text()
    image=self.lineedit3.text()
    if image=='':
      self.seller.create_new_product(name, description)
    else:
       self.seller.create_new_product(name, description, image)
    self.lineedit1.setText("") 
    self.lineedit2.setText("")
    self.lineedit3.setText("")  


  def add_stock_price(self):
    price=self.lineedit4.text()
    stock=self.lineedit5.text()
    product=self.products[self.product_combobox.currentIndex()]
    self.seller.add_product_stock(product, int(price), int(stock))
    self.lineedit4.setText("")
    self.lineedit5.setText("")


    


class general(QWidget):
  def __init__(self, seller, seller_store):
    super().__init__()
    layout=QHBoxLayout()
    self.setLayout(layout)
    store_widget=store(seller)
    incom_widget=incom(seller)
    makecommodity_widget=makecommodity(seller_store, seller)
    layout.addWidget(incom_widget)
    layout.addWidget(store_widget)
    layout.addWidget(makecommodity_widget)
