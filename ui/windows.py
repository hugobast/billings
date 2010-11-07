from wx import *
import custom_controls


app_title = 'Facturation Demo'

class BatchWindow(Frame):
  
    def __init__(self, parent, id = -1, title = app_title):
  
        self.app = PySimpleApp()
        Frame.__init__(self, parent, ID_ANY, title)

        icon = EmptyIcon()
        icon.CopyFromBitmap(Bitmap('icons/16x16/dollar_currency_sign.png'))
        self.SetIcon(icon)        

        self.panel = Panel(self)
        
        self.toolbar = self.CreateToolBar(style = TB_TEXT | NO_BORDER | TB_HORIZONTAL | TB_FLAT)
        self.add = self.toolbar.AddLabelTool(-1, 'Add', Bitmap('icons/24x24/add_item.png'), shortHelp = 'Add')
        self.remove = self.toolbar.AddLabelTool(-1, 'Remove', Bitmap('icons/24x24/remove_item.png'), shortHelp = 'Remove')
        self.toolbar.AddSeparator()
        self.pay = self.toolbar.AddLabelTool(-1, 'Pay', Bitmap('icons/24x24/dollar_currency_sign.png'), shortHelp = 'Pay')
        self.accept = self.toolbar.AddLabelTool(-1, 'Accept', Bitmap('icons/24x24/accept_item.png'), shortHelp = 'Accept')
        self.hold = self.toolbar.AddLabelTool(-1, 'Hold', Bitmap('icons/24x24/delete_item.png'), shortHelp = 'Hold')
        self.toolbar.AddSeparator()
        self.edit = self.toolbar.AddLabelTool(-1, 'Edit', Bitmap('icons/24x24/note.png'), shortHelp = 'Edit')
        #self.create_nwo = self.toolbar.AddLabelTool(-1, 'New Work', Bitmap('icons/24x24/attachment.png'), shortHelp = 'New Work Order')
        self.toolbar.Realize()

        self.images = ImageList(16, 16)
        self.yellowFlag = self.images.Add(Bitmap('icons/16x16/remove_item.png'))
        self.redFlag = self.images.Add(Bitmap('icons/16x16/delete_item.png'))
        self.greenFlag = self.images.Add(Bitmap('icons/16x16/accept_item.png'))

        self.invoices = custom_controls.EditableList(self.panel, -1, style = LC_REPORT | LC_SINGLE_SEL | BORDER_SIMPLE)
        self.invoices.SetHighlightColor(Color(240, 240, 240))
        self.invoices.InsertColumn(0, "St", width = 25)
        self.invoices.InsertColumn(1, "Number", width = 70)
        self.invoices.InsertColumn(2, "Ord", width = 40)
        self.invoices.InsertColumn(3, "Contractor", width = 100)
        self.invoices.InsertColumn(4, "Cost", width = 70)
        self.invoices.InsertColumn(5, "Sell", width = 70)
        self.invoices.InsertColumn(6, "Tot. M/U%", width = 70)
        self.invoices.InsertColumn(7, "Invoice #", width = 100)
        self.invoices.InsertColumn(8, "Date", width = 100)
        self.invoices.InsertColumn(9, "Notes")
        self.invoices.LockColumns(range(9))
        self.invoices.SetImageList(self.images, IMAGE_LIST_SMALL)

        self.payments = custom_controls.List(self.panel, -1, style = LC_REPORT | LC_SINGLE_SEL | BORDER_SIMPLE)
        self.payments.SetHighlightColor(Color(240, 240, 240))
        self.payments.InsertColumn(0, "Contractor", width = 175)
        self.payments.InsertColumn(1, "Amount", width = 70)
        self.payments.InsertColumn(2, "Date", width = 100)
        self.payments.InsertColumn(3, "Reference #1", width = 100)
        self.payments.InsertColumn(4, "Reference #1", width = 100)

        panel_sizer = BoxSizer(VERTICAL)
        panel_sizer.Add(self.invoices, 2, EXPAND)
        panel_sizer.AddSpacer(Size(10, 10))
        panel_sizer.Add(StaticText(self.panel, -1, ' Payments'), 0, EXPAND)
        panel_sizer.Add(self.payments, 1, EXPAND)
        self.panel.SetSizer(panel_sizer)
        
        sizer = BoxSizer()
        sizer.Add(self.panel, 1, EXPAND)
        self.SetSizer(sizer)
        self.Fit()

        self.SetSize(Size(800, 600))
        self.SetMinSize(Size(318, 91))
        self.CreateStatusBar()    


    def get_instance(self): return self

    def close(self, event = None):
        self.Destroy()
    
    def start(self):
        self.CenterOnScreen()
        self.Show()
        self.app.MainLoop()

    def add_invoice(self, invoice):

        pos = self.invoices.InsertImageItem(self.invoices.GetItemCount(), invoice.get_flag())
        self.invoices.SetStringItem(pos, 1, invoice.get_sales_cheque_number())
        self.invoices.SetStringItem(pos, 2, invoice.get_comm())
        self.invoices.SetStringItem(pos, 3, invoice.get_contractor_alias())
        self.invoices.SetStringItem(pos, 4, invoice.get_total_cost())
        self.invoices.SetStringItem(pos, 5, invoice.get_total_selling())
        self.invoices.SetStringItem(pos, 6, invoice.get_mark_up())
        self.invoices.SetStringItem(pos, 7, invoice.get_vendor_invoice())
        self.invoices.SetStringItem(pos, 8, invoice.get_received_date())
        self.invoices.SetStringItem(pos, 9, invoice.get_notes())
        self.invoices.RefreshRows() #to repaint the list highlights...

    def add_payment(self, payment):

        pos = self.payments.InsertStringItem(self.payments.GetItemCount(), payment.get_contractor_alias())
        self.payments.SetStringItem(pos, 1, payment.get_amount())
        self.payments.SetStringItem(pos, 2, payment.get_date())
        self.payments.SetStringItem(pos, 3, payment.get_ref_one())
        self.payments.SetStringItem(pos, 4, payment.get_ref_two())

    def hold_invoice(self, index):
        self.invoices.SetItemImage(index, self.redFlag)

    def accept_invoice(self, index):
        self.invoices.SetItemImage(index, self.greenFlag)

    def remove_invoice(self, index):
        self.invoices.DeleteItem(index)
        self.invoices.RefreshRows()

    def delete_invoices(self):
        self.invoices.DeleteAllItems()

    def delete_payments(self):
        self.payments.DeleteAllItems()

    def get_selected_invoice(self):
        return self.invoices.GetNextItem(-1, LIST_NEXT_ALL, LIST_STATE_SELECTED)

    def pay_invoices(self):
        pass
        

class InvoiceFactoryWindow(Frame):

    def __init__(self, parent, id = -1, title = app_title):

        Frame.__init__(self, parent, id, title, style =
                       FRAME_NO_TASKBAR
                       | FRAME_FLOAT_ON_PARENT
                       | DEFAULT_FRAME_STYLE
                       ^ RESIZE_BORDER
                       ^ MINIMIZE_BOX
                       ^ MAXIMIZE_BOX)

        icon = EmptyIcon()
        icon.CopyFromBitmap(Bitmap('icons/16x16/dollar_currency_sign.png'))
        self.SetIcon(icon)

        self.panel = Panel(self)
        color = self.panel.GetBackgroundColour()

        small_font = Font(7, 0, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL)

        self.toolbar = self.CreateToolBar(style = TB_TEXT | NO_BORDER | TB_HORIZONTAL | TB_FLAT)
        self.search = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/search_magnifier.png'), shortHelp = 'Search')
        self.add = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/add_item.png'), shortHelp = 'Add')
        self.toolbar.AddSeparator()
        self.create = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/attachment.png'), shortHelp = 'Create New')
        self.toolbar.Realize()
        self.toolbar.EnableTool(self.create.GetId(), False)
        
        self.customer_number = TextCtrl(self.panel, -1, '', size = (250, 15), style = BORDER_NONE)
        self.customer_number.SetBackgroundColour(color)
        self.customers = ComboBox(self.panel, -1, style = CB_READONLY)
        self.invoices = ComboBox(self.panel, -1, style = CB_READONLY)
        #self.contractor = TextCtrl(self.panel, -1, '', size = (150, 15), style = BORDER_NONE)
        #self.contractor.SetBackgroundColour(color)        
        #contractor = StaticText(self.panel, -1, 'Contractor Alias', style = ALIGN_RIGHT)
        #contractor.SetFont(small_font)
        #self.amount = TextCtrl(self.panel, -1, '', size = (150, 15), style = BORDER_NONE)
        #self.amount.SetBackgroundColour(color)
        #amount = StaticText(self.panel, -1, 'Total Amount $', style = ALIGN_RIGHT)
        #amount.SetFont(small_font)

        self.bag_sizer = GridBagSizer(1, 10)
        panel_sizer = BoxSizer(HORIZONTAL)

        spacer = Size(5, 5)

        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (0,  0), (1,  2), EXPAND       )
        self.bag_sizer.AddSpacer( spacer,                                                 (1,  0), (1,  2)               )
        self.bag_sizer.Add(       StaticText(self.panel, -1, 'Contract Number:'),         (2,  0), (1,  1),  ALIGN_CENTER_VERTICAL)
        self.bag_sizer.Add(       self.customer_number,                                   (2,  1), (1,  1)               )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (3,  0), (1,  2), EXPAND       )
        self.bag_sizer.AddSpacer( spacer,                                                 (4,  0), (1,  2)               )
        self.bag_sizer.Add(       self.customers,                                         (5,  0), (1,  2), EXPAND       )
        self.bag_sizer.AddSpacer( spacer,                                                 (6,  0), (1,  2)               )
        self.bag_sizer.Add(       self.invoices,                                          (7,  0), (1,  2), EXPAND       )
        self.bag_sizer.AddSpacer( spacer,                                                 (8,  0), (1,  2)               )
        #self.bag_sizer.Add(       self.contractor,                                        (9,  0), (1,  1),              )
        #self.bag_sizer.Add(       self.amount,                                            (9,  1), (1,  1),              )
        #self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (10, 0), (1,  1), EXPAND       )
        #self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (10, 1), (1,  1), EXPAND       )
        #self.bag_sizer.Add(       contractor,                                             (11, 0), (1,  1), EXPAND       )
        #self.bag_sizer.Add(       amount,                                                 (11, 1), (1,  1), EXPAND       )        
        #self.bag_sizer.AddSpacer( spacer,                                                 (12, 0), (1,  2)               )

        panel_sizer.AddSpacer(spacer)
        panel_sizer.Add(self.bag_sizer)
        panel_sizer.AddSpacer(spacer)
        self.panel.SetSizer(panel_sizer)
        
        sizer = BoxSizer()
        sizer.Add(self.panel, 1, EXPAND)
        self.SetSizer(sizer)
        self.Fit()

    def close(self, event = None):
        self.MakeModal(False)
        self.Destroy()

    def enable_create(self):
        self.toolbar.EnableTool(self.create.GetId(), True)

    def disable_create(self):
        self.toolbar.EnableTool(self.create.GetId(), False)

    def get_contractor(self):
        return self.contractor.GetValue()

    def get_amount(self):
        return self.amount.GetValue()

    def get_customer_number(self):
        return self.customer_number.GetValue()

    def get_selected_customer(self):
        return self.customers.GetCurrentSelection()

    def get_selected_invoice(self):
        return self.invoices.GetCurrentSelection()

    def set_customers(self, customers):
        self.customers.Clear()
        for customer in customers:
            self.customers.Append(str(customer[5:]))

    def set_invoices(self, invoices):
        self.invoices.Clear()
        for invoice in invoices:
            self.invoices.Append(str(invoice[5:]))
            
    def start(self):
        self.MakeModal(True)
        self.CenterOnParent()
        self.Show()


class InvoiceWindow(Frame):

    def __init__(self, parent, id = -1, title = app_title):


        Frame.__init__(self, parent, id, title, style =
                       FRAME_NO_TASKBAR
                       | FRAME_FLOAT_ON_PARENT
                       | DEFAULT_FRAME_STYLE
                       ^ RESIZE_BORDER
                       ^ MINIMIZE_BOX
                       ^ MAXIMIZE_BOX)
        
        icon = EmptyIcon()
        icon.CopyFromBitmap(Bitmap('icons/16x16/dollar_currency_sign.png'))
        self.SetIcon(icon)

        self.panel = Panel(self)
        color = self.panel.GetBackgroundColour()

        small_font = Font(7, 0, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL)
        bold_font = Font(8, 0, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)

        self.toolbar = self.CreateToolBar(style = TB_TEXT | NO_BORDER | TB_HORIZONTAL | TB_FLAT)
        self.ok = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/accept_item.png'), shortHelp = 'Close')
        self.apply = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/calculator.png'), shortHelp = 'Calculate And Save')
        self.refresh = self.toolbar.AddLabelTool(-1, '', Bitmap('icons/24x24/database_server.png'), shortHelp = 'Update From NIO')
        self.toolbar.Realize()

        customer_info = StaticText(self.panel, -1, 'Customer Info:')
        customer_info.SetFont(bold_font)
        customer_name = StaticText(self.panel, -1, 'Name', style = ALIGN_RIGHT)
        customer_name.SetFont(small_font)
        sales_cheque_number = StaticText(self.panel, -1, 'Number', style = ALIGN_RIGHT)
        sales_cheque_number.SetFont(small_font)
        comm = StaticText(self.panel, -1, 'Order #', style = ALIGN_RIGHT)
        comm.SetFont(small_font)
        contractor_info = StaticText(self.panel, -1, 'Contractor Info:')
        contractor_info.SetFont(bold_font)
        contractor_alias = StaticText(self.panel, -1, 'Alias', style = ALIGN_RIGHT)
        contractor_alias.SetFont(small_font)
        vendor_invoice = StaticText(self.panel, -1, 'Invoice', style = ALIGN_RIGHT)
        vendor_invoice.SetFont(small_font)
        received_date = StaticText(self.panel, -1, 'Date Received', style = ALIGN_RIGHT)
        received_date.SetFont(small_font)
        total_cost = StaticText(self.panel, -1, 'Total Cost', style = ALIGN_RIGHT)
        total_cost.SetFont(small_font)
        total_selling = StaticText(self.panel, -1, 'Total Selling', style = ALIGN_RIGHT)
        total_selling.SetFont(small_font)
        mark_up = StaticText(self.panel, -1, 'Final Markup', style = ALIGN_RIGHT)
        mark_up.SetFont(small_font)

        self.customer_name = TextCtrl(self.panel, -1, size = (230, 14), style = BORDER_NONE | TE_READONLY)
        self.customer_name.SetBackgroundColour(color)
        self.contractor_alias = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE)
        self.contractor_alias.SetBackgroundColour(color)
        self.sales_cheque_number = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE | TE_READONLY)
        self.sales_cheque_number.SetBackgroundColour(color)
        self.comm = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE | TE_READONLY)
        self.comm.SetBackgroundColour(color)
        self.vendor_invoice = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE)
        self.vendor_invoice.SetBackgroundColour(color)
        self.received_date = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE)
        self.received_date.SetBackgroundColour(color)
        self.total_cost = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE | TE_RIGHT)
        self.total_cost.SetBackgroundColour(color)
        self.total_selling = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE | TE_READONLY | TE_RIGHT)
        self.total_selling.SetBackgroundColour(color)
        self.mark_up = TextCtrl(self.panel, -1, size = (115, 14), style = BORDER_NONE | TE_READONLY | TE_RIGHT)
        self.mark_up.SetBackgroundColour(color)

        self.items = custom_controls.EditableList(self.panel, -1, style = LC_REPORT | LC_SINGLE_SEL)
        self.items.SetHighlightColor(Color(240, 240, 240))
        self.items.InsertColumn(0, "Item", width = 40)
        self.items.InsertColumn(1, "Qty", LIST_FORMAT_RIGHT, width = 30)
        self.items.InsertColumn(2, "UOM", width = 35)
        self.items.InsertColumn(3, "Ele", width = 30)
        self.items.InsertColumn(4, "Description", width = 200)
        self.items.InsertColumn(5, "Cost", LIST_FORMAT_RIGHT, width = 60)
        self.items.InsertColumn(6, "Sell", LIST_FORMAT_RIGHT, width = 60)
        self.items.InsertColumn(7, "M/U", LIST_FORMAT_RIGHT, width = 30)
        self.items.LockColumns([0, 2, 3, 4, 7])


        spacer = Size(10, 10)
        self.bag_sizer = GridBagSizer(1, 10)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (0,  0), (1,  4), flag = EXPAND)
        self.bag_sizer.AddSpacer( spacer,                                                 (1,  0), (1,  4)               )
        self.bag_sizer.Add(       customer_info,                                          (2,  0), (1,  4)               )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (3,  0), (1,  4), flag = EXPAND)
        self.bag_sizer.AddSpacer( spacer,                                                 (4,  0), (1,  4)               )
        self.bag_sizer.Add(       self.customer_name,                                     (5,  0), (1,  2)               )
        self.bag_sizer.Add(       self.sales_cheque_number,                               (5,  2)                        )
        self.bag_sizer.Add(       self.comm,                                              (5,  3)                        )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (6,  0), (1,  2), flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (6,  2),          flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (6,  3),          flag = EXPAND)
        self.bag_sizer.Add(       customer_name,                                          (7,  0), (1,  2), flag = EXPAND)
        self.bag_sizer.Add(       sales_cheque_number,                                    (7,  2),          flag = EXPAND)
        self.bag_sizer.Add(       comm,                                                   (7,  3),          flag = EXPAND)
        self.bag_sizer.AddSpacer( spacer,                                                 (8,  0)                        )
        self.bag_sizer.Add(       contractor_info,                                        (9,  0)                        )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (10, 0), (1,  4), flag = EXPAND)
        self.bag_sizer.AddSpacer( spacer,                                                 (11, 0), (1,  4)               )
        self.bag_sizer.Add(       self.contractor_alias,                                  (12, 0)                        )
        self.bag_sizer.Add(       self.vendor_invoice,                                    (12, 1)                        )
        self.bag_sizer.Add(       self.received_date,                                     (12, 2)                        )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (13, 0),          flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (13, 1),          flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (13, 2),          flag = EXPAND)
        self.bag_sizer.Add(       contractor_alias,                                       (14, 0),          flag = EXPAND)
        self.bag_sizer.Add(       vendor_invoice,                                         (14, 1),          flag = EXPAND)
        self.bag_sizer.Add(       received_date,                                          (14, 2),          flag = EXPAND)
        self.bag_sizer.Add(       self.items,                                             (16, 0), (11, 4), flag = EXPAND)
        self.bag_sizer.Add(       self.total_cost,                                        (28, 1)                        )
        self.bag_sizer.Add(       self.total_selling,                                     (28, 2)                        )
        self.bag_sizer.Add(       self.mark_up,                                           (28, 3)                        )
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (29, 1),          flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (29, 2),          flag = EXPAND)
        self.bag_sizer.Add(       StaticLine(self.panel, -1, style = LI_HORIZONTAL),      (29, 3),          flag = EXPAND)
        self.bag_sizer.Add(       total_cost,                                             (30, 1),          flag = EXPAND)
        self.bag_sizer.Add(       total_selling,                                          (30, 2),          flag = EXPAND)
        self.bag_sizer.Add(       mark_up,                                                (30, 3),          flag = EXPAND)
        self.bag_sizer.AddSpacer( spacer,                                                 (31, 0)                        )

        spacer = Size(5, 5)
        self.panel_sizer = BoxSizer(VERTICAL)
        self.panel_sizer.Add(self.bag_sizer, 0, EXPAND)
        self.panel_sizer.AddSpacer(spacer)
        self.panel.SetSizer(self.panel_sizer)
        
        sizer = BoxSizer()
        sizer.Add(self.panel, 1, EXPAND)
        self.SetSizer(sizer)
        self.Fit()

    def close(self, event = None):
        self.MakeModal(False)
        self.Destroy()

    def delete_items(self):
        self.items.DeleteAllItems()

    def get_contractor_alias(self):
        return self.contractor_alias.GetValue()

    def get_vendor_invoice(self):
        return self.vendor_invoice.GetValue()

    def get_received_date(self):
        return self.received_date.GetValue()
        
    def set_customer_name(self, customer_name):
        self.customer_name.SetValue(customer_name)
    
    def set_sales_cheque_number(self, sales_cheque_number):
        self.sales_cheque_number.SetValue(sales_cheque_number)
    
    def set_comm(self, comm):
        self.comm.SetValue(comm)
    
    def set_contractor_alias(self, contractor_alias):
        self.contractor_alias.SetValue(contractor_alias)
    
    def set_vendor_invoice(self, vendor_invoice):
        self.vendor_invoice.SetValue(vendor_invoice)
    
    def set_received_date(self, received_date):
        self.received_date.SetValue(received_date)
    
    def set_total_cost(self, total_cost):
        self.total_cost.SetValue(total_cost)
    
    def set_total_selling(self, total_selling):
        self.total_selling.SetValue(total_selling)
    
    def set_mark_up(self, mark_up):
        self.mark_up.SetValue(mark_up)

    def set_items(self, items):
        for item in items:
            ref = self.items.InsertStringItem(self.items.GetItemCount(), item[5])
            self.items.SetStringItem(ref, 1, item[6])
            self.items.SetStringItem(ref, 2, item[7])
            self.items.SetStringItem(ref, 3, item[8])
            self.items.SetStringItem(ref, 4, item[9])
            self.items.SetStringItem(ref, 5, item[10])
            self.items.SetStringItem(ref, 6, item[11])
            self.items.SetStringItem(ref, 7, item[12])
            
            if item[5]:
                self.items.LockRows([ref, ])
        self.items.RefreshRows()

    def start(self):
        self.MakeModal(True)
        self.CenterOnParent()
        self.Show()

        

class PleaseWait(Frame):

    def __init__(self, parent, id = -1, title = ''):

        Frame.__init__(self, parent, id, title, style =
                       FRAME_NO_TASKBAR
                       | FRAME_FLOAT_ON_PARENT
                       | DEFAULT_FRAME_STYLE
                       ^ RESIZE_BORDER
                       ^ MINIMIZE_BOX
                       ^ MAXIMIZE_BOX
                       ^ CAPTION)
        

        StaticText(self, -1, '   Working...   ')

        self.Fit()
        self.CenterOnParent()
        self.Show()
        self.Update()
        
    def close(self, event = None):
        self.Destroy()

if __name__ == '__main__':

    app = App(0)
    b = BatchWindow(None)
    i = InvoiceWindow(b)
    PleaseWait(i)
    app.MainLoop()
    app.Destroy()
    
