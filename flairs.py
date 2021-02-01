import praw
import csv
import time

# Init Reddit instance
reddit = praw.Reddit('settings')

# Init the sub selection
#sub = reddit.subreddit('formula1')
sub = reddit.subreddit('formula1exp')
#sub = reddit.subreddit('formula1flairs')

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
    name = row['class']

    print(f'####################')
    print(f'####################   {name}')
    print(f'####################')
    
    if(name != 'label') :

      image = f'src/flairs/{name}.png'
      
      print(f'Adding emoji: {name}, {image}, mod only: {row["mod_only"] == "True"}, post flair: {row["post_flair_allowed"]}, user flair: {row["user_flair_allowed"]}')
      
      sub.emoji.add(
        name,
        image,
        row['mod_only'] == 'True',
        row['post_flair_allowed'] == 'True', # post_flair_allowed,
        row['user_flair_allowed'] == 'True' # user_flair_allowed
      )

    # Add flair templates
    if(row['emoji_only'] == 'False'):
      text = row["text"] if name == 'label' else f':{name}: {row["text"]}'
      class_name = 'label' if name == 'label' else ''

      print(f'Adding flair: {text}, editable: {row["text_editable"] == "True"}, background: {row["background_color"]}, color: {row["text_color"]}, mod only: {row["mod_only"] == "True"}, allowable content: {row["allowable_content"]}')

      sub.flair.templates.add(
        text,
        class_name,
        row['text_editable'] == 'True',
        '#ffffff' if row['background_color'] == '' else row['background_color'],
        row['text_color'],
        row['mod_only'] == 'True',
        row['allowable_content']
      )

print('Done!')
