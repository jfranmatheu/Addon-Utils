from dataclasses import dataclass, asdict


@dataclass
class AddonInfo:
    name: str = 'Test Addon'
    author: str = 'Anonymous'
    description: str = "Nice Addon"
    blender: tuple[int, int, int] = (3, 5, 0)
    version: tuple[int, int, int] = (0, 0 , 1)
    location: str = ''
    category: str = 'GENERAL'
    warning: str = ''
    doc_url: str = ''
    tracker_url: str = ''
    support: str = 'COMMUNITY'
    
    @property
    def bl_info(self) -> dict:
        return asdict(self)


def AddonInfo(name: str = 'Test Addon',
              author: str = 'Anonymous',
              description: str = "Nice Addon",
              blender: tuple[int, int, int] = (3, 5, 0),
              version: tuple[int, int, int] = (0, 0 , 1),
              location: str = '',
              category: str = 'GENERAL',
              warning: str = '',
              doc_url: str = '',
              tracker_url: str = '',
              support: str = 'COMMUNITY') -> dict:
    bl_info = {
        'name': name,
        'author': author,
        'description': description,
        'blender': blender,
        'version': version,
        'location': location,
        'category': category,
        'warning': warning,
    }
    from ._globals import pprint_debug
    pprint_debug("Addon Info", bl_info)
    return bl_info

# bl_info = AddonInfo()