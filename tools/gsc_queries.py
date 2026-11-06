#!/usr/bin/env python3
"""
GSC Query+Page fetcher for craicbet.com
Outputs: gsc_query_page.csv  (query, page, clicks, impressions, position)

Setup (one time):
  pip install google-auth google-auth-oauthlib google-api-python-client --break-system-packages

Auth:
  1. Go to https://console.cloud.google.com/
  2. Create project → Enable "Google Search Console API"
  3. Credentials → Create OAuth 2.0 Client ID → Desktop app → Download JSON
  4. Save as: tools/client_secret.json
  5. Run this script — browser opens, sign in, done.
     Token saved to tools/gsc_token.json for reuse.
"""

import os, json, csv, datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SITE = "sc-domain:craicbet.com"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "gsc_token.json")
SECRET_FILE = os.path.join(os.path.dirname(__file__), "client_secret.json")
OUT_FILE = os.path.join(os.path.dirname(__file__), "gsc_query_page.csv")

# Date range: last 90 days
END = datetime.date.today().isoformat()
START = (datetime.date.today() - datetime.timedelta(days=90)).isoformat()

def get_creds():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(SECRET_FILE):
                print(f"ERROR: {SECRET_FILE} not found.")
                print("Download OAuth2 credentials from Google Cloud Console.")
                raise SystemExit(1)
            flow = InstalledAppFlow.from_client_secrets_file(SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds

def fetch_all():
    service = build("searchconsole", "v1", credentials=get_creds())
    rows = []
    start_row = 0
    page_size = 25000

    print(f"Fetching query+page data for {SITE} ({START} → {END})...")
    while True:
        resp = service.searchanalytics().query(
            siteUrl=SITE,
            body={
                "startDate": START,
                "endDate": END,
                "dimensions": ["query", "page"],
                "rowLimit": page_size,
                "startRow": start_row,
            }
        ).execute()

        batch = resp.get("rows", [])
        if not batch:
            break
        rows.extend(batch)
        print(f"  fetched {len(rows)} rows...")
        if len(batch) < page_size:
            break
        start_row += page_size

    return rows

def main():
    rows = fetch_all()
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["query", "page", "clicks", "impressions", "ctr", "position"])
        for r in rows:
            keys = r["keys"]
            w.writerow([
                keys[0],  # query
                keys[1],  # page
                r.get("clicks", 0),
                r.get("impressions", 0),
                round(r.get("ctr", 0) * 100, 2),
                round(r.get("position", 0), 1),
            ])

    print(f"\nDone! {len(rows)} rows saved to {OUT_FILE}")
    print("Upload gsc_query_page.csv to Claude for H2 analysis.")

if __name__ == "__main__":
    main()
