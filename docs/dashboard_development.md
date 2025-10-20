# Dashboard Development Guide

This document explains how to evolve the current Flask site into a modern dashboard. It covers layout, components, data flow, recommended frontend libraries, testing, and deployment notes.

## Goals / contract

- Input: server-side data (database, APIs), user interactions (filters, date ranges)
- Output: responsive dashboard UI with KPIs, charts, tables, and detail views
- Error modes: network/API failures, empty datasets, authentication failures

## Recommended project structure

- app/
  - routes/
    - dashboard.py  # blueprint for dashboard pages and endpoints
  - templates/
    - dashboard/
      - overview.html
      - partials/_kpi.html
      - partials/_chart.html
  - static/
    - css/style.css  # updated modern styles
    - js/dashboard.js # client-side interactions

## Layout and components

- Top nav (header) with brand, environment, and user controls
- Left sidebar for navigation and filters
- Main content: hero KPIs, grid of cards, charts, and a data table
- Modal/detail drawer for record details

Use the existing `layout` and `grid` classes from `style.css` as a starting point.

## Frontend libraries (optional)

- Charts: Chart.js or ApexCharts for simple embedding; Plotly for interactive graphs
- UI components: Tailwind CSS (already similar to current utility classes) or lightweight component library like Flowbite
- State & interactivity: Alpine.js for small interactions; React or Vue if you want a fully client-rendered dashboard

## Backend endpoints

- Provide JSON endpoints for charts and tables, e.g. `/api/dashboard/kpis`, `/api/dashboard/sales?start=&end=`
- Keep endpoints small, paginated, and cacheable. Add query params for filters/sorting.

Example Flask blueprint sketch:

```py
from flask import Blueprint, render_template, jsonify, request

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.get('/')
def overview():
    return render_template('dashboard/overview.html')

@bp.get('/api/kpis')
def kpis():
    # return JSON KPIs
    return jsonify({ 'revenue': 10000, 'active_users': 350 })
```

## Data flow and caching

- For expensive queries, use caching (Flask-Caching with Redis) and set short TTLs for live dashboards.
- Use background jobs (Celery/RQ) for heavy aggregation and store results in a fast-read store.

## Authentication & multi-tenant concerns

- Integrate Flask-Login or an external auth provider (Auth0, Okta) if you need per-user dashboards.
- Consider role-based filtering so different users see different datasets.

## Tests and quality gates

- Unit tests for blueprint endpoints and data transformers (use pytest + Flask test client)
- Small end-to-end smoke test that renders the dashboard page and loads `/api/kpis`

## Accessibility & performance

- Ensure sufficient color contrast for KPIs and charts
- Lazy-load heavy charts and paginate tables
- Use gzipped assets and a CDN in production

## Deployment notes

- Keep the WSGI entry point (`wsgi.py`) to call `create_app()` (already updated)
- For production: use Gunicorn + Nginx (or a Windows-friendly WSGI host), enable SSL, and ensure the `STATIC_ROOT` is served correctly by the webserver.

## Next steps (low risk additions I can implement for you)

- Add a `dashboard` blueprint, example templates, and a small JS file wiring a Chart.js example.
- Create API mocks and example tests demonstrating the data flow.

---

If you'd like I can scaffold the dashboard blueprint and a sample overview page with a Chart.js chart and one API endpoint. Tell me which sample metrics you'd like (sales, active users, property listings, etc.).
