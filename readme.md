Simple Flask application for employees table.

Web application is splitted on 3 parts: model, view, controller. As database sqlite is used. By default app is launched
on http://localhost:5000/.

In schema there is one table for employees. Each next employee has incremental id.

Post operation adds values to employees table. Hired date - the current one.
Delete operation updates Fired date on the current one.
Put operation updates values in the table by values from the request.

Examples of queries in request.py.