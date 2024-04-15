import pandas as pd
import emoji

import re

def create_dataframe():
  # Read chat data from text file
  with open('./data/_chat.txt', 'r', encoding='utf-8') as f:
      chat_data = f.readlines()

  # Define regular expressions to extract data
  # message_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2})\] (\w+): (.+)')
  message_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2})\] (.*?): (.+)')
  system_message_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2})\] Baile Balersón: ‎(.+)')
  media_message_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2})\] (.*?): (?:image|video|sticker) omitted')

  # Initialize data lists
  dates = []
  times = []
  members = []
  messages = []
  message_types = []
  message_lengths = []
  reaction_counts = []
  word_counts = []
  hashtags = []
  mentions = []
  emojis = []

  # Loop through chat data and extract required information
  for line in chat_data:
      # Check if line contains a message
      match = message_regex.match(line)
      if match:
          dates.append(match.group(1)[:10])
          times.append(match.group(1)[11:])
          member = emoji.demojize(match.group(2)).strip()
          members.append(member)
          messages.append(match.group(3))
          message_types.append('text')
          message_lengths.append(len(match.group(3)))
          reaction_counts.append(0)
          word_counts.append(len(match.group(3).split()))
          hashtags.append(re.findall(r'#(\w+)', match.group(3)))
          mentions.append(re.findall(r'@(\w+)', match.group(3)))
          emojis.append(re.findall(r'[\U0001F600-\U0001F650]', match.group(3)))
      else:
          # Check if line contains a system message
          match = system_message_regex.match(line)
          if match:
              dates.append(match.group(1)[:10])
              times.append(match.group(1)[11:])
              members.append('System')
              messages.append(match.group(2))
              message_types.append('system')
              message_lengths.append(len(match.group(2)))
              reaction_counts.append(0)
              word_counts.append(len(match.group(2).split()))
              hashtags.append([])
              mentions.append([])
              emojis.append([])
          else:
              # Check if line contains a media message
              match = media_message_regex.match(line)
              if match:
                  dates.append(match.group(1)[:10])
                  times.append(match.group(1)[11:])
                  member = emoji.demojize(match.group(2)).strip()
                  members.append(member)
                  messages.append(match.group(3))
                  message_types.append('media')
                  message_lengths.append(0)
                  reaction_counts.append(0)
                  word_counts.append(0)
                  hashtags.append([])
                  mentions.append([])
                  emojis.append([])

  # Create pandas dataframe from extracted data
  df = pd.DataFrame({
      'date': dates,
      'time': times,
      'member': members,
      'message': messages,
      'message_type': message_types,
      'message_length': message_lengths,
      'reaction_count': reaction_counts,
      'word_count': word_counts,
      'hashtags': hashtags,
      'mentions': mentions,
      'emojis': emojis
  })
  df.drop([0, 1, 2], axis=0, inplace=True)
  df.reset_index(drop=True, inplace=True)
  name_dict = {
    'Agustin': 'Agustin',
    'Emmanuel Castillo': 'Emma',
    '~ Pau Prado': 'Paula',
    'Paula Prado': 'Paula',
    'Agus Osimani': 'Agustina',
    'Julián Antonielli': 'Julian',
    'Nahuel Aguilar': 'Nahue',
    'Santiago Ivulich': 'Santi',
    'Victoria Rached': 'Vicky',
    'Flor Scarpettini': 'Flor S',
    'Juan Godfrid': 'Juan',
    'Diego Zuluaga': 'Zulu',
    'Nacho Rodriguez Paez': 'Nacho',
    'Tomás Cerdá': 'Tomi',
    'Florencia Prado': 'Flor P',
    'Pablo Baile Bailerson': 'Pablo',
    '~ Franco Bonavento': 'Bona',
    'Guille Laviz': 'Guille',
    'Carla Salvemini': 'Carla'
  }
  df['member'] = df['member'].replace(name_dict)
  return df
