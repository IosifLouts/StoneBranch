import datetime


class CustomerInput:
   def __init__(self, customercode):
       self.customercode = customercode


class Customer:
    def __init__(self,customercode,firstname,lastname):
      self.customercode = customercode
      self.firstname = firstname
      self.lastname = lastname


class Invoice:
    def __init__(self,customercode,invoicecode,amount,date):
      self.customercode = customercode
      self.invoicecode = invoicecode
      self.amount = amount
      self.date = date



class InvoiceItem:
    def __init__(self, invoicecode, itemcode,amount,quantity):
      self.invoicecode = invoicecode
      self.itemcode = itemcode
      self.amount = amount
      self.quantity = quantity

