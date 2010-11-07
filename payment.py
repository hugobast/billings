import os
import sys
import copy
import pickle
import macro
import wx


class Batch(object):

    def __init__(self):
        self.invoices = []
        self.current_invoice = None

    def create_nwo(self):
        macro.create_nwo(self.current_invoice)

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def get_current_invoice(self):
        return self.current_invoice

    def select_invoice(self, index):
        self.current_invoice = self.invoices[index]

    def refresh(self):
        if self.current_invoice == None:
            return
        sales_cheque_number = self.current_invoice.get_sales_cheque_number()
        invoices = [inv for inv in self.invoices if inv.get_sales_cheque_number() == sales_cheque_number]
        for invoice in invoices:
            invoice.detail = copy.deepcopy(self.current_invoice.detail)
            invoice.set_flag(self.current_invoice.get_flag())
                
    def remove_invoice(self, invoice):
        self.invoices.remove(invoice)

    def sort_by_contractor(self):
        self.invoices.sort \
        (
            lambda x, y: cmp(x.get_contractor_alias(), y.get_contractor_alias())
        )

    def pay(self, payments):
        unique_contractor_names = set([inv.get_contractor_alias() for inv in self.invoices])
        for contractor_name in unique_contractor_names:
            contractor_invoices = [inv for inv in self.invoices if inv.get_contractor_alias() == contractor_name]
            valid_contractor_invoices = [inv for inv in contractor_invoices if inv.is_profitable_and_valid()]
            if valid_contractor_invoices != []:
                current_payment = copy.deepcopy(macro.new_payment(valid_contractor_invoices))
                if type(current_payment) is str:
                    wx.MessageBox('Une erreur s'est produite avec la commande: ' + current_payment, 'Info)
                else:
                    payments.add_payment(Payment(current_payment, valid_contractor_invoices))
                    self.current_invoice = None
                    for invoice in valid_contractor_invoices:
                        invoice.is_paid = True
                        self.remove_invoice(invoice)


class InvoiceFactory(object):

    def __init__(self):
        self.navigator = HostNavigator()

    def create_new_invoice(self):
        macro.create_invoice_from_factory()

    def get_customers(self, number):
        self.navigator.new_route()
        self.navigator.append(macro.get_jobs, number)
        return parse_screen(macro.get_jobs(number))

    def get_invoices(self, index):
        self.navigator.append(macro.get_invoices, index)
        return parse_screen(macro.get_invoices(index))

    def get_invoice(self, index):
        self.navigator.append(macro.get_invoice, index)
        self.oie = copy.deepcopy(macro.get_invoice(index))
        self.detail = copy.deepcopy(macro.get_detail())
        return self.oie

    def make_invoice(self):
        return Invoice(self.detail, self.oie, self.navigator)


class Invoice(object):

    def __init__(self, detail, oie, navigator):
        
        self.navigator = navigator
        self.oie = oie
        self.detail = detail
        self.notes = ''
        self.flag = self.is_profitable()
        self.is_paid = False

    def is_profitable(self):
        if int(self.calculate_final_mark_up()) > 25: #will come from a lookup table
            return 2
        return 1

    def is_profitable_and_valid(self):

        return self.get_vendor_invoice() and \
               self.get_received_date() and \
               (self.get_flag() == 2)

    def is_customer_rung(self):
        return macro.is_customer_rung(self.get_comm())

    def get_customer_name(self):
        return self.oie.customer_name.get_text()

    def get_sales_cheque_number(self):
        return self.detail.sales_cheque_number.get_text()

    def get_comm(self):
        return self.oie.comm.get_text()

    def get_total_cost(self):
        return self.oie.total_cost.get_text()

    def get_total_selling(self):
        return self.oie.total_selling.get_text()

    def get_sell_unit(self):
        return self.oie.sell_unit.get_text()

    def get_mark_up(self):
        return self.calculate_final_mark_up()

    def get_contractor_alias(self):
        return self.oie.contractor_alias.get_text()

    def get_vendor_invoice(self):
        return self.oie.vendor_invoice.get_text()

    def get_received_date(self):
        return self.oie.received_date.get_text()

    def get_flag(self):
        return self.flag

    def get_notes(self):
        return self.notes

    def get_items(self):
        return parse_screen(self.oie)

    def set_notes(self, notes):
        self.notes = notes

    def set_flag(self, flag):
        self.flag = flag

    def get_to(self):
        self.navigator.travel()

    def calculate_final_mark_up(self):

        sell = float(self.detail.initial_selling.get_text()) + \
               float(self.detail.adjusted_selling.get_text()) + \
               float(self.detail.warranty_work_selling.get_text())
        
        cost = float(self.detail.initial_cost.get_text()) + \
               float(self.detail.adjusted_cost.get_text()) + \
               float(self.detail.warranty_work_cost.get_text())

        delta = sell - cost
        if sell == 0:
            return '0'
        return str(int(delta / sell * 100))

    def __get_relative_oieitem(self, pos):
        return self.oie.get_item(pos)

    def refresh(self):
        
        self.get_to()
        self.oie.scrape()
        self.detail.get_to()
        self.detail.scrape()
        self.flag = self.is_profitable()

    def set_contractor_alias(self, cntr):
        self.oie.contractor_alias.text = cntr

    def set_vendor_invoice(self, inv):
        self.oie.vendor_invoice.text = inv

    def set_received_date(self, date):
        self.oie.received_date.text = date

    def set_total_cost(self, cost):
        self.oie.total_cost.text = cost

    def set_total_selling(self, selling):
        self.oie.total_selling.text = selling

    def update(self, cntr, inv, date):

        self.get_to()
        self.oie.contractor_alias.update()
        self.oie.save()
        self.oie.vendor_invoice.update()
        self.oie.received_date.update()
        self.oie.update_items()
        self.oie.save()
        self.oie.scrape()
        self.detail.get_to()
        self.detail.scrape()
        self.flag = self.is_profitable()

    def update_item(self, data):
        self.__get_relative_oieitem(data).text = data[2]


class Payments(object):

    def __init__(self):
        self.payments = []
        current_payment = None

    def add_payment(self, payment):
        self.payments.append(payment)

    def select_payment(self, index):
        self.currentPayment = self.payments[index]


class Payment(object):

    def __init__(self, vpd, invoices):
        self.vpd = vpd
        self.invoices = invoices

    def get_contractor_alias(self):
        return self.vpd.contractor_alias.get_text()

    def get_amount(self):
        return self.vpd.total.get_text()

    def get_date(self):
        return self.vpd.created_date.get_text()

    def get_ref_one(self):
        return self.vpd.created_reference.get_text()

    def get_ref_two(self):
        return self.vpd.paid_reference.get_text()


def pickle_batch(batch):
    pickle.Pickler(open('batch.p', 'wb'), pickle.HIGHEST_PROTOCOL).dump(batch)
 

def parse_screen(screen):
    
    if not screen:
        return ''

    if screen.is_list():
        l = []
        for i in screen.items:
            l.append([f.get_text() for f in i.fields])
        return l
    else:
        return [f.get_text() for f in screen.fields]


class HostNavigator(object):

    def __init__(self):
        self.directions = []

    def new_route(self):
        self.directions = []

    def remove_last_direction(self):
        self.directions.pop()

    def append(self, direction, *args):
        self.directions.append([direction, args])

    def travel(self):
        updated_screens = []
        for direction, args in self.directions:
            updated_screens.append(direction(*args))
        return updated_screens
