import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

user_name = "Sudheer"
user_email = "sudheerss928@gmail.com"
masked_email = user_email[0] + "*" * (len(user_email) - 13) + user_email[-12:]
account_balance = "₹6000.95"

otp = str(random.randint(100000, 999999))

def send_otp_email():
    subject = "Your Secure OTP Code"
    body = f"Dear {user_name},\n\nYour One-Time Password (OTP) is: {otp}\nPlease use this to complete your secure login.\n\nThank you,\nSecure Bank"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = user_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, msg.as_string())
        messagebox.showinfo("Sent", f"OTP sent to {user_email}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email.\n{e}")

def show_dashboard():
    dash = tk.Toplevel(root)
    dash.title("Secure Banking Dashboard")
    dash.geometry("380x300")
    dash.configure(bg="#f1f6f9")

    login_time = datetime.now().strftime("%d %b %Y %I:%M %p")

    tk.Label(dash, text=f"🏦 Welcome, {user_name}", font=("Arial", 14, "bold"), bg="#f1f6f9").pack(pady=10)
    tk.Label(dash, text=f"🔐 Email: {masked_email}", font=("Arial", 11), bg="#f1f6f9").pack(pady=2)
    tk.Label(dash, text=f"🕒 Login Time: {login_time}", font=("Arial", 11), bg="#f1f6f9").pack(pady=2)
    tk.Label(dash, text=f"💰 Account Balance: {account_balance}", font=("Arial", 12, "bold"), fg="green", bg="#f1f6f9").pack(pady=10)

    tk.Label(dash, text="✔️ Your session is secure and encrypted.", font=("Arial", 10), fg="gray", bg="#f1f6f9").pack(pady=5)
    tk.Button(dash, text="Logout", command=dash.destroy, width=15, bg="#d9534f", fg="white").pack(pady=20)

def verify_otp():
    entered = entry.get()
    if entered == otp:
        messagebox.showinfo("Success", "✅ OTP Verified Successfully!")
        show_dashboard()
    else:
        messagebox.showerror("Error", "❌ Incorrect OTP. Please try again.")

sender_email = "sudheerss928@gmail.com"
sender_password = "parx kqer emgl yqjv"

root = tk.Tk()
root.title("Bank OTP Login")
root.geometry("300x250")
root.configure(bg="#ffffff")

tk.Button(root, text="📧 Send OTP to Email", command=send_otp_email, bg="#5cb85c", fg="white").pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack(pady=10)

tk.Button(root, text="Verify OTP", command=verify_otp, bg="#0275d8", fg="white").pack(pady=10)

root.mainloop()

