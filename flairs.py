import praw
import csv
import time

# Init Reddit instance
reddit = praw.Reddit('settings')

# Init the sub selection
sub = reddit.subreddit('formula1')
#sub = reddit.subreddit('formula1exp')

# Remove all templates to ensure no conflicts or weird sorting
print('Clearing flair templates...')

sub.flair.templates.clear()

print('Clearing emojis...')

for emoji in sub.emoji:
  print(f'Removing emoji: {emoji}')

  sub.emoji[emoji].delete()

# Read CSV for flairs
with open('flairs.csv', newline = '') as flairs:
  reader = csv.DictReader(flairs)

  # Add emojis
  print('Adding emojis...')

  for row in reader:
    name = 'aaa-default' if row['class'] == 'label' else row['class']
    image = f'src/flairs/{name}.png'
    
    print(f'####################')
    print(f'####################   {name}')
    print(f'####################')
    
    print(f'Adding emoji: {name}, {image}, mod only: {row["mod_only"] == "True"}')
    
    sub.emoji.add(
      name,
      image,
      row['mod_only'] == 'True',
      False, # post_flair_allowed,
      True # user_flair_allowed
    )

    # Add flair templates
    text = row["text"] if name == 'aaa-default' else f':{name}: {row["text"]}'

    print(f'Adding flair: {row["text"]}, editable: {row["text_editable"] == "True"}, background: {row["background_color"]}, color: {row["text_color"]}, mod only: {row["mod_only"] == "True"}, allowable content: {row["allowable_content"]}')

    sub.flair.templates.add(
      text,
      row['class'],
      row['text_editable'] == 'True',
      row['background_color'],
      row['text_color'],
      row['mod_only'] == 'True',
      row['allowable_content']
    )

print('Done!')
