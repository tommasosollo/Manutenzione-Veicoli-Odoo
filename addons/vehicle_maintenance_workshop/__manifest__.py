{
    "name": "Vehicle Maintenance Workshop",
    "author": "Tommaso Sollo",
    "license": "LGPL-3",
    "version": "17.0.1.0",
    "depends": [
        "base",
        "product",
        "account",
        "mail"
    ],

    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/vehicle_views.xml",
        "views/workorder_views.xml",
        "views/workorder_type_views.xml",
        "views/product_views.xml",
        "data/sequence.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
}