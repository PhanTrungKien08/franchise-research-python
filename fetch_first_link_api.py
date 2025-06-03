import requests, openpyxl, urllib.parse, time, glob

# ---- THÔNG SỐ CÁ NHÂN ---------------------------------
API_KEY = "aaaa"   # <-- DÁN API KEY
CX      = "eaaa"                  # mã công cụ tìm kiếm
SLEEP   = 1          # giây chờ giữa 2 lần gọi (giảm nếu muốn nhanh)
# --------------------------------------------------------

def first_link(query: str) -> str:
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx":  CX,
        "q":   query,
        "num": 1,
        "fields": "items(link)"
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data.get("items", [{}])[0].get("link", "")

def fill_excel(path: str):
    wb = openpyxl.load_workbook(path)
    sh = wb.active
    for row in range(2, sh.max_row + 1):        # bỏ tiêu đề
        g_url = sh.cell(row, 1).value
        if not g_url or sh.cell(row, 2).value:
            continue
        q = urllib.parse.parse_qs(
                urllib.parse.urlparse(g_url).query).get("q", [""])[0]
        sh.cell(row, 2).value = first_link(q)
        print(f"{row-1}: {sh.cell(row, 2).value}")
        time.sleep(SLEEP)
    wb.save(path.replace(".xlsx", "_done.xlsx"))

# ----- TỰ ĐỘNG TÌM MỌI FILE google_part*.xlsx -----
for f in glob.glob("google_link.xlsx"):
    fill_excel(f)
