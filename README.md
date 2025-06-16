# franchise-research-python-on_going
Scripts &amp; docs for scraping top 400 global franchises and download data 400 global franchises' FDD from 2017 to 2023
# Franchise Research (Python Automation)

**Goal:** Build an automated pipeline to collect, clean & deliver data on the top 400 global franchise brands.

## Workflow_1
1. Fetch list from Entrepreneur Franchise 500 & other sources.
2. Use `requests` + `BeautifulSoup` to scrape brand profiles.
3. Clean & merge data with `pandas`; export to Excel.
4. Validate manually (random 5 %) before delivery.
Sau khi có danh sách tên công ty được trích xuất từ PDF, sử dụng hàm HYPERLINK và ENCODEURL => Để tìm kiếm công ty có trong danh sách top 400 trên google
E.g. Cột A là Chili’s -> sẽ trả kết quả cột B là kết quả tìm kiếm của google. Kết quả đầu tiên sẽ là link dẫn đến <https://www.franchisetimes.com/top-400-2024/26-chilis/article_67d6fca6-5668-11ef-9c7c-03e75a70ff0b.html>
Các thư viện python đã sử dụng: 
selenium: điều khiển trình duyệt
pandas: đọc/ghi Excel, xử lý DataFrame
openpyxl: backend cho pandas khi xuất file .xlsx
requests: gửi HTTP request, tải file
lxml: parse HTML qua lxml.html và XPath
beautifulsoup4 (tuỳ chọn): parse HTML bằng BS4 nếu không dùng lxml

Bước 1: Sau khi đã có danh sách link google như trên sử dụng python để lấy kết quả là link đầu tiên như trên. 
Bước 2: Tạo 1 file excel 400_Franchiese gồm các cột cần lấy dữ liệu như Franchisor's name, Lowest investment (USD), Highest investment (USD), Initial investment, Category, Global Sales, US Units, International Units, Percent Franchised (%), % International Units, US Franchised Units, International Franchised Units, Sales Growth (%), Unit Growth (%), Link (lấy được ở Bước 1)
Bước 3: Chạy Python và sẽ trả ra file 400_Franchiese_Filled. File này sẽ có đầy đủ dữ liệu của các cột ở bước 2
Bước 4: Kiểm tra lại file kết quả. Những hàng/ô trống không ra kết quả sẽ được kiểm tra và điền dữ liệu thủ công

## Workflow_2
- Tạo Folder Tổng FDD → Tạo các Folder theo tên Franchise riêng biệt (E.g. FDD/Chilis/Chilis-fdd.pdf).
- Dựa vào tên top 400 franchise đang lấy từ đầu. Mở Tab ẩn danh → Truy cập vào Franchisepanda.com → chọn mục browse A to Z → Chọn chữ cái đầu franchise đang cần tải, E.g. #26 Chili’s → chọn C → Control + F → Paste Chili’s → chọn Get details → Kéo xuống chọn FDD trong khoảng 2017 đến 2024 → Điền thông tin và email → truy cập mail và tải link về đúng folder tên franchise. Tiếp tục với 400 franchise tiếp theo tương tự.
Notes: tải khoảng 12-20 FDD sẽ không cho tải nữa và hiện thế này. Chỉ cần tắt tab ẩn danh và mở tab ẩn danh khác mới, điền lại thông tin mail như cũ và tải về bình thường.
- Sau khi download xong FDD từ 2017-2024 về đúng folder các franchise. Điền Y/N vào file Excel (Top 400 Franchise - FDD). 

## Key Result
* ⏱️ Saved ~70 % manual data‐entry time.
* 📊 Delivered 400-row structured dataset in XLSX & CSV.
* Downloaded 400 global franchises' FDD and report.

## Files
* `scrape_franchise.py` – main script  
* `sample_output.xlsx` – anonymised demo  
* `requirements.txt`
