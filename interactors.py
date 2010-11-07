from wx import *
from ui.custom_controls import EVT_EDITLIST


class BatchInteractor(object):

    def install(self, presenter, view):

        self.presenter = presenter
        self.view = view
        self.view.Bind(EVT_TOOL, self.add_invoice, view.add)
        self.view.Bind(EVT_TOOL, self.edit_invoice, view.edit)
        self.view.Bind(EVT_TOOL, self.hold_invoice, view.hold)
        self.view.Bind(EVT_TOOL, self.accept_invoice, view.accept)
        self.view.Bind(EVT_TOOL, self.remove_invoice, view.remove)
        self.view.Bind(EVT_TOOL, self.pay_invoices, view.pay)
        #self.view.Bind(EVT_TOOL, self.create_nwo, view.create_nwo)
        self.view.Bind(EVT_LIST_ITEM_SELECTED, self.select_invoice, view.invoices)
        self.view.invoices.Bind(EVT_LEFT_DCLICK, self.edit_invoice)
        self.view.Bind(EVT_CLOSE, self.close_and_pickle)

    def close_and_pickle(self, event):
        self.presenter.pickle_batch()
        self.view.close()

    def create_nwo(self, event):
        self.presenter.create_nwo()

    def add_invoice(self, event):
        self.presenter.start_add_invoice_dialog()

    def edit_invoice(self, event):
        self.presenter.start_edit_invoice_dialog()

    def select_invoice(self, event):
        self.presenter.select_invoice()

    def hold_invoice(self, event):
        self.presenter.hold_invoice()

    def accept_invoice(self, event):
        self.presenter.accept_invoice()

    def remove_invoice(self, event):
        self.presenter.remove_invoice()

    def pay_invoices(self, event):
        self.presenter.pay_invoices()


class InvoiceFactoryInteractor(object):

    def install(self, parent, presenter, view):

        self.parent = parent
        self.presenter = presenter
        self.view = view
        self.view.Bind(EVT_TOOL, self.add_invoice, view.add)
        self.view.Bind(EVT_TOOL, self.search_for_cutomers, view.search)
        self.view.Bind(EVT_TOOL, self.create_new_invoice, view.create)
        self.view.Bind(EVT_COMBOBOX, self.search_for_invoices, view.customers)
        self.view.Bind(EVT_CLOSE, self.close)

    def close(self, event = None):
        self.parent.refresh_view()
        self.view.close()

    def add_invoice(self, event = None):
        self.parent.add_invoice(self.presenter.create_invoice())
        self.close()

    def create_new_invoice(self, event = None):
        self.presenter.create_new_invoice()
        self.search_for_invoices()

    def search_for_cutomers(self, event = None):
        self.presenter.search_for_cutomers()
        self.view.disable_create()

    def search_for_invoices(self, event = None):
        self.presenter.search_for_invoices()
        self.view.enable_create()

class InvoiceInteractor(object):
    
    def install(self, parent, presenter, view):

        self.parent = parent
        self.presenter = presenter
        self.view = view
        self.view.Bind(EVT_TOOL, self.apply_changes, view.apply)
        self.view.Bind(EVT_TOOL, self.refresh, view.refresh)
        self.view.Bind(EVT_TOOL, self.exit, view.ok)
        self.view.Bind(EVT_EDITLIST, self.update_item, view.items)
        self.view.Bind(EVT_TEXT, self.update_contractor_alias, view.contractor_alias)
        self.view.Bind(EVT_TEXT, self.update_vendor_invoice, view.vendor_invoice)
        self.view.Bind(EVT_TEXT, self.update_received_date, view.received_date)
        self.view.Bind(EVT_TEXT, self.update_total_cost, view.total_cost)
        self.view.Bind(EVT_TEXT, self.update_total_selling, view.total_selling)
        self.view.Bind(EVT_CLOSE, self.close)

    def close(self, event = None):
        self.view.close()

    def exit(self, event = None):
        self.parent.refresh_view()
        self.close()
        
    def apply_changes(self, event = None):
        self.presenter.apply_changes()

    def refresh(self, event):
        self.presenter.refresh()

    def update_contractor_alias(self, event):
        self.presenter.update_contractor_alias(event.GetString())

    def update_received_date(self, event):
        self.presenter.update_received_date(event.GetString())

    def update_vendor_invoice(self, event):
        self.presenter.update_vendor_invoice(event.GetString())

    def update_total_cost(self, event):
        self.presenter.update_total_cost(event.GetString())

    def update_total_selling(self, event):
        self.presenter.update_total_selling(event.GetString())        
    
    def update_item(self, event):
        self.presenter.update_item(event.data)


class PaymentsInteractor(object):

    def install(self, presenter, view):

        self.presenter = presenter
        self.view = view
