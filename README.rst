django-linkage
==============

A links, menus and breadcrumbs tool for Django sites.

Quick Start
-----------

1. Install as with any Django app:

   .. code-block:: python

      INSTALLED_APPS = [
          ...
          'linkage',
      ]

2. For any models you want to be able to link to a List view for, add a
   ``get_list_url`` method.

3. For any models you want to be able to link to a Detail view for, add a
   ``get_detail_url`` method.

4. Create Link records in Admin

5. Create Menu records in Admin, if you want.

6. In your templates:

.. code-block:: html

    {% load linkage %}
    {% load_links_with 'foo' as foo_links %}
    <ul>
    {% for link in foo_links %}
        <li><a href="{{ link.href }}">{{ link.title }}</a></li>
    {% endfor %}
    </ul>

