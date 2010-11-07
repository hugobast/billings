#FIX ME: Interactors uses threading to run long running macros, generates a
#pythonw.exe zombie on exit. Tried different approach and nothing works

#FIX ME: Numbers of total connect/disconnect for host is 26 threads... I need
#to replace threading with something else... wx.Yield ???

#FIX ME: Threading is too hard for me yet... hahaha

import presenters
import payment
import interactors
import ui.windows
import persistent

batch = persistent.Batch()
if batch is None:
    batch = payment.Batch()
    

batch_presenter = presenters.BatchPresenter \
(
    
    batch,
    payment.Payments(),
    ui.windows.BatchWindow(None),
    interactors.BatchInteractor()
    
)



    


