from .base_ui import BaseUI, DrawExtension, UILayout, Context
from ..._auto_load import __main_package__

from bpy.types import Panel as BlPanel


class Panel(BaseUI, DrawExtension):
    @classmethod
    def draw_in_layout(cls, layout: UILayout, label: str = 'Panel'):
        layout.popover(cls.bl_idname, text=label)

    @classmethod
    def register(cls, deco_cls, label: str, tab: str = __main_package__, space_type: str = 'VIEW_3D', region_type: str = 'UI',
                 hide_header: bool = False, default_closed: bool = False, instanced: bool = False) -> BlPanel:
        options = set()
        if hide_header:
            options.add('HIDE_HEADER')
        if default_closed:
            options.add('DEFAULT_CLOSED')
        if instanced:
            options.add('INSTANCED')
        return type(
            cls.__name__,
            (cls, BlPanel) if deco_cls is None else (cls, deco_cls, BlPanel),
            {
                'bl_idname': __main_package__ + '_PT_' + cls.__name__.lower(),
                'bl_label': label,
                'bl_category': tab,
                'bl_space_type': space_type,
                'bl_region_type': region_type,
                'bl_options': options
            }
        )

    class Register:
        POPOVER = lambda deco_cls, label: Panel.register(deco_cls, label, '', 'EMPTY', 'WINDOW', instanced=True)

        VIEW_3D = lambda deco_cls, label, tab: Panel.register(deco_cls, label, tab, 'VIEW_3D', 'UI')
        NODE_EDITOR = lambda deco_cls, label, tab: Panel.register(deco_cls, label, tab, 'NODE_EDITOR', 'UI')
        IMAGE_EDITOR = lambda deco_cls, label, tab: Panel.register(deco_cls, label, tab, 'IMAGE_EDITOR', 'UI')
