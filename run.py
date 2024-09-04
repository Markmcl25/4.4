import argparse
import gspread
from google.oauth2.service_account import Credentials

# Set up Google Sheets API credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('read-it-news')

# Reference to the 'articles' worksheet
articles = SHEET.worksheet('articles')

# Function to create a new article
def create_article(args):
# Prepare the data to insert
    new_article = [
        args.article_id,
        args.title,
        args.content,
        args.author,
        args.category,
        args.published_date,
        args.image_url
    ]
    # Append the new article to the sheet
    articles_sheet.append_row(new_article)
    print("Article created successfully.")