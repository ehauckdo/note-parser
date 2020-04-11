def read_lines(filename):
  lines = []
  source = open(filename, "r")
  for line in source:
    lines.append(line) 
  return lines

def write_lines(lines, filename="out.txt"):
  with open(filename, 'w') as the_file:
    for l in lines:
      the_file.write(l)

def is_hiragana(s):
  return fcc(s) > min_hiragana and fcc(s) < max_hiragana
def is_katakana(s):
  return fcc(s) > min_katakana and fcc(s) < max_katakana

#first character code
def fcc(string):
  return ord(string[0])

def reverse_hirakana(string):
  import jaconv
  if is_hiragana(string):
    string = jaconv.hira2kata(string)
  elif is_katakana(string):
    string = jaconv.kata2hira(string)
  return string

min_hiragana = ord("぀")
max_hiragana = ord("ゟ")
min_katakana = ord("゠")
max_katakana = ord("ヿ")


filename = "3 - Vocabulary.txt"
input_lines = read_lines(filename)
output_lines = []

for l in input_lines:
  fields = l.split("\t")
  # ignore "Basic and Reversed"
  # notes that have only 2 fields
  if len(fields) < 3: continue
  fields[1] = reverse_hirakana(fields[1])
  out = "\t".join(fields)
  output_lines.append(out)

write_lines(output_lines)
