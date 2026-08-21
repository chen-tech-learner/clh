import requests
import time

FILE_LIST = [
    ("clh.m3u", "clh_out.m3u"),
    ("clh1.m3u", "clh1_out.m3u"),
    ("clh2.m3u", "clh2_out.m3u"),
]
TIMEOUT = 8

def check_url(url):
    try:
        resp = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
        return resp.status_code == 200
    except Exception:
        return False

def process_file(in_path, out_path):
    with open(in_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = []
    temp_line = None
    total = 0
    ok = 0

    for line in lines:
        line = line.rstrip("\n")
        if line.startswith("#EXTM3U"):
            out_lines.append(line + "\n")
            continue
        if line.startswith("#EXTINF:"):
            temp_line = line
            continue
        if temp_line and (line.startswith("http://") or line.startswith("https://")):
            total += 1
            if check_url(line):
                ok += 1
                out_lines.append(temp_line + "\n")
                out_lines.append(line + "\n")
            temp_line = None
        time.sleep(0.2)

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(out_lines)
    print(f"文件 {in_path}：总共{total}个，存活{ok}，输出→{out_path}")

def main():
    for in_f, out_f in FILE_LIST:
        process_file(in_f, out_f)

if __name__ == "__main__":
    main()
