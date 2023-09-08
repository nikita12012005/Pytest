class PageObject:
    def __init__(self, driver):
        self.driver = driver
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle(self):
        if self.successor:
            self.successor.handle()
