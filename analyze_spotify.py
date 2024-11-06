import ast
import csv

def is_valid(num: str) -> bool:
    try:
        num = float(num)
        if 0 < num < 1:
            return True
        return False
    except ValueError:
        return False

with open('top_50_2023.csv', 'r') as csvfile:
    header = next(csvfile)
    data = []
    for line in csvfile:
        line = line[:-1].split(',')
        data.append(line)

with open('top_50_2023.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)

GENRE = header.index('genres')
for row in rows:
    row[GENRE] = ast.literal_eval(row[GENRE])

# analyze danceability
danceability = header.index('danceability')
sum_dance = 0
counter = 0
for row in rows:
    if is_valid(row[danceability]):
        counter += 1
        sum_dance += float(row[danceability])
print(f"Average danceability is {round(sum_dance/counter, 2)}")

# find number of explicit songs
EXPLICIT = 2
counter = 0
for row in rows:
    if row[EXPLICIT] == 'True':
        counter += 1
print(f"Number of explicit songs is {counter}")

# top three genres
GENRES = 4
genres_count = {}
for row in rows:
    for genre in row[GENRES]:
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
top_3 = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:3]
top_3_genres = []
for genre in top_3:
    top_3_genres.append(genre[0])
print(f"Top 3 genres are {', '.join(top_3_genres)}")

# the most popular artist
ARTIST = 0
artist_count = {}
for row in rows:
    if row[ARTIST] in artist_count:
        artist_count[row[ARTIST]] += 1
    else:
        artist_count[row[ARTIST]] = 1
top_artist = sorted(artist_count.items(), key=lambda x: x[1], reverse=True)[:1]
for artist in top_artist:
    print(f"Top artist is {artist[0]}")

# most popular year
YEAR = 3
year_count = {}
for row in rows:
    if row[YEAR].split('-')[0] in year_count:
        year_count[row[YEAR].split('-')[0]] += 1
    else:
        year_count[row[YEAR].split('-')[0]] = 1
top_year = sorted(year_count.items(), key=lambda x: x[1], reverse=True)[:1]
for year in top_year:
    print(f"Top year is {year[0]}")

# analyse Average Liveliness with Energy Criteria
liveness = header.index('liveness')
energy = header.index('energy')
sum_live = 0
counter = 0
for row in rows:
    if is_valid(row[liveness]):
        if float(row[energy]) > 0.5:
            counter += 1
            sum_live += float(row[liveness])
print(f"Average liveness is {round(sum_live/counter, 2)}")