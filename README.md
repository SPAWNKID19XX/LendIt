# LendIt
Rental ecomerce
# 🚲 LendIt — Peer-to-Peer (P2P) Rental Platform

**LendIt** is a high-performance backend engine for peer-to-peer item rentals. It allows users to list their belongings (tools, electronics, vehicles) for rent and manage bookings with complex date-collision logic.

## 🛠 Tech Stack (2026 Standards)
- **Framework:** Django 6.x / Django REST Framework
- **Database:** PostgreSQL (with Row-Level Locking)
- **Auth:** JWT (SimpleJWT)
- **Architecture:** Service-oriented, Atomic Transactions

---

## 🏗 Key Architectural Features (Senior Level)

### 1. Advanced Date Collision Logic
To prevent double-booking, the system uses a mathematically robust overlap check:
`Existing_Start <= New_End AND Existing_End >= New_Start`.
This is implemented at the database level using **Q-objects** and **Row-Level Locking (`select_for_update`)** during the booking transaction.

### 2. Historical Price Consistency
Rental prices are locked at the moment of booking. Even if the owner changes the item's daily rate later, the original contract remains unchanged.

### 3. Smart Availability Calculation
The system dynamically calculates item availability for specific date ranges, excluding all "Confirmed" and "Pending" overlapping bookings.

---

## 🔐 1. Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `users/register/` | User sign-up |
| `POST` | `token/` | Login & Obtain JWT |

## 📦 2. Items (Listings)

| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `items/` | Public | Search available items |
| `POST` | `items/` | Authenticated | List a new item for rent |
| `GET` | `items/{id}/` | Public | Item details & Rental history |

## 📅 3. Bookings (Rentals)

| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `bookings/` | Authenticated | Request a rental (Start/End dates) |
| `PATCH` | `bookings/{id}/` | Owner/Renter | Update status (Confirm/Cancel) |

**Booking Request Format:**
```json
{
  "item": 101,
  "start_date": "2026-06-01",
  "end_date": "2026-06-05"
}
```

## Management Data
| Description     | Command                     | 
|:----------------|:----------------------------| 
| 50 new users    | ./manage.py new_users       | 
| Fuel categories | ./manage.py new_categories  | 
| Fuel 5000 items | ./manage.py new_items       | 
| Fuel items img  | ./manage.py new_item_imgs   | 