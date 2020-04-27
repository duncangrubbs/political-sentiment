commands = []
f = open('./usernames.txt', "r")
for line in f:
  line = line.replace('\n', '')
  commands.append(f'touch ./out/{line}.csv\n')
  commands.append(f'python GetOldTweets3.py --username "{line}" --output="./out/{line}.csv" --since 2015-01-01 --until 2019-12-31\n')
  # commands.append(f'mv output_got.csv {line}.csv\n')

f.close()

f2 = open('./commands.sh', 'w')
for c in commands:
  f2.write(c)
