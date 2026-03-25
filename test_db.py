import urllib.request
import json
import urllib.error

url_tours = "https://zdtmhcmcngarwieniwgk.supabase.co/rest/v1/tours?select=*"
url_reviews = "https://zdtmhcmcngarwieniwgk.supabase.co/rest/v1/reviews?select=*"
key = "sb_publishable_IxJ8eZHR-AsD1aFQqcVrRg_wRIIUDqY"

headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}"
}

print("Testing Tours Table...")
try:
    req = urllib.request.Request(url_tours, headers=headers)
    res = urllib.request.urlopen(req)
    print("Tours Data:", res.read()[:200], "...(truncated)")
except urllib.error.HTTPError as e:
    print(f"Error fetching tours: {e.code} - {e.reason}")
    print(e.read())

print("\nTesting Reviews Table...")
try:
    req = urllib.request.Request(url_reviews, headers=headers)
    res = urllib.request.urlopen(req)
    print("Reviews Data:", res.read()[:200], "...(truncated)")
except urllib.error.HTTPError as e:
    print(f"Error fetching reviews: {e.code} - {e.reason}")
    print(e.read())
