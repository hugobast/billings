import payment
import interactors
import ui.windows


class BatchPresenter(object):
    
    def __init__(self, batch, payments, view, interactor):
        self.batch = batch
        self.payments = payments
        self.view = view
        interactor.install(self, view)
        self.load_view()
        view.start()

    def pickle_batch(self):
        payment.pickle_batch(self.batch)

    def refresh_view(self):
        self.batch.refresh()
        self.view.delete_invoices()
        for invoice in self.batch.invoices:
            self.view.add_invoice(invoice)
        self.view.delete_payments()
        for payment in self.payments.payments:
            if payment != None:
                self.view.add_payment(payment)

    def load_view(self):
        for invoice in self.batch.invoices:
            self.view.add_invoice(invoice)
        for payment in self.payments.payments:
            self.view.add_payment(payment)

    def start_add_invoice_dialog(self):
        
        InvoiceFactoryPresenter \
        (
            self, 
            payment.InvoiceFactory(),
            ui.windows.InvoiceFactoryWindow(self.view),
            interactors.InvoiceFactoryInteractor()
        )

    def start_edit_invoice_dialog(self):
        
        InvoicePresenter \
        (
            self,
            self.batch.get_current_invoice(),
            ui.windows.InvoiceWindow(self.view),
            interactors.InvoiceInteractor()
        )

    def add_invoice(self, invoice):
        self.batch.add_invoice(invoice)
        self.view.add_invoice(invoice)
        
    def select_invoice(self):
        self.batch.select_invoice(self.view.get_selected_invoice())

    def hold_invoice(self):
        self.batch.current_invoice.set_flag(1)
        self.view.hold_invoice(self.view.get_selected_invoice())

    def accept_invoice(self):
        self.batch.current_invoice.set_flag(2)
        self.view.accept_invoice(self.view.get_selected_invoice())

    def remove_invoice(self):
        self.view.remove_invoice(self.view.get_selected_invoice())
        self.batch.remove_invoice(self.batch.current_invoice)
        self.batch.current_invoice = None

    def pay_invoices(self):
        self.batch.pay(self.payments)
        self.refresh_view()

    def create_nwo(self):
        self.batch.create_nwo()


class InvoiceFactoryPresenter(object):

    def __init__(self, parent, invoice_factory, view, interactor):
        self.invoice_factory = invoice_factory
        self.view = view
        interactor.install(parent, self, view)
        view.start()

    def create_invoice(self):
        self.invoice_factory.get_invoice(self.view.get_selected_invoice())
        return self.invoice_factory.make_invoice()

    def create_new_invoice(self):
        self.invoice_factory.create_new_invoice()

    def search_for_cutomers(self):
        self.view.set_customers(self.invoice_factory.get_customers(self.view.get_customer_number()))

    def search_for_invoices(self):
        self.view.set_invoices(self.invoice_factory.get_invoices(self.view.get_selected_customer()))
        

class InvoicePresenter(object):

    def __init__(self, parent, invoice, view, interactor):

        self.invoice = invoice
        self.view = view
        interactor.install(parent, self, view)
        view.start()
        self.refresh_view()

    def apply_changes(self):
        self.invoice.update \
        (
            self.view.get_contractor_alias(),
            self.view.get_vendor_invoice(),
            self.view.get_received_date()
        )
        self.refresh_view()

    def refresh(self):
        self.invoice.refresh()
        self.refresh_view()

    def refresh_view(self):
        
        self.view.delete_items()
        self.view.set_customer_name(self.invoice.get_customer_name())
        self.view.set_sales_cheque_number(self.invoice.get_sales_cheque_number())
        self.view.set_comm(self.invoice.get_comm())
        self.view.set_contractor_alias(self.invoice.get_contractor_alias())
        self.view.set_vendor_invoice(self.invoice.get_vendor_invoice())
        self.view.set_received_date(self.invoice.get_received_date())
        self.view.set_total_cost(self.invoice.get_total_cost())
        self.view.set_total_selling(self.invoice.get_total_selling())
        self.view.set_mark_up(self.invoice.get_mark_up())
        self.view.set_items(self.invoice.get_items())

    def update_contractor_alias(self, data):
        self.invoice.set_contractor_alias(data)

    def update_received_date(self, data):
        self.invoice.set_received_date(data)

    def update_vendor_invoice(self, data):
        self.invoice.set_vendor_invoice(data)

    def update_total_cost(self, data):
        self.invoice.set_total_cost(data)

    def update_total_selling(self, data):
        self.invoice.set_total_selling(data)

    def update_item(self, data):
        self.invoice.update_item(data)
        
    
