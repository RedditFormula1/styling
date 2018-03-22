import praw
import csv
import json
from os import path

reddit = praw.Reddit('settings')

sub = reddit.subreddit('formula1flairs')

def templates_from_csv(path):
  f = csv.reader(file(path))
  # skip header row
  f.next()
  return [(r[0], r[1]) for r in f]

print 'Parsing csv file ...'
csv_templates = templates_from_csv('flairs.csv')

print 'Clearing flair templates ...'

sub.flair.templates.clear()

for text, css_class in csv_templates:
  print 'Adding flair template: %r, %r' % (text, css_class)

  sub.flair.templates.add(text, css_class, False)

print 'Done!'
