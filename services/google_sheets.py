
import uuid
import gspread

from pathlib import Path
from datetime import datetime
from google.oauth2.service_account import Credentials


# -------------------- CONFIGURATION --------------------

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS_FILE = (
    Path(__file__).resolve().parent.parent
    / "credentials"
    / "service_account.json"
)

SPREADSHEET_NAME = "CloudContact Assist"

HEADERS = [
    "Ticket_ID",
    "Received_Date",
    "Customer_Email",
    "Subject",
    "Message",
    "Category",
    "Assigned_Team",
    "Priority",
    "Status"
]


# -------------------- GOOGLE SHEETS CONNECTION --------------------

def connect_to_sheet():

    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(
            f"Google credentials not found: {CREDENTIALS_FILE}"
        )

    credentials = Credentials.from_service_account_file(
        str(CREDENTIALS_FILE),
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open(SPREADSHEET_NAME)

    return spreadsheet.sheet1


# -------------------- SAVE TICKET --------------------

def save_ticket(customer_email, subject, message, routing):

    sheet = connect_to_sheet()

    ticket_id = "TKT-" + uuid.uuid4().hex[:6].upper()

    received_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    row = [
        ticket_id,
        received_date,
        customer_email,
        subject,
        message,
        routing["Category"],
        routing["Assigned_Team"],
        routing["Priority"],
        routing["Status"]
    ]

    sheet.append_row(
        row,
        value_input_option="USER_ENTERED"
    )

    return ticket_id


# -------------------- GET ALL TICKETS --------------------

def get_tickets():

    sheet = connect_to_sheet()

    return sheet.get_all_records()


# -------------------- UPDATE TICKET STATUS --------------------

def update_ticket_status(ticket_id, new_status):

    allowed_statuses = [
        "Open",
        "In Progress",
        "Resolved"
    ]

    if new_status not in allowed_statuses:
        raise ValueError("Invalid ticket status")

    sheet = connect_to_sheet()

    ticket_ids = sheet.col_values(1)

    try:
        row_number = ticket_ids.index(ticket_id) + 1

    except ValueError:
        raise ValueError(
            f"Ticket {ticket_id} not found"
        )

    if row_number == 1:
        raise ValueError("Invalid ticket ID")

    # Column I = Status
    sheet.update_cell(
        row_number,
        9,
        new_status
    )

    return True


# -------------------- CONNECTION TEST --------------------

if __name__ == "__main__":

    print("Google Sheets connection test")

    sheet = connect_to_sheet()

    print("Connected successfully!")
    print("Spreadsheet:", SPREADSHEET_NAME)
    print("Worksheet:", sheet.title)
    print("Headers:", sheet.row_values(1))
