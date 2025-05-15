# capstone-modul1
# Sports Field Booking System 🏟️

## 📌 Introduction
This is a **console-based Python application** designed to manage the booking of sports fields. The system allows users to **view field availability**, **add**, **update**, and **delete** bookings with real-time conflict checking. It is designed with a clear and organized terminal interface suitable for learning or small-scale use.

---

## ✨ Features

- 📅 **View Availability**: Displays a neatly formatted schedule showing available and booked time slots for each field.
- ➕ **Create Booking**: Users can add a new reservation with validation on:
  - Duplicate names (case-insensitive)
  - Time overlap with existing bookings
- ✏️ **Update Booking**: Modify existing reservations with conflict validation.
- ❌ **Delete Booking**: Remove reservations based on booking ID.
- ✅ **Confirmation before all actions** (Add/Update/Delete/Exit)
- 📋 Real-time display of updated schedule before confirmation

---

## 👁️ View Availability

- Time slots from **16:00 to 04:00**
- Booking information displayed in a table:
  - `"✅ Available"` for free slots
  - `"❌ B003"` indicating a booking ID that occupies the slot

---

## 📝 Create Booking

Input fields required:
- `Name` (must be unique, case-insensitive)
- `Phone number`
- `Field` (choose from a list)
- `Start time` and `End time` (16 to 23 or 0 to 4)

System checks:
- Time conflicts with other bookings
- Duplicate names
- Confirmation prompt before saving

---

## ✏️ Update Booking

- Shows current bookings for easy selection
- Allows editing of:
  - Name
  - Field
  - Start and End time
- Conflict checking with other bookings (excluding the current one)
- Confirmation prompt before updating

---

## ❌ Delete Booking

- Shows current booking list
- Prompts for ID selection
- Confirmation prompt before deletion

---

## 💻 Technology Used

- **Language**: Python 3.x
- **Type**: Console-based CRUD application
- **Libraries**: No external libraries required
