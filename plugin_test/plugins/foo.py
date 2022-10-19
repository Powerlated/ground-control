import dearpygui.dearpygui as gui
from . import base_plugin

class Plugin(base_plugin.Plugin):
    def __init__(self) -> None:
        super().__init__(identifier='foo')

    def process(gui):
        pass