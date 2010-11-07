import nio


def get_jobs(sales_cheque_number):

    nio.js.get_to()
    nio.js.clear()
    nio.js.sales_cheque_number.set_text(str(sales_cheque_number))
    nio.js.sell_unit.clear()
    nio.js.search()

    if nio.js.has_error():
        return None

    nio.jl.get_to()
    nio.jl.scrape()
    return nio.jl

def get_invoices(job_index):
    
    nio.jl.get_to()
    nio.jl.select(job_index)
    nio.ol.get_to()
    nio.ol.scrape()
    return nio.ol

def get_invoice(order_index):
    
    nio.ol.get_to()
    nio.ol.select(order_index)
    nio.oie.scrape()
    nio.oie.get_page('1')
    return nio.oie

def get_detail():

    nio.jd.get_to()
    nio.jd.scrape()
    return nio.jd


def ring_customer():

    nio.qd.get_to()
    nio.qd.search()

    if nio.qd.has_error():
        nio.qd.ring()
        return

    nio.ql.select()
    while not nio.qd.has_error():
        nio.qd.ring()
        nio.qd.next_page()

def is_customer_rung(comm):

    nio.qd.get_to()
    nio.qd.search()

    if nio.qd.has_error():
        nio.qd.scrape()
        if __match_comm(comm):
            if nio.qd.status.get_text()[0] == 'R':
                return True
            return False
        return True

    nio.ql.select()
    while not nio.qd.has_error():
        nio.qd.scrape()
        if __match_comm(comm):
            if nio.qd.status.get_text()[0] == 'R':
                return True
            return False
        nio.qd.next_page()
    return True

def __match_comm(comm):
    for item in nio.qd.items:
        if item.comm.get_text() == comm:
            return True
        return False

def post_comment(comment):

    nio.jhd.post('', 'N', comment)


def create_nwo(invoice):

    #FIX ME: Hide in nio library
    invoice.get_to()
    nio.oie.nwo()
    nio.od.related_order.set_text('G00')
    nio.od.save()
    nio.oie.clear()
    nio.oie.contractor_alias.set_text(invoice.get_contractor_alias())
    nio.oie.sell_unit.set_text(invoice.get_sell_unit())
    nio.oie.pricing_area.set_text('18')
    nio.oie.items[0].item_code.set_text('38998')
    nio.oie.items[0].quantity.set_text('1')
    nio.oie.items[1].line_command.set_text('C')
    nio.oie.items[1].quantity.set_text('1')
    nio.oie.items[1].element.set_text('000')
    nio.oie.items[1].cost.set_text('0.00')
    nio.oie.items[1].selling.set_text('0.00')
    nio.oie.save()
    nio.oa.psap.set_text('111430')
    nio.oa.save()

def create_invoice_from_factory(alias = '', amount = '0.00'):

    nio.ol.get_to()
    nio.ol.select(0)
    nio.oie.scrape()
    sell_unit = nio.oie.sell_unit.get_text()

    nio.oie.nwo()
    nio.od.related_order.set_text('G00')
    nio.od.save()
    nio.oie.clear()
    nio.oie.contractor_alias.set_text(alias)
    nio.oie.sell_unit.set_text(sell_unit)
    nio.oie.pricing_area.set_text('18')
    nio.oie.items[0].item_code.set_text('38998')
    nio.oie.items[0].quantity.set_text('1')
    nio.oie.items[1].line_command.set_text('C')
    nio.oie.items[1].quantity.set_text('1')
    nio.oie.items[1].element.set_text('000')
    nio.oie.items[1].cost.set_text('0.00')
    nio.oie.items[1].selling.set_text('0.00')
    nio.oie.enter()
    nio.oie.items[1].cost.set_text(amount)
    nio.oie.save()
    nio.oa.psap.set_text('111430')
    nio.oa.save()

def new_payment(invoices):

    if invoices == []:
        return

    nio.vd.make_new()
    nio.vd.contractor_alias.set_text(invoices[0].get_contractor_alias())
    nio.vd.show()
    nio.vd.scrape()
    
    invoices_from_nio = \
    [
        (
            n.sales_cheque_number.get_text(),
            n.vendor_invoice.get_text()
        )
        for n in nio.vd.items
    ]

    
    for invoice in invoices:
        nio.vd.select \
        (
            invoices_from_nio.index \
            (
                (invoice.get_sales_cheque_number(), invoice.get_vendor_invoice())
            )
        )
        if nio.vd.has_error():
          return invoice.sales_cheque_number.get_text()
        
        print invoice.get_sales_cheque_number()

    nio.vd.save()
    
    nio.vpd.make_new()
    nio.vpd.select()
    nio.vpd.save()
    nio.vpd.scrape()

    nio.vpd.command_input.set_text('P')
    nio.vpd.save()

    nio.vd.get_to()
    nio.vd.scrape()
    
    return nio.vd

