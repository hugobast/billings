import base


class Search(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'JS  ')

        self.customer_phone_number = base.Field((7, 46, 12))
        self.status_code = base.Field((8, 46, 2))
        self.written_date_from = base.Field((9, 46, 9))
        self.written_date_to = base.Field((9, 61, 9))
        self.complete_date_from = base.Field((10, 46, 9))
        self.complete_date_to = base.Field((10, 61, 9))
        self.contractor_alias = base.Field((11, 46, 7))
        self.product_category = base.Field((12, 46, 3))
        self.sales_cheque_number = base.Field((13, 46, 9))
        self.sell_unit = base.Field((16, 46, 7))
        self.perf_unit = base.Field((17, 46, 7))

        self.add_field(self.customer_phone_number)    
        self.add_field(self.status_code)
        self.add_field(self.written_date_from)
        self.add_field(self.written_date_to)
        self.add_field(self.complete_date_from)
        self.add_field(self.complete_date_to)
        self.add_field(self.contractor_alias)
        self.add_field(self.product_category)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.sell_unit)
        self.add_field(self.perf_unit)


class List(base.ListScreen):
    
    def __init__(self):
        
        base.ListScreen.__init__(self, 'JL  ')
        self.top, self.max = (6, 16)
        self.list_screen_item = ListItem
            
class ListItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 16

        self.customer_name = base.Field((self.index - self.offset, 4, 20))
        self.address = base.Field((self.index - self.offset, 25, 30))
        self.product_category = base.Field((self.index - self.offset, 57, 3))
        self.status_code = base.Field((self.index - self.offset, 61, 2))
        self.written_date = base.Field((self.index - self.offset, 64, 9))
        self.contractor_alias = base.Field((self.index - self.offset, 74, 7))

        self.add_field(self.customer_name)
        self.add_field(self.address)
        self.add_field(self.product_category)
        self.add_field(self.status_code)
        self.add_field(self.written_date)
        self.add_field(self.contractor_alias)

class Detail(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'JD  ')

        self.customer_name = base.Field((5, 9, 35))
        self.sales_cheque_number = base.Field((5, 50, 9))
        self.status_code = base.Field((5, 68, 2))
        self.perf_unit = base.Field((6, 9, 7))
        self.sell_unit = base.Field((12, 14, 7))
        self.product_category = base.Field((6, 60, 3))
        self.sales_person_id = base.Field((11, 12, 7))
        
        self.cheque_created_date = base.Field((11, 72, 9))
        self.sale_written_date = base.Field((12, 72, 9))
        self.installed_date = base.Field((13, 72, 9))
        self.completed_date = base.Field((14, 72, 9))
        self.approved_date = base.Field((15, 72, 9))
        self.original_completion_date = base.Field((16, 72, 9))
        self.satisfaction_date = base.Field((17, 72, 9))
        self.initial_contact_date = base.Field((18, 72, 9))
        self.delinquent_date = base.Field((19, 72, 9))
        self.promised_date = base.Field((20, 72, 9))
        self.revised_date = base.Field((21, 72, 9))

        self.initial_cost = base.Field((15, 14, 10))
        self.adjusted_cost = base.Field((16, 14, 10))
        self.work_order_cost = base.Field((17, 14, 10))
        self.warranty_work_cost = base.Field((18, 14, 10))
        self.total_cost = base.Field((19, 14, 10))
        self.final_cost = base.Field((20, 14, 10))

        self.initial_selling = base.Field((15, 25, 10))
        self.adjusted_selling = base.Field((16, 25, 10))
        self.work_order_selling = base.Field((17, 25, 10))
        self.warranty_work_selling = base.Field((18, 25, 10))
        self.total_selling = base.Field((19, 25, 10))
        self.final_selling = base.Field((20, 25, 10))

        self.initial_mark_up = base.Field((15, 36, 3))
        self.final_mark_up = base.Field((20, 36, 3))

        self.add_field(self.customer_name)
        self.add_field(self.sales_cheque_number)
        self.add_field(self.status_code)
        self.add_field(self.perf_unit)
        self.add_field(self.sell_unit)
        self.add_field(self.product_category)
        self.add_field(self.sales_person_id)
        
        self.add_field(self.cheque_created_date)
        self.add_field(self.sale_written_date)
        self.add_field(self.installed_date)
        self.add_field(self.completed_date)
        self.add_field(self.approved_date)
        self.add_field(self.original_completion_date)
        self.add_field(self.satisfaction_date)
        self.add_field(self.initial_contact_date)
        self.add_field(self.delinquent_date)
        self.add_field(self.promised_date)
        self.add_field(self.revised_date)

        self.add_field(self.initial_cost)
        self.add_field(self.adjusted_cost)
        self.add_field(self.work_order_cost)
        self.add_field(self.warranty_work_cost)
        self.add_field(self.total_cost)
        self.add_field(self.final_cost)

        self.add_field(self.initial_selling)
        self.add_field(self.adjusted_selling)
        self.add_field(self.work_order_selling)
        self.add_field(self.warranty_work_selling)
        self.add_field(self.total_selling)
        self.add_field(self.final_selling)

        self.add_field(self.initial_mark_up)
        self.add_field(self.final_mark_up)

class HistoryList(base.ListScreen):

    def __init__(self):

        base.ListScreen.__init__(self, 'JHL ')
        self.top, self.max = (9, 13)
        self.list_screen_item = HistoryListItem

        

class HistoryListItem(base.ListScreenItem):

    def __init__(self, index, page = 0):

        base.ListScreenItem.__init__(self, index, page)
        self.offset = self.page * 13

        self.text = base.Field((self.index - self.offset, 4, 54))
        self.comm = base.Field((self.index - self.offset, 59, 3))
        self.status = base.Field((self.index - self.offset, 63, 2))
        self.reason = base.Field((self.index - self.offset, 66, 2))
        self.updated_date = base.Field((self.index - self.offset, 69, 9))
        self.print_flag = base.Field((self.index - self.offset, 79, 1))

        self.add_field(self.text)
        self.add_field(self.comm)
        self.add_field(self.status)
        self.add_field(self.reason)
        self.add_field(self.updated_date)
        self.add_field(self.print_flag)


class HistoryDetail(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'JHD  ')
        self.new = 'NJH'

        self.comm = base.Field((5, 29, 3))
        self.print_flag = base.Field((8, 73, 1))
        self.lines = []
        self.lines.append(base.Field((10, 4, 77)))
        self.lines.append(base.Field((11, 4, 77)))
        self.lines.append(base.Field((12, 4, 77)))
        self.lines.append(base.Field((13, 4, 77)))
        self.lines.append(base.Field((14, 4, 77)))
        self.lines.append(base.Field((15, 4, 77)))
        self.lines.append(base.Field((16, 4, 77)))
        self.lines.append(base.Field((17, 4, 77)))
        self.lines.append(base.Field((18, 4, 77)))
        self.lines.append(base.Field((19, 4, 77)))
        self.lines.append(base.Field((20, 4, 77)))
        self.lines.append(base.Field((21, 4, 77)))
        

    def post(self, comm, print_flag, comment):

        #FIX ME: Make it better...
        
        self.make_new()
        self.comm.set_text(comm)
        self.print_flag.set_text(print_flag)
        
        i = 0
        for line in comment:
            self.lines[i].set_text(line)
            i += 1

        self.save()


class CustomerDetail(base.Screen):

    def __init__(self):

        base.Screen.__init__(self, 'JCD ')





