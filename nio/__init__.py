import job
import order
import cheque
import invoice
import interface

interface.WinHLLAPI().connect()

js = job.Search()
jl = job.List()
jhl = job.HistoryList()
jhd = job.HistoryDetail()
jd = job.Detail()

ol = order.List()
oie = order.ItemElementList()
oa = order.Accounts()
od = order.Detail()

vd = invoice.Detail()
vpd = invoice.PaymentsDetail()

qd = cheque.Detail()
ql = cheque.List()
