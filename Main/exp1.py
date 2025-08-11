import os
import re

INPUT_DIR = '../Data/input'

c_id_pattern = r'^[A-Za-z0-9]{6}$'
p_id_pattern = r'^[A-Za-z0-9]{10}$'
date_pattern = r'^\d{4}-\d{2}-\d{2}$'
rating_pattern = r'^[1-5]$'

ans = []
invalid = 0
valid = 0
prod_sums = {}
prod_counts = {}

for file in os.listdir(INPUT_DIR):
    if file.endswith('.txt'):
        path = os.path.join(INPUT_DIR, file)
        try:
            with open(path, encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = re.split(r'\s+', line, 4)
                    
                    if len(parts) < 5:
                        invalid += 1
                        continue
                        
                    c_id, p_id, review_date, review_rating_str, review_text = parts
                    # check invalidity
                    if not re.match(c_id_pattern, c_id) or not re.match(
                            p_id_pattern, p_id) or not re.match(
                                date_pattern, review_date) or not re.match(
                                    rating_pattern, review_rating_str):
                        invalid += 1
                        continue
                        
                    try:
                        review_rating = int(review_rating_str)
                    except ValueError:
                        invalid += 1
                        continue
                    
                    prod_sums[p_id] = prod_sums.get(p_id, 0) + review_rating
                    prod_counts[p_id] = prod_counts.get(p_id, 0) + 1
                    valid += 1
                    ans.append(
                        (c_id, p_id, review_date, review_rating, review_text))
        except Exception as e:
            print(f"Error reading {path}: {e}")

total_processed = valid + invalid
prod_avg = {pid: prod_sums[pid] / prod_counts[pid] for pid in prod_sums}
top3 = sorted(prod_avg.items(), key=lambda x: (-x[1], -prod_counts[x[0]]))[:3]

with open('summary.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total reviews processed: {total_processed}\n")
    out.write(f"Total valid reviews: {valid}\n")
    out.write(f"Total invalid reviews: {invalid}\n")
    out.write("\nTop 3 products by average rating:\n")
    for pid, avg in top3:
        out.write(f"{pid}\t->\t{avg:.2f}\n")

