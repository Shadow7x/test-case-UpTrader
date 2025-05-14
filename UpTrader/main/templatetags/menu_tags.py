from ..models import *
from django import template
from typing import List
from django.db.models import Q


register = template.Library()

def build_menu_tree(items, parent=None) ->List[dict]:

    return [{
        'item': item,
        'children': build_menu_tree(items, item)
    } for item in items if item.parent == parent]
     

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context):
    request = context['request']

    current_url = request.path
    items = MenuItem.objects.all().select_related('parent') 

    menu_structure = build_menu_tree(items)
    
    for item in items:
        if (item.get_url == current_url):
            active_menu = item 
            break
    else:
        raise Exception('Записи по текущему адресу не найдено')
    
    active_menu_items = active_menu.order
    active_menu_type = active_menu.menu_name
    

    return {'menu_structure': menu_structure, 'active_menu_items': active_menu_items, 'active_menu_type': active_menu_type, 'request': request}    