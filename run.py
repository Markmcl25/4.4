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
articles_sheet = SHEET.worksheet('articles')

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

# Function to list all articles
def list_articles():
    data = articles_sheet.get_all_values()
    for row in data:
        print(row)

# Set up argument parsing
def main():
    parser = argparse.ArgumentParser(description="Google Sheets Article Management")

    # Subcommands for different actions
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Command to create a new article
    create_parser = subparsers.add_parser('create', help='Create a new article')
    create_parser.add_argument('article_id', help='ID of the article')
    create_parser.add_argument('title', help='Title of the article')
    create_parser.add_argument('content', help='Content of the article')
    create_parser.add_argument('author', help='Author of the article')
    create_parser.add_argument('category', help='Category of the article')
    create_parser.add_argument('published_date', help='Published date of the article')
    create_parser.add_argument('image_url', help='Image URL of the article')

    # Command to list all articles
    subparsers.add_parser('list', help='List all articles')

    # Parse arguments
    args = parser.parse_args()

    # Execute based on command
    if args.command == 'create':
        create_article(args)
    elif args.command == 'list':
        list_articles()
    else:
        parser.print_help()

# Entry point
if __name__ == '__main__':
    main()
