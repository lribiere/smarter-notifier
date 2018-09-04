URL="$1"
HTML_FILE_DIR="html_folder"
LAST_ARTICLE_DIR="last_article"

function print_usage() {
  echo "Usage : bash launcher.py <URL>"
}

function check_param() {
  if [ -n "$URL" ]; then
  	return 0
  else
  	return 1
  fi
}

function main() {  
  # cat ~/.wgetrc - CONTENT OF wgetrc configuration file (to pretend request comes from a legit browser) :
  # hsts=0
  # robots = off
  # header = Accept-Language: en-us,en;q=0.5
  # header = Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  # header = Connection: keep-alive
  # user_agent = Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
  # referer = /
  wget "$1" -O "${HTML_FILE_DIR}/index.html"
  
  python notifier.py
}

check_param || { print_usage ; exit 1 ; }
[ ! -d "$HTML_FILE_DIR" ] && mkdir "$HTML_FILE_DIR"
[ ! -d "$LAST_ARTICLE_DIR" ] && mkdir "$LAST_ARTICLE_DIR"

main "$URL"