"""
Utility code for dearpygui themes.
"""

import enum
import dearpygui.dearpygui as gui
import toml

class ThemeException(Exception):
    pass

def is_color(value) -> bool:
    if isinstance(value, list) and len(value) == 4:
        for idx in range(4):
            if not (isinstance(value[idx], float) and value[idx] >= 0.0 and value[idx] <= 1.0):
                return False
        return True
    return False

class ThemeValueDataType(enum.Enum):
    COLOR = 0
    INT = 1
    FLOAT = 2
    VECTOR_2D = 3

class ThemeValueType(enum.Enum):
    COLOR = 0
    STYLE = 1


THEME_CONSTANTS_INFO = {
    'Color_Text'                  : (ThemeValueType.COLOR, gui.mvThemeCol_Text                   ),
    'Color_TextDisabled'          : (ThemeValueType.COLOR, gui.mvThemeCol_TextDisabled           ),
    'Color_WindowBg'              : (ThemeValueType.COLOR, gui.mvThemeCol_WindowBg               ),
    'Color_ChildBg'               : (ThemeValueType.COLOR, gui.mvThemeCol_ChildBg                ),
    'Color_PopupBg'               : (ThemeValueType.COLOR, gui.mvThemeCol_PopupBg                ),
    'Color_Border'                : (ThemeValueType.COLOR, gui.mvThemeCol_Border                 ),
    'Color_BorderShadow'          : (ThemeValueType.COLOR, gui.mvThemeCol_BorderShadow           ),
    'Color_FrameBg'               : (ThemeValueType.COLOR, gui.mvThemeCol_FrameBg                ),
    'Color_FrameBgHovered'        : (ThemeValueType.COLOR, gui.mvThemeCol_FrameBgHovered         ),
    'Color_FrameBgActive'         : (ThemeValueType.COLOR, gui.mvThemeCol_FrameBgActive          ),
    'Color_TitleBg'               : (ThemeValueType.COLOR, gui.mvThemeCol_TitleBg                ),
    'Color_TitleBgActive'         : (ThemeValueType.COLOR, gui.mvThemeCol_TitleBgActive          ),
    'Color_TitleBgCollapsed'      : (ThemeValueType.COLOR, gui.mvThemeCol_TitleBgCollapsed       ),
    'Color_MenuBarBg'             : (ThemeValueType.COLOR, gui.mvThemeCol_MenuBarBg              ),
    'Color_ScrollbarBg'           : (ThemeValueType.COLOR, gui.mvThemeCol_ScrollbarBg            ),
    'Color_ScrollbarGrab'         : (ThemeValueType.COLOR, gui.mvThemeCol_ScrollbarGrab          ),
    'Color_ScrollbarGrabHovered'  : (ThemeValueType.COLOR, gui.mvThemeCol_ScrollbarGrabHovered   ),
    'Color_ScrollbarGrabActive'   : (ThemeValueType.COLOR, gui.mvThemeCol_ScrollbarGrabActive    ),
    'Color_CheckMark'             : (ThemeValueType.COLOR, gui.mvThemeCol_CheckMark              ),
    'Color_SliderGrab'            : (ThemeValueType.COLOR, gui.mvThemeCol_SliderGrab             ),
    'Color_SliderGrabActive'      : (ThemeValueType.COLOR, gui.mvThemeCol_SliderGrabActive       ),
    'Color_Button'                : (ThemeValueType.COLOR, gui.mvThemeCol_Button                 ),
    'Color_ButtonHovered'         : (ThemeValueType.COLOR, gui.mvThemeCol_ButtonHovered          ),
    'Color_ButtonActive'          : (ThemeValueType.COLOR, gui.mvThemeCol_ButtonActive           ),
    'Color_Header'                : (ThemeValueType.COLOR, gui.mvThemeCol_Header                 ),
    'Color_HeaderHovered'         : (ThemeValueType.COLOR, gui.mvThemeCol_HeaderHovered          ),
    'Color_HeaderActive'          : (ThemeValueType.COLOR, gui.mvThemeCol_HeaderActive           ),
    'Color_Separator'             : (ThemeValueType.COLOR, gui.mvThemeCol_Separator              ),
    'Color_SeparatorHovered'      : (ThemeValueType.COLOR, gui.mvThemeCol_SeparatorHovered       ),
    'Color_SeparatorActive'       : (ThemeValueType.COLOR, gui.mvThemeCol_SeparatorActive        ),
    'Color_ResizeGrip'            : (ThemeValueType.COLOR, gui.mvThemeCol_ResizeGrip             ),
    'Color_ResizeGripHovered'     : (ThemeValueType.COLOR, gui.mvThemeCol_ResizeGripHovered      ),
    'Color_ResizeGripActive'      : (ThemeValueType.COLOR, gui.mvThemeCol_ResizeGripActive       ),
    'Color_Tab'                   : (ThemeValueType.COLOR, gui.mvThemeCol_Tab                    ),
    'Color_TabHovered'            : (ThemeValueType.COLOR, gui.mvThemeCol_TabHovered             ),
    'Color_TabActive'             : (ThemeValueType.COLOR, gui.mvThemeCol_TabActive              ),
    'Color_TabUnfocused'          : (ThemeValueType.COLOR, gui.mvThemeCol_TabUnfocused           ),
    'Color_TabUnfocusedActive'    : (ThemeValueType.COLOR, gui.mvThemeCol_TabUnfocusedActive     ),
    'Color_DockingPreview'        : (ThemeValueType.COLOR, gui.mvThemeCol_DockingPreview         ),
    'Color_DockingEmptyBg'        : (ThemeValueType.COLOR, gui.mvThemeCol_DockingEmptyBg         ),
    'Color_PlotLines'             : (ThemeValueType.COLOR, gui.mvThemeCol_PlotLines              ),
    'Color_PlotLinesHovered'      : (ThemeValueType.COLOR, gui.mvThemeCol_PlotLinesHovered       ),
    'Color_PlotHistogram'         : (ThemeValueType.COLOR, gui.mvThemeCol_PlotHistogram          ),
    'Color_PlotHistogramHovered'  : (ThemeValueType.COLOR, gui.mvThemeCol_PlotHistogramHovered   ),
    'Color_TableHeaderBg'         : (ThemeValueType.COLOR, gui.mvThemeCol_TableHeaderBg          ),
    'Color_TableBorderStrong'     : (ThemeValueType.COLOR, gui.mvThemeCol_TableBorderStrong      ),
    'Color_TableBorderLight'      : (ThemeValueType.COLOR, gui.mvThemeCol_TableBorderLight       ),
    'Color_TableRowBg'            : (ThemeValueType.COLOR, gui.mvThemeCol_TableRowBg             ),
    'Color_TableRowBgAlt'         : (ThemeValueType.COLOR, gui.mvThemeCol_TableRowBgAlt          ),
    'Color_TextSelectedBg'        : (ThemeValueType.COLOR, gui.mvThemeCol_TextSelectedBg         ),
    'Color_DragDropTarget'        : (ThemeValueType.COLOR, gui.mvThemeCol_DragDropTarget         ),
    'Color_NavHighlight'          : (ThemeValueType.COLOR, gui.mvThemeCol_NavHighlight           ),
    'Color_NavWindowingHighlight' : (ThemeValueType.COLOR, gui.mvThemeCol_NavWindowingHighlight  ),
    'Color_NavWindowingDimBg'     : (ThemeValueType.COLOR, gui.mvThemeCol_NavWindowingDimBg      ),
    'Color_ModalWindowDimBg'      : (ThemeValueType.COLOR, gui.mvThemeCol_ModalWindowDimBg       ),

    'PlotColor_Line'            : (ThemeValueType.COLOR, gui.mvPlotCol_Line),
    'PlotColor_Fill'            : (ThemeValueType.COLOR, gui.mvPlotCol_Fill),
    'PlotColor_MarkerOutline'   : (ThemeValueType.COLOR, gui.mvPlotCol_MarkerOutline),
    'PlotColor_MarkerFill'      : (ThemeValueType.COLOR, gui.mvPlotCol_MarkerFill),
    'PlotColor_ErrorBar'        : (ThemeValueType.COLOR, gui.mvPlotCol_ErrorBar),
    'PlotColor_FrameBg'         : (ThemeValueType.COLOR, gui.mvPlotCol_FrameBg),
    'PlotColor_PlotBg'          : (ThemeValueType.COLOR, gui.mvPlotCol_PlotBg),
    'PlotColor_PlotBorder'      : (ThemeValueType.COLOR, gui.mvPlotCol_PlotBorder),
    'PlotColor_LegendBg'        : (ThemeValueType.COLOR, gui.mvPlotCol_LegendBg),
    'PlotColor_LegendBorder'    : (ThemeValueType.COLOR, gui.mvPlotCol_LegendBorder),
    'PlotColor_LegendText'      : (ThemeValueType.COLOR, gui.mvPlotCol_LegendText),
    'PlotColor_TitleText'       : (ThemeValueType.COLOR, gui.mvPlotCol_TitleText),
    'PlotColor_InlayText'       : (ThemeValueType.COLOR, gui.mvPlotCol_InlayText),
    'PlotColor_XAxis'           : (ThemeValueType.COLOR, gui.mvPlotCol_XAxis),
    'PlotColor_XAxisGrid'       : (ThemeValueType.COLOR, gui.mvPlotCol_XAxisGrid),
    'PlotColor_YAxis'           : (ThemeValueType.COLOR, gui.mvPlotCol_YAxis),
    'PlotColor_YAxisGrid'       : (ThemeValueType.COLOR, gui.mvPlotCol_YAxisGrid),
    'PlotColor_YAxis2'          : (ThemeValueType.COLOR, gui.mvPlotCol_YAxis2),
    'PlotColor_YAxisGrid2'      : (ThemeValueType.COLOR, gui.mvPlotCol_YAxisGrid2),
    'PlotColor_YAxis3'          : (ThemeValueType.COLOR, gui.mvPlotCol_YAxis3),
    'PlotColor_YAxisGrid3'      : (ThemeValueType.COLOR, gui.mvPlotCol_YAxisGrid3),
    'PlotColor_Selection'       : (ThemeValueType.COLOR, gui.mvPlotCol_Selection),
    'PlotColor_Query'           : (ThemeValueType.COLOR, gui.mvPlotCol_Query),
    'PlotColor_Crosshairs'      : (ThemeValueType.COLOR, gui.mvPlotCol_Crosshairs),

    'NodeColor_NodeBackground'          : (ThemeValueType.COLOR, gui.mvNodeCol_NodeBackground),
    'NodeColor_NodeBackgroundHovered'   : (ThemeValueType.COLOR, gui.mvNodeCol_NodeBackgroundHovered),
    'NodeColor_NodeBackgroundSelected'  : (ThemeValueType.COLOR, gui.mvNodeCol_NodeBackgroundSelected),
    'NodeColor_NodeOutline'             : (ThemeValueType.COLOR, gui.mvNodeCol_NodeOutline),
    'NodeColor_TitleBar'                : (ThemeValueType.COLOR, gui.mvNodeCol_TitleBar),
    'NodeColor_TitleBarHovered'         : (ThemeValueType.COLOR, gui.mvNodeCol_TitleBarHovered),
    'NodeColor_TitleBarSelected'        : (ThemeValueType.COLOR, gui.mvNodeCol_TitleBarSelected),
    'NodeColor_Link'                    : (ThemeValueType.COLOR, gui.mvNodeCol_Link),
    'NodeColor_LinkHovered'             : (ThemeValueType.COLOR, gui.mvNodeCol_LinkHovered),
    'NodeColor_LinkSelected'            : (ThemeValueType.COLOR, gui.mvNodeCol_LinkSelected),
    'NodeColor_Pin'                     : (ThemeValueType.COLOR, gui.mvNodeCol_Pin),
    'NodeColor_PinHovered'              : (ThemeValueType.COLOR, gui.mvNodeCol_PinHovered),
    'NodeColor_BoxSelector'             : (ThemeValueType.COLOR, gui.mvNodeCol_BoxSelector),
    'NodeColor_BoxSelectorOutline'      : (ThemeValueType.COLOR, gui.mvNodeCol_BoxSelectorOutline),
    'NodeColor_GridBackground'          : (ThemeValueType.COLOR, gui.mvNodeCol_GridBackground),
    'NodeColor_GridLine'                : (ThemeValueType.COLOR, gui.mvNodeCol_GridLine),

    'NodesColor_GridLinePrimary'                : (ThemeValueType.COLOR, gui.mvNodesCol_GridLinePrimary),
    'NodesColor_MiniMapBackground'              : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapBackground),
    'NodesColor_MiniMapBackgroundHovered'       : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapBackgroundHovered),
    'NodesColor_MiniMapOutline'                 : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapOutline),
    'NodesColor_MiniMapOutlineHovered'          : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapOutlineHovered),
    'NodesColor_MiniMapNodeBackground'          : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapNodeBackground),
    'NodesColor_MiniMapNodeBackgroundHovered'   : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapNodeBackgroundHovered),
    'NodesColor_MiniMapNodeBackgroundSelected'  : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapNodeBackgroundSelected),
    'NodesColor_MiniMapNodeOutline'             : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapNodeOutline),
    'NodesColor_MiniMapLink'                    : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapLink),
    'NodesColor_MiniMapLinkSelected'            : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapLinkSelected),
    'NodesColor_MiniMapCanvas'                  : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapCanvas),
    'NodesColor_MiniMapCanvasOutline'           : (ThemeValueType.COLOR, gui.mvNodesCol_MiniMapCanvasOutline),

    'Style_Alpha'                  : (ThemeValueType.STYLE, gui.mvStyleVar_Alpha),
    'Style_WindowPadding'          : (ThemeValueType.STYLE, gui.mvStyleVar_WindowPadding),
    'Style_WindowRounding'         : (ThemeValueType.STYLE, gui.mvStyleVar_WindowRounding),
    'Style_WindowBorderSize'       : (ThemeValueType.STYLE, gui.mvStyleVar_WindowBorderSize),
    'Style_WindowMinSize'          : (ThemeValueType.STYLE, gui.mvStyleVar_WindowMinSize),
    'Style_WindowTitleAlign'       : (ThemeValueType.STYLE, gui.mvStyleVar_WindowTitleAlign),
    'Style_ChildRounding'          : (ThemeValueType.STYLE, gui.mvStyleVar_ChildRounding),
    'Style_ChildBorderSize'        : (ThemeValueType.STYLE, gui.mvStyleVar_ChildBorderSize),
    'Style_PopupRounding'          : (ThemeValueType.STYLE, gui.mvStyleVar_PopupRounding),
    'Style_PopupBorderSize'        : (ThemeValueType.STYLE, gui.mvStyleVar_PopupBorderSize),
    'Style_FramePadding'           : (ThemeValueType.STYLE, gui.mvStyleVar_FramePadding),
    'Style_FrameRounding'          : (ThemeValueType.STYLE, gui.mvStyleVar_FrameRounding),
    'Style_FrameBorderSize'        : (ThemeValueType.STYLE, gui.mvStyleVar_FrameBorderSize),
    'Style_ItemSpacing'            : (ThemeValueType.STYLE, gui.mvStyleVar_ItemSpacing),
    'Style_ItemInnerSpacing'       : (ThemeValueType.STYLE, gui.mvStyleVar_ItemInnerSpacing),
    'Style_IndentSpacing'          : (ThemeValueType.STYLE, gui.mvStyleVar_IndentSpacing),
    'Style_CellPadding'            : (ThemeValueType.STYLE, gui.mvStyleVar_CellPadding),
    'Style_ScrollbarSize'          : (ThemeValueType.STYLE, gui.mvStyleVar_ScrollbarSize),
    'Style_ScrollbarRounding'      : (ThemeValueType.STYLE, gui.mvStyleVar_ScrollbarRounding),
    'Style_GrabMinSize'            : (ThemeValueType.STYLE, gui.mvStyleVar_GrabMinSize),
    'Style_GrabRounding'           : (ThemeValueType.STYLE, gui.mvStyleVar_GrabRounding),
    'Style_TabRounding'            : (ThemeValueType.STYLE, gui.mvStyleVar_TabRounding),
    'Style_ButtonTextAlign'        : (ThemeValueType.STYLE, gui.mvStyleVar_ButtonTextAlign),
    'Style_SelectableTextAlign'    : (ThemeValueType.STYLE, gui.mvStyleVar_SelectableTextAlign),

    'PlotStyle_LineWeight'         : (ThemeValueType.STYLE, gui.mvPlotStyleVar_LineWeight),
    'PlotStyle_Marker'             : (ThemeValueType.STYLE, gui.mvPlotStyleVar_Marker),
    'PlotStyle_MarkerSize'         : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MarkerSize),
    'PlotStyle_MarkerWeight'       : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MarkerWeight),
    'PlotStyle_FillAlpha'          : (ThemeValueType.STYLE, gui.mvPlotStyleVar_FillAlpha),
    'PlotStyle_ErrorBarSize'       : (ThemeValueType.STYLE, gui.mvPlotStyleVar_ErrorBarSize),
    'PlotStyle_ErrorBarWeight'     : (ThemeValueType.STYLE, gui.mvPlotStyleVar_ErrorBarWeight),
    'PlotStyle_DigitalBitHeight'   : (ThemeValueType.STYLE, gui.mvPlotStyleVar_DigitalBitHeight),
    'PlotStyle_DigitalBitGap'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_DigitalBitGap),
    'PlotStyle_PlotBorderSize'     : (ThemeValueType.STYLE, gui.mvPlotStyleVar_PlotBorderSize),
    'PlotStyle_MinorAlpha'         : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MinorAlpha),
    'PlotStyle_MajorTickLen'       : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MajorTickLen),
    'PlotStyle_MinorTickLen'       : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MinorTickLen),
    'PlotStyle_MajorTickSize'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MajorTickSize),
    'PlotStyle_MinorTickSize'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MinorTickSize),
    'PlotStyle_MajorGridSize'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MajorGridSize),
    'PlotStyle_MinorGridSize'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MinorGridSize),
    'PlotStyle_PlotPadding'        : (ThemeValueType.STYLE, gui.mvPlotStyleVar_PlotPadding),
    'PlotStyle_LabelPadding'       : (ThemeValueType.STYLE, gui.mvPlotStyleVar_LabelPadding),
    'PlotStyle_LegendPadding'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_LegendPadding),
    'PlotStyle_LegendInnerPadding' : (ThemeValueType.STYLE, gui.mvPlotStyleVar_LegendInnerPadding),
    'PlotStyle_LegendSpacing'      : (ThemeValueType.STYLE, gui.mvPlotStyleVar_LegendSpacing),
    'PlotStyle_MousePosPadding'    : (ThemeValueType.STYLE, gui.mvPlotStyleVar_MousePosPadding),
    'PlotStyle_AnnotationPadding'  : (ThemeValueType.STYLE, gui.mvPlotStyleVar_AnnotationPadding),
    'PlotStyle_FitPadding'         : (ThemeValueType.STYLE, gui.mvPlotStyleVar_FitPadding),
    'PlotStyle_PlotDefaultSize'    : (ThemeValueType.STYLE, gui.mvPlotStyleVar_PlotDefaultSize),
    'PlotStyle_PlotMinSize'        : (ThemeValueType.STYLE, gui.mvPlotStyleVar_PlotMinSize),

    'NodeStyle_GridSpacing'                : (ThemeValueType.STYLE, gui.mvNodeStyleVar_GridSpacing),
    'NodeStyle_NodeCornerRounding'         : (ThemeValueType.STYLE, gui.mvNodeStyleVar_NodeCornerRounding),
    'NodeStyle_NodePadding'                : (ThemeValueType.STYLE, gui.mvNodeStyleVar_NodePadding),
    'NodeStyle_NodeBorderThickness'        : (ThemeValueType.STYLE, gui.mvNodeStyleVar_NodeBorderThickness),
    'NodeStyle_LinkThickness'              : (ThemeValueType.STYLE, gui.mvNodeStyleVar_LinkThickness),
    'NodeStyle_LinkLineSegmentsPerLength'  : (ThemeValueType.STYLE, gui.mvNodeStyleVar_LinkLineSegmentsPerLength),
    'NodeStyle_LinkHoverDistance'          : (ThemeValueType.STYLE, gui.mvNodeStyleVar_LinkHoverDistance),
    'NodeStyle_PinCircleRadius'            : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinCircleRadius),
    'NodeStyle_PinQuadSideLength'          : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinQuadSideLength),
    'NodeStyle_PinTriangleSideLength'      : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinTriangleSideLength),
    'NodeStyle_PinLineThickness'           : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinLineThickness),
    'NodeStyle_PinHoverRadius'             : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinHoverRadius),
    'NodeStyle_PinOffset'                  : (ThemeValueType.STYLE, gui.mvNodeStyleVar_PinOffset),
    
    'NodesStyle_MiniMapPadding' : (ThemeValueType.STYLE, gui.mvNodesStyleVar_MiniMapPadding),
    'NodesStyle_MiniMapOffset'  : (ThemeValueType.STYLE, gui.mvNodesStyleVar_MiniMapOffset),
}

def load_theme_file(gui: gui, path: str) -> None:
    
    data = toml.load(path)
    
    # Interpret and apply theme values:
    with gui.theme() as global_theme:
        with gui.theme_component(gui.mvAll):
            for key, value in data.items():
                print(f'{key}: {value}')

                if key in THEME_CONSTANTS_INFO:
                    (value_type, value_target) = THEME_CONSTANTS_INFO[key]
                    
                    try:
                        if value_type == ThemeValueType.COLOR:
                            if is_color(value):
                                for idx in range(len(value)):
                                    value[idx] = value[idx] * 255.0
                                gui.add_theme_color(value_target, value)
                        
                        elif value_type == ThemeValueType.STYLE:

                            if isinstance(value, list) and len(value) == 2:
                                gui.add_theme_style(value_target, x=value[0], y=value[1])
                            else:
                                gui.add_theme_style(value_target, value)
                        
                    except SystemError as e:
                        raise ThemeException(f'Couldn\'t set "{key}" to "{value}"') from e
        
    gui.bind_theme(global_theme)

if __name__ == '__main__':
    gui.create_context()
    gui.enable_docking()

    with gui.window() as win0:
        gui.set_primary_window(win0, True)

    with gui.window(label="Tutorial", pos=(20, 50), width=275, height=225) as win1:
        t1 = gui.add_input_text(default_value="some text")
        t2 = gui.add_input_text(default_value="some text")
        with gui.child_window(height=100):
            t3 = gui.add_input_text(default_value="some text")
            gui.add_input_int()
        gui.add_input_text(default_value="some text")

    with gui.window(label="Tutorial", pos=(320, 50), width=275, height=225) as win2:
        gui.add_input_text(default_value="some text")
        gui.add_input_int()

    # with gui.theme() as global_theme:

    #     with gui.theme_component(gui.mvAll):
    #         gui.add_theme_color(gui.mvThemeCol_FrameBg, (255, 140, 23), category=gui.mvThemeCat_Core)
    #         gui.add_theme_style(gui.mvStyleVar_FrameRounding, 5, category=gui.mvThemeCat_Core)

    #     with gui.theme_component(gui.mvInputInt):
    #         gui.add_theme_color(gui.mvThemeCol_FrameBg, (140, 255, 23), category=gui.mvThemeCat_Core)
    #         gui.add_theme_style(gui.mvStyleVar_FrameRounding, 5, category=gui.mvThemeCat_Core)

    # gui.bind_theme(global_theme)

    gui.show_style_editor()
    gui.show_imgui_demo()
    load_theme_file(gui, 'themes/dark.toml')

    gui.create_viewport(title='Custom Title', width=800, height=600)
    gui.setup_dearpygui()
    gui.show_viewport()
    gui.start_dearpygui()
    gui.destroy_context()
