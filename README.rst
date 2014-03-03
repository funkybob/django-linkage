==============
django-linkage
==============

A links, menus and breadcrumbs tool for Django sites.

Install
=======

1. pip install django-linkage
2. Add 'linkage' to INSTALLED_APPS
3. run syncdb

Usage
=====

Links
-----

Links allow you to configure links for reuse around your site.  There are three
types of link:

1. SimpleLink

   Links to a static URL.

2. ObjectTypeLink

   Links to a Model's list view.  This is determined by the model having a
   ``get_list_url`` method.

3. ObjectLink

   Links to a Model's detail view.  This is determined using the instances
   ``get_absolute_url`` method.

You can use Links in your templates as follows:

.. code-block:: html

   {% load linkage %}
   {% load_links_with 'foo' as foo_links %}
   <ul>
   {% for link in foo_links %}
       <li><a href="{{ link.href }}">{{ link.title }}</a></li>
   {% endfor %}
   </ul>

Or:

.. code-block:: html

   {% load linkage %}

   {# Default template is linkage/link.html #}
   {% link slug_or_name %}

   {# Will render the template, passing the link instance as 'link' in context. #}
   {% link slug_or_name template="link.html" %} 


Menus
-----

You can construct ordered, hierarchical sets of Links as Menus.

Each Menu has a title and a slug, and a list of MenuItems.  MenuItems have an
order, link, label, and a level.  The level can be used as a hint for rendering.

.. code-block:: html

   {% load linkage %}
   {# Default template is linkage/menu.html #}
   {% menu slug_or_name %}

   {# Passes the menu as 'menu' #}
   {% menu slug_or_name template='menu.html' %}
