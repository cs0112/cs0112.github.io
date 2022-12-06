
def most_common(counts): 
  most_common = ''
  most_common_count = 0
  for word in counts:   
    if counts[word] > most_common_count:
      most_common = word
      most_common_count = counts[word]    
  return most_common



