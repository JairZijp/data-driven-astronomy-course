# Write your crossmatch function here.
import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  ra2s = cat2[:,0]
  dec2s = cat2[:,1]

  for id1, (ra1, dec1) in enumerate(cat1):
    dists = angular_dist(ra1, dec1, ra2s, dec2s)
    min_id = np.argmin(dists)
    min_dist = dists[min_id]
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  ra1, dec1 = np.radians([180, 30])
  cat2 = [[180, 32], [55, 10], [302, -44]]
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))
  
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)