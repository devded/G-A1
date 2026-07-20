import os

from course_renderer import render_day, render_readme, ensure_dir, fmt_day

from data_w1 import weeks_data as w1_list
from data_w2 import weeks_data as w2_list
from data_w3 import weeks_3_to_6 as w3_list
from data_w4 import w4
from data_w5 import w5
from data_w6 import w6
from data_w7 import w7
from data_w8 import w8
from data_w9 import w9
from data_w10 import w10
from data_w11 import w11
from data_w12 import w12

all_weeks = []
all_weeks.extend(w1_list)
all_weeks.extend(w2_list)
all_weeks.extend(w3_list)
all_weeks.append(w4)
all_weeks.append(w5)
all_weeks.append(w6)
all_weeks.append(w7)
all_weeks.append(w8)
all_weeks.append(w9)
all_weeks.append(w10)
all_weeks.append(w11)
all_weeks.append(w12)

base_dir = '/home/thededar/Downloads/Workspace/test2/German-A1-Self-Study'

total_days_written = 0
total_readmes_written = 0

for w in all_weeks:
    week_num = w["weekNum"]
    week_str = fmt_day(week_num)
    
    # 1. Render & write Week README
    readme_path = os.path.join(base_dir, 'Weeks', f'Week-{week_str}', 'README.md')
    ensure_dir(readme_path)
    readme_content = render_readme(w)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    total_readmes_written += 1
    
    # 2. Render & write each Day file
    for d in w["days"]:
        day_num = d["dayNum"]
        day_str = fmt_day(day_num)
        day_path = os.path.join(base_dir, 'Weeks', f'Week-{week_str}', 'Days', f'Day-{day_str}.md')
        ensure_dir(day_path)
        day_content = render_day(d, week_num)
        with open(day_path, 'w', encoding='utf-8') as f:
            f.write(day_content)
        total_days_written += 1

print(f"🎉 Build Complete! Successfully written {total_days_written} Day files and {total_readmes_written} Week README files.")
