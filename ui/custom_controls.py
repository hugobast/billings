from wx import *
import wx.lib.mixins.listctrl as mixins
import wx.lib.newevent as newevent

class List(ListCtrl, mixins.ListRowHighlighter, mixins.ListCtrlAutoWidthMixin):

    def __init__(self, parent, id, pos = DefaultPosition, size = DefaultSize, style = 0):

      ListCtrl.__init__(self, parent, id, pos, size, style)
      mixins.ListRowHighlighter.__init__(self)
      mixins.ListCtrlAutoWidthMixin.__init__(self)

class EditableList(List, mixins.TextEditMixin):

    def __init__(self, parent, id, pos = DefaultPosition, size = DefaultSize, style = 0):

        List.__init__(self, parent, id, pos, size, style)
        mixins.TextEditMixin.__init__(self)

    def SetStringItem(self, index, col, data):
        ListCtrl.SetStringItem(self, index, col, data)
        event = EditableListEvent(editlist_event_type, self.GetId(), (index, col, data))
        self.GetEventHandler().ProcessEvent(event)


editlist_event_type = NewEventType()
EVT_EDITLIST = PyEventBinder(editlist_event_type, 1)

class EditableListEvent(PyCommandEvent):

    def __init__(self, event_type, id, data):

        PyCommandEvent.__init__(self, event_type, id)
        self.data = data
