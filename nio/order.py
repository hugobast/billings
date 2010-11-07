import base


class List(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'OL  ')
        self.top, self.max = (8, 14)
        self.list_screen_item = ListItem

        self.customer_name = base.Field((5, 8, 33))
        self.sales_cheque_number = base.Field((5, 56, 9))
        self.total_cost = base.Field((6, 52, 10))
        self.total_selling = base.Field((6, 63, 10))

        self.add_field(self.customer_name)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.total_cost)
        self.add_field(self.total_selling)

class ListItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 14        

        self.comm = base.Field((self.index - self.offset, 4, 3))
        self.contractor_name = base.Field((self.index - self.offset, 8, 16))
        self.product_category = base.Field((self.index - self.offset, 25, 16))
        self.created_date = base.Field((self.index - self.offset, 42, 9))
        self.total_cost = base.Field((self.index - self.offset, 52, 10))
        self.total_selling = base.Field((self.index - self.offset, 63, 10))
        self.sell_unit = base.Field((self.index - self.offset, 74, 7))

        self.add_field(self.comm)
        self.add_field(self.contractor_name)
        self.add_field(self.product_category)
        self.add_field(self.created_date)
        self.add_field(self.total_cost)
        self.add_field(self.total_selling)
        self.add_field(self.sell_unit)

class ItemElementList(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'OIE ')
        self.top, self.max = (11, 11)
        self.list_screen_item = ItemElementListItem

        self.customer_name = base.Field((5, 8, 31))
        self.contractor_alias = base.Field((6, 8, 7))
        self.contractor_name = base.Field((6, 16, 30))
        self.sales_cheque_number = base.Field((5, 49, 9))
        self.status = base.Field((5, 61, 2))
        self.comm = base.Field((5, 67, 3))
        self.pricing_area = base.Field((7, 16, 2))
        self.sell_unit = base.Field((8, 16, 7))
        self.vendor_invoice = base.Field((7, 61, 20))
        self.received_date = base.Field((8, 61, 9))
        self.total_cost = base.Field((9, 52, 10))
        self.total_selling = base.Field((9, 63, 10))
        self.mark_up = base.Field((9, 74, 3))

        self.add_field(self.customer_name)
        self.add_field(self.contractor_alias)
        self.add_field(self.contractor_name)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.status)
        self.add_field(self.comm)
        self.add_field(self.pricing_area)
        self.add_field(self.sell_unit)
        self.add_field(self.vendor_invoice)
        self.add_field(self.received_date)
        self.add_field(self.total_cost)
        self.add_field(self.total_selling)
        self.add_field(self.mark_up)

    def nwo(self):
        self.command_input.set_text('NWO')
        self.enter()

    def nto(self):
        pass

    def no(self):
        pass

    def nmo(self):
        pass

class ItemElementListItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 11

        self.line_command = base.Field((self.index - self.offset, 2, 1))
        self.item_code = base.Field((self.index - self.offset, 6, 5))
        self.quantity = base.Field((self.index - self.offset, 12, 5))
        self.unit_of_measure = base.Field((self.index - self.offset, 18, 2))
        self.element = base.Field((self.index - self.offset, 21, 3))
        self.description = base.Field((self.index - self.offset, 25, 26))
        self.cost = base.Field((self.index - self.offset, 52, 10))
        self.selling = base.Field((self.index - self.offset, 63, 10))
        self.mark_up = base.Field((self.index - self.offset, 74, 3))

        self.add_field(self.item_code)
        self.add_field(self.quantity)
        self.add_field(self.unit_of_measure)
        self.add_field(self.element)
        self.add_field(self.description)
        self.add_field(self.cost)
        self.add_field(self.selling)
        self.add_field(self.mark_up)


class Accounts(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'OA  ')
        self.psap = base.Field((9, 46, 6))
        self.add_field(self.psap)


class Detail(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'OD  ')
        self.related_order = base.Field((6, 78, 3))
        self.add_field(self.related_order)
