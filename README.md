The project is built using:

🖥 Backend:

Flask (Python web framework)
Flask-WTF (Form handling)
SQLAlchemy (Database ORM)
🌐 Frontend:

Jinja2 (Flask templating engine)
Tailwind CSS (Modern styling for UI)
🗄 Database:

SQLite (Can be replaced with PostgreSQL/MySQL)


1. Features & Functionalities
The application provides the following functionalities:

✅ Manage Products:

Add, edit, and view products.
Each product has a unique product_id and a name.
✅ Manage Locations:

Add, edit, and view warehouse locations.
Each location has a unique location_id and a name.
✅ Track Product Movements:

Record product transfers between locations.
Movements include:
from_location: where the product is coming from (can be empty if it's an incoming product).
to_location: where the product is moving to (can be empty if it's an outgoing product).
qty: number of units being transferred.
2. Database Design
The project uses three database tables to store inventory data:

Table	Columns	Description
Product	product_id (PK), name	Stores product details.
Location	location_id (PK), name	Stores warehouse locations.
ProductMovement	movement_id (PK), timestamp, from_location, to_location, product_id, qty	Tracks product movements.
Notes:

Primary keys (PK) can be strings (VARCHAR).
Either from_location or to_location can be empty to represent stock coming in or going out.

Key Enhancements
✅ Tailwind CSS for Modern Styling – Clean and minimal design.
✅ Responsive Navigation Bar – Provides easy access to all sections.
✅ Styled Form Elements – Input fields with focus effects and padding.
✅ Improved Product List Formatting – Better spacing and readability.
✅ Stylish Buttons & Hover Effects – Smooth UI interactions.


 User Workflow
1️⃣ The user adds products (e.g., product_id = P001, name = Laptop).
2️⃣ The user adds warehouse locations (e.g., location_id = L001, name = New York Warehouse).
3️⃣ The user records product movements (e.g., Laptop moved from Supplier to New York Warehouse (10 units)).
4️⃣ The system keeps a history of all product movements.


 Summary
Flask-based inventory system for managing products & locations.
Tracks product movements between warehouses.
Uses Flask-WTF for forms and SQLAlchemy for database management.
Tailwind CSS for modern UI styling.
Can be extended with user authentication, API, and reports.