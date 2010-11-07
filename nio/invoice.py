import base

class Detail(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'VD  ')
        self.top, self.max = (11, 11)
        self.new = 'NV  '

        self.list_screen_item = DetailItem

        self.contractor_alias = base.Field((5, 8, 7))
        self.contractor_name = base.Field((5, 16, 30))
        self.total = base.Field((7, 6, 10))
        self.gst = base.Field((8, 6, 10))
        self.pst = base.Field((9, 6, 10))
        self.created_date = base.Field((7, 29, 9))
        self.paid_date = base.Field((8, 29, 9))
        self.created_reference = base.Field((7, 39, 10))
        self.paid_reference = base.Field((8, 39, 10))

        self.add_field(self.contractor_alias)
        self.add_field(self.contractor_name)
        self.add_field(self.total)
        self.add_field(self.gst)
        self.add_field(self.pst)
        self.add_field(self.created_date)
        self.add_field(self.paid_date)
        self.add_field(self.created_reference)
        self.add_field(self.paid_reference)

class DetailItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 11

        self.amount = base.Field((self.index - self.offset, 6, 10))
        self.sales_cheque_number = base.Field((self.index - self.offset, 17, 9))
        self.comm = base.Field((self.index - self.offset, 27, 3))
        self.vendor_invoice = base.Field((self.index - self.offset, 31, 20))
        self.sell_unit = base.Field((self.index - self.offset, 52, 7))
        self.customer_name = base.Field((self.index - self.offset, 60, 21))

        self.add_field(self.amount)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.comm)
        self.add_field(self.vendor_invoice)
        self.add_field(self.sell_unit)
        self.add_field(self.customer_name)

class PaymentsDetail(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'VDP ')
        self.top, self.max = (11, 11)
        self.new = 'NVP '

        self.list_screen_item = PaymentsDetailItem

        self.contractor_alias = base.Field((5, 8, 7))
        self.contractor_name = base.Field((5, 16, 30))
        self.total = base.Field((7, 6, 10))
        self.gst = base.Field((8, 6, 10))
        self.pst = base.Field((9, 6, 10))
        self.created_date = base.Field((7, 29, 9))
        self.paid_date = base.Field((8, 29, 9))
        self.created_reference = base.Field((7, 39, 10))
        self.paid_reference = base.Field((8, 39, 10))

        self.add_field(self.contractor_alias)
        self.add_field(self.contractor_name)
        self.add_field(self.total)
        self.add_field(self.gst)
        self.add_field(self.pst)
        self.add_field(self.created_date)
        self.add_field(self.paid_date)
        self.add_field(self.created_reference)
        self.add_field(self.paid_reference)


class PaymentsDetailItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 11

        self.amount = base.Field((self.index - self.offset, 6, 10))
        self.date = base.Field((self.index - self.offset, 29, 9))
        self.number = base.Field((self.index - self.offset, 43, 10))

        self.add_field(self.amount)
        self.add_field(self.date)
        self.add_field(self.number)
        

        
