import requests
import time

IN_FILE = "clh.m3u"
OUT_FILE = "clh_out.m3u"
TIMEOUT = 8

def check_url(url):
    try:
        resp = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
        return resp.status_code == 200
    except Exception:
        return False

def main():
    with open(IN_FILE, "r", encoding="utf-8") as f:
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

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(out_lines)
    print(f"总共:{total}个频道，存活:{ok}，已输出到 {OUT_FILE}")

if __name__ == "__main__":
    main()
