import allure
import inspect


def auto_step(cls):
    for name, func in inspect.getmembers(cls):
        if inspect.isfunction(func) and not name.startswith('_'):
            setattr(cls, name, allure.step(func))
    return cls


@auto_step
class YourPageObject:
    def perform_step(self):
        pass
