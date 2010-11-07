import base

class Detail(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'QD  ')
        self.top, self.max = (15, 4)
        self.new = 'NQ  '

        self.list_screen_item = DetailItem

        self.customer_phone = base.Field((6, 9, 12))
        self.sales_cheque_number = base.Field((6, 43, 9))
        self.status = base.Field((6, 64, 2))
        self.customer_name = base.Field((7, 8, 42))
        self.created_date = base.Field((7, 64, 9))
        self.sell_unit = base.Field((8, 15, 7))
        self.rung_date = base.Field((8, 64, 9))
        self.credit_approval_number = base.Field((9, 64, 6))
        self.how_paid = base.Field((11, 15, 2))
        self.account_number = base.Field((11, 41, 16))
        self.expiration_date = base.Field((11, 71 ,4))
        self.promise_date = base.Field((12, 15, 9))
        self.gst = base.Field((19, 7, 10))
        self.pst = base.Field((19, 23, 10))
        self.tax = base.Field((19, 41, 10))
        self.total = base.Field((20, 41, 10))
        self.rung_by = base.Field((21, 41, 10))

        self.add_field(self.customer_phone)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.status)
        self.add_field(self.customer_name)
        self.add_field(self.created_date)
        self.add_field(self.sell_unit)
        self.add_field(self.rung_date)
        self.add_field(self.credit_approval_number)
        self.add_field(self.how_paid)
        self.add_field(self.account_number)
        self.add_field(self.expiration_date)
        self.add_field(self.promise_date)
        self.add_field(self.gst)
        self.add_field(self.pst)
        self.add_field(self.tax)
        self.add_field(self.total)
        self.add_field(self.rung_by)

    def ring(self):
        self.status.set_text('RU')
        self.save()

    def ring_elsewhere(self):
        pass

    def ring_later(self):
        pass

    def unring(self):
        pass
    

class DetailItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 4

        self.division = base.Field((self.index - self.offset, 4, 3))
        self.item = base.Field((self.index - self.offset, 8, 5))
        self.article = base.Field((self.index - self.offset, 14, 3))
        self.quantity = base.Field((self.index - self.offset, 18, 3))
        self.description = base.Field((self.index - self.offset, 22, 17))
        self.price = base.Field((self.index - self.offset, 40, 10))
        self.taxes = base.Field((self.index - self.offset, 51, 2))
        self.promotion = base.Field((self.index - self.offset, 56, 10))
        self.discount = base.Field((self.index - self.offset, 67, 10))
        self.comm = base.Field((self.index - self.offset, 78, 3))
        
        self.add_field(self.division)
        self.add_field(self.item)
        self.add_field(self.article)
        self.add_field(self.quantity)
        self.add_field(self.description)
        self.add_field(self.price)
        self.add_field(self.taxes)
        self.add_field(self.promotion)
        self.add_field(self.discount)
        self.add_field(self.comm)

class List(base.ListScreen):
    
    def __init__(self):
        
        base.ListScreen.__init__(self, 'JL  ')
        self.top, self.max = (7, 16)
        self.list_screen_item = ListItem

            
class ListItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 16

