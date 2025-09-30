def count_log_levels(log_path):
    warn_count = 0
    info_count = 0
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'warn' in line.lower():
                warn_count += 1
            if 'info' in line.lower():
                info_count += 1
    print(f"Number of WARN messages: {warn_count}")
    print(f"Number of INFO messages: {info_count}")

if __name__ == "__main__":
    log_file_path = r"Basics\Notes.txt"  # Change this to your log file path
    count_log_levels(log_file_path)
