import getpass
import os
import sys
from csv_xlsx_handling import CSV_XLSX_Handler
from email_handling import Email_Sender


def clear_screen():
    # Simple cross-platform clear
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt_path(prompt_text: str, must_exist: bool = True) -> str:
    while True:
        p = input(prompt_text).strip()
        if not p:
            print('Input required. Please try again.')
            continue
        if must_exist and not os.path.isfile(p):
            print(f'File not found: {p}')
            cont = input('Try again? [y/N]: ').strip().lower()
            if cont == 'y':
                continue
            else:
                return ''
        return p


def convert_flow():
    print('\n--- CSV -> XLSX Converter ---')
    csv_path = prompt_path('Enter path to CSV file: ', must_exist=True)
    if not csv_path:
        print('Conversion cancelled')
        return
    default_out = os.path.splitext(csv_path)[0] + '.xlsx'
    out = input(f'Output XLSX path [{default_out}]: ').strip() or default_out

    handler = CSV_XLSX_Handler(csv_path=csv_path, xlsx_path=out)
    try:
        handler.convert_csv_to_xlsx()
        print(f'Success: {csv_path} -> {out}')
    except Exception as e:
        print('Conversion failed:', e)


def send_flow():
    print('\n--- Send Email ---')
    smtp_server = input('SMTP server (e.g. smtp.gmail.com) [smtp.gmail.com]: ').strip() or 'smtp.gmail.com'
    port_str = input('SMTP port [587]: ').strip() or '587'
    try:
        port = int(port_str)
    except ValueError:
        print('Invalid port; using 587')
        port = 587

    sender = input('Sender email: ').strip()
    if not sender:
        print('Sender required, cancelling')
        return
    password = getpass.getpass('Password (input hidden): ')
    recipient = input('Recipient email: ').strip()
    if not recipient:
        print('Recipient required, cancelling')
        return
    subject = input('Subject: ').strip() or 'No subject'
    body = input('Body: ').strip() or ''

    attachments = []
    while True:
        a = input('Add attachment (path) or press Enter to continue: ').strip()
        if not a:
            break
        if not os.path.isfile(a):
            print('Attachment not found, not added.')
            continue
        attachments.append(a)

    emailer = Email_Sender(smtp_server=smtp_server, port=port, sender_email=sender, password=password)
    try:
        emailer.send_email(recipient_email=recipient, subject=subject, body=body, attachments=attachments)
        print('Email sent')
    except Exception as e:
        print('Failed to send email:', e)


def main_menu():
    while True:
        print('\n===== Simple Automation Menu =====')
        print('1) Convert CSV -> XLSX')
        print('2) Send an email')
        print('3) Exit')
        choice = input('Choose an option [1-3]: ').strip()
        if choice == '1':
            convert_flow()
        elif choice == '2':
            send_flow()
        elif choice == '3':
            print('Goodbye')
            break
        else:
            print('Invalid choice; please enter 1, 2 or 3')


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print('\nCancelled by user')
        sys.exit(0)
