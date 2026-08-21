# run.py 模板示例
import requests

# =========在这里填你的源地址=========
source_url = "这里替换成你的直播源txt/m3u地址"
out1 = "clh.m3u"
out2 = "clh1.m3u"
out3 = "clh2.m3u"
# ==================================

def fetch_save(url, savepath):
    try:
        resp = requests.get(url,timeout=30)
        resp.encoding = "utf‑8"
        with open(savepath,"w",encoding="utf‑8") as f:
            f.write(resp.text)
        print(f"已写入 {savepath}")
    except Exception as e:
        print(f"获取失败 {url} , {e}")

# 示例：只更新第一个文件，你可以按需求改
fetch_save(source_url, out1)
# fetch_save(source_url, out2)
# fetch_save(source_url, out3)
