'''

  Working with files in Python

'''

# reading and writing files
path_to_file = '00 - Very Basics/text_files/'
file_name1 = input('What is the file name you want to write to? ')

try:
  file1 = open('{}/{}.txt'.format(path_to_file, file_name1), 'w')
  file1.write('''
    You don't know how to be a man

    I open myself, you close me,
    I want to run, but you catch me again,
    I want to cry out, you tell me to shut up,
    Why do I do it?

    I throw myself, like a child
    I listen to you, pleasant, humble
    Why do I do it?
    Why don't I leave, why do I settle?

    I gave you power over me,
    I am strong but not this way, but not now
    When do I have to say it;
    How do I say it to you?

    You don't know how to be a man
    For a girl.
    You didn't even try,
    Not even once.
    My argument is mute,
    It's just for me.
    You don't know how to be a man
    And nobody teaches you how.

  ''')
  file1.close()
except FileNotFoundError as error:
  print(error)
else:
  print('Text file was correctelly created/written.')

file_name2 = input('What is the file name you want to read from? ')

try:
  file2 = open('{}/{}.txt'.format(path_to_file, file_name2), 'r')
  print(file2.read())
  file2.close()
except FileNotFoundError as error:
  print(error)
else:
  print('File was read correctelly.')

  print(file1.closed)
  print(file2.closed)

try:
  with open('{}/{}.txt'.format(path_to_file, file_name2)) as myFile:
    print(myFile.read())
except FileNotFoundError as error:
  print(error)

songs = [
  'Visele',
  'Iubirea noastra muta',
  'Da\' ce tu',
  'Haina ta',
  'Ce s-a intamplat cu noi',
  'My Favourite Man',
  'Bandana',
  'Bolnavi amandoi',
  'Cosmos',
  'Octombrie Rosu',
  'Eroii pieselor noastre',
  'Beau',
  'In locul meu',
  'Cel mai bun prieten',
  'Nu stii tu sa fii barbat'
]

try:
  with open('{}/{}'.format(path_to_file, 'irina_rimes_songs.txt'), 'w') as songs_file:
    for song in songs:
      songs_file.write('{}\n'.format(song))
except FileNotFoundError as error:
  print(error)

try:
  with open('{}/{}'.format(path_to_file, 'irina_rimes_songs1.txt'), 'w') as songs_file:
    for song in songs:
      songs_file.writelines('%s\n'%song)
except FileNotFoundError as error:
  print(error)

with open('{}/{}'.format(path_to_file, 'irina_rimes_songs1.txt')) as songs_file:
  print(songs_file.readline(10))
  print(songs_file.tell())
  print(songs_file.readlines())

with open('{}/{}'.format(path_to_file, 'irina_rimes_songs1.txt')) as songs_file:
  print(songs_file.tell())
  songs_file.seek(10, 0)
  print(songs_file.tell())
  print(songs_file.read(15))
  print(songs_file.tell())

with open('{}/{}'.format(path_to_file, 'irina_rimes_songs1.txt'), 'r+') as songs_file:
  songs_file.seek(0, 2)
  print(songs_file.tell())
  songs_file.write('Hello')

# os module
import os
print(os.getcwd())
# print(os.get_exec_path())

try:
  os.mkdir('nice_folder')
except Exception:
  pass

print(os.path.isdir('nice_folder'))

try:
  os.rename('nice_folder', 'ugly_folder')
except Exception:
  pass

print(os.path.isdir('nice_folder'))
try:
  os.remove('ugly_folder')
except Exception as error:
  print(error)