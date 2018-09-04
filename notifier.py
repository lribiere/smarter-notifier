import sys
from bs4 import BeautifulSoup

# TODO : rather than considering the last id, compute ids sets differences and notify with the delta
# Check if necessary before anything.

def get_last_known_id():
  try:
    with open("last_article/id", 'r') as last_id:
      return last_id.read()
  except IOError as e:
  	return -1

def compute_most_fresh_id():
  with open("html_folder/index.html", 'r') as html_doc:
    doc = html_doc.read()  
  soup = BeautifulSoup(doc, "lxml")
  all_lis = soup.find_all('li')
  if len(all_lis) == 0:
    print "Could not find id in index.html file..."
    sys.exit(0)
  try:
    for li in all_lis:
      if li.has_attr("itemtype"):
        return li.find_all("a")[0].get("href").split("/")[2]
  except Exception as e:
    print "Could not find id in index.html file..."
    sys.exit(0)

def update_last_known_id(most_fresh_id):
  try:
    with open("last_article/id", 'w') as last_id:
      last_id.write(most_fresh_id)
  except IOError as e:
  	print "Could not update last know id"

def main():
  last_known_id = get_last_known_id()
  print "last known id :", last_known_id

  most_fresh_id = compute_most_fresh_id()
  print "most fresh id :", most_fresh_id

  if most_fresh_id != last_known_id:
    print "Ids differ, there is some catching up to do"
    update_last_known_id(most_fresh_id)
  else:
    print "We are up to date"
  
  # Get all the missing articles in between
  # Send notifications (Slack ?)

if __name__ == "__main__":
    main()
