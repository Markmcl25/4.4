from django.shortcuts import render
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
articles_sheet = SHEET.worksheet('articles')

def politics_view(request):
    return fetch_articles_view(request, 'politics.html')

def sports_view(request):
    return fetch_articles_view(request, 'sports.html')

def technology_view(request):
    return fetch_articles_view(request, 'technology.html')

def fetch_articles_view(request, template_name):
    # Fetch articles from Google Sheets
    articles = articles_sheet.get_all_records()  # Fetching all articles

    return render(request, template_name, {'articles': articles})

def create_article_view(request):
    if request.method == 'POST':
        # Handle form submission for creating a new article
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        category = request.POST.get('category')
        published_date = request.POST.get('published_date')
        image_url = request.POST.get('image_url')
        
        # Prepare the data to insert
        new_article = [None, title, content, author, category, published_date, image_url]  # Assuming ID is auto-generated
        articles_sheet.append_row(new_article)  # Append the new article to the sheet

        return render(request, 'success.html', {'title': title})  # Redirect to a success page

    return render(request, 'create_article.html')  # Render the form for creating a new article
