import dearpygui.dearpygui as gui
import os
import plugins.base_plugin
import importlib

gui.create_context()
gui.create_viewport(title='Custom Title', width=600, height=300)

with gui.window(label="Example Window"):
    gui.add_text("Hello, world")
    gui.add_button(label="Save")
    gui.add_input_text(label="string", default_value="Quick brown fox")
    gui.add_slider_float(label="float", default_value=0.273, max_value=1)

gui.setup_dearpygui()
gui.show_viewport()

# Import plugins:
plugin_names = [
    'bar',
    'foo',
]
# plugin_names: list[str] = os.listdir('plugins/')
# plugin_names = list(filter(lambda x: x.endswith('.py'), plugin_names))
# plugin_names = list(filter(lambda x: x != 'base_plugin.py', plugin_names))
# print(plugin_names)

plugin_instances: list[plugins.base_plugin.Plugin] = []
for plugin_name in plugin_names:
    plugin_module = importlib.import_module(f'plugins.{plugin_name}', '.')
    plugin_instance = plugin_module.Plugin()
    # plugin_instances.append(plugin_instance)

# Main process loop:
while gui.is_dearpygui_running():

    gui.render_dearpygui_frame()


gui.destroy_context()