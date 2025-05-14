# Remind Me Later

Simple Django REST API to save reminders with message, date, time, and type (SMS/Email).

## 🔗 API Endpoint

**POST** `/api/reminders/create/`

### 📥 Request Format
```json
{
  "date": "2025-05-15",
  "time": "15:30:00",
  "message": "Project meeting with team",
  "reminder_type": "email"
}
