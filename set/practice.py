

# Setup the set of filename
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}
("--------------------------------------------------------------------------------------")

print("=> 1")
print("Yesterday:", yesterday)
print("Today:", today)
("--------------------------------------------------------------------------------------")

# New file (today only) and deleted files (yesterday only)
new_files = today - yesterday
deleted_files = yesterday - today
("--------------------------------------------------------------------------------------")

print("\n=> 2")
print("New files:", new_files)
print("Deleted files:", deleted_files)
("--------------------------------------------------------------------------------------")

# Unchanged file
unchanged_files = yesterday & today
print("\n=> 3 - Unchanged files:", unchanged_files)
("--------------------------------------------------------------------------------------")

# All changes (symmetric difference).
all_changes = yesterday ^ today
print("\n=> 4 - Added or deleted files:", all_changes)
("--------------------------------------------------------------------------------------")

# All file ever seen
all_files = yesterday | today
print("\n=> 5 - All files ever seen:", all_files)
