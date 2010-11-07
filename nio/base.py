import interface


_whlla = interface.WinHLLAPI()


class Field(object):

    def __init__(self, pos = (1, 1, 1)):
                    
        self.pos = pos
        self.text = ''

    def clear(self): _whlla.set_text(' ' * self.pos[2], self.pos)

    def get_text(self): return self.text.strip()

    def scrape(self): self.text = _whlla.get_text(self.pos)

    def sane(self):
        sane = ''; unsane = self.text.split()
        for u in unsane:
            sane += ' ' + u.capitalize()
        return sane.strip()
    
    def set_text(self, value):    
        self.clear()
        _whlla.set_text(value, self.pos)

    def to_int(self):
        return int(self.get_text())

    def update(self):
        self.set_text(self.text)
 

class Screen(object):
        
    def __init__(self, name):
        
        self.name = name
        self.new = ''
        self.fields = []

        self.command_input = Field((1, 2, 4))
        self.screen_id = Field((3, 2, 4))
        self.info_id = Field((22, 2, 3))
        self.info_flag = Field((22, 5, 1))
        self.info_desc = Field((22, 7, 74))
        
        self.add_field(self.command_input)
        self.add_field(self.screen_id)
        self.add_field(self.info_id)
        self.add_field(self.info_flag)
        self.add_field(self.info_desc)

    def add_field(self, field): self.fields.append(field)

    def clear(self): _whlla.command(interface.CLEAR)

    def get_to(self):
        self.screen_id.scrape()
        if self.screen_id.get_text() != self.name.strip():
            self.command_input.set_text(self.name)
            _whlla.command(interface.ENTER)

    def has_error(self):
        self.info_flag.scrape()
        if self.info_flag.get_text() == 'E':
            return True
        return False

    def is_list(self): return False

    def make_new(self):
        self.command_input.set_text(self.new)
        _whlla.command(interface.ENTER)

    def next_page(self): _whlla.command(interface.NEXT)

    def save(self): _whlla.command(interface.SAVE)

    def enter(self): _whlla.command(interface.ENTER)
    
    def scrape(self): self.scrape_fields()

    def scrape_fields(self):
        for field in self.fields: field.scrape()

    def search(self): _whlla.command(interface.SEARCH)        

    def show(self):
        self.command_input.set_text('SHOW')
        _whlla.command(interface.ENTER)


class ListScreen(Screen):

    def __init__(self, name):

        Screen.__init__(self, name)

        self.top = 0
        self.max = 0
        self.cursor = 0
        self.items = []
        
        self.list_screen_item = ListScreenItem
        
        self.current_page = Field((4, 71, 3))
        self.max_page = Field((4, 78, 3))

        self.add_field(self.current_page)
        self.add_field(self.max_page)

    def add_item(self, item):
        item.scrape()
        self.items.append(item)

    def eol(self):
        if _whlla.get_text((self.cursor, 1, 80)) == (str(' ') * 80):
            return True
        return False

    def get_item(self, pos):
        return self.items[pos[0]].fields[pos[1] + 5]
    
    def get_page(self, page):
        self.current_page.set_text(page)
        _whlla.command(interface.ENTER)
        
    def is_list(self): return True
        
    def next_page2(self): _whlla.command(interface.NEXTPAGE)

    def scrape(self):
        self.get_page('1')
        self.scrape_fields()
        self.scrape_items()

    def scrape_items(self):
        self.items = []
        for page in range(self.max_page.to_int()):
            self.cursor = self.top
            while (not self.eol()) and (self.cursor - self.top + 1<= self.max):
                self.add_item(self.list_screen_item(self.cursor + (page  * self.max), page))
                self.cursor += 1
            self.next_page2()
            
    def select(self, index = 0, action = 'S'):
        page = int(index / self.max) + 1
        i = index - ((page - 1) * self.max)
        self.get_page(str(page))
        _whlla.set_text(action, (self.top + i, 2))
        _whlla.command(interface.ENTER)

    def update_items(self):
        for index in range(len(self.items)):
            page = int(index / self.max) + 1
            if self.current_page.to_int() != page:
                self.get_page(str(page))
            for field in self.items[index].fields:
                field.update()


class ListScreenItem(Screen):

    def __init__(self, index, page = 0):
        Screen.__init__(self, '')
        self.index = index
        self.page = page
        
        
