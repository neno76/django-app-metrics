=================
Utility Functions
=================

.. function:: create_metric(name, slug)
    
    Creates a new type of metric track

.. function::  metric(slug, num=1, **kwargs)

    Shortcut to the current backend (as set by :ref:`Mixpanel backend<mixpanel_backend>`)'s metric method. Increment a metric by ``num`` 
    
    If there is no metric mapped to ``slug``, a metric named ``slug`` will be auto-generated.

    Arguments
    ---------

    ``slug`` `(required)`
    Name of the metric to increment.

    ``num``

    ``**kwargs``
    Any extra keyword arguments to pass to the backend.

.. function:: create_metric_set(create_metric_set(name=None, metrics=None, email_recipients=None, no_email=False, send_daily=True, send_weekly=False, send_monthly=False)

    
