# TCP Chatbot

Đây là một chat bot đơn giản sử dụng dụng socket để truyền dữ liễu giữa các máy tình cùng một mạng nội bộ với nhau.

## Cài đặt

###  Cài đặt Python

 1. Tải xuống Python

Truy cập trang web chính thức của Python (https://www.python.org/downloads/) và tải xuống phiên bản phù hợp với hệ điều hành của bạn. Python có hai phiên bản chính là Python 2 và Python 3, tuy nhiên, Python 2 đã ngừng được hỗ trợ và khuyến nghị sử dụng Python 3.

 2. Chạy trình cài đặt

Sau khi tải xuống, chạy file cài đặt Python mà bạn vừa tải về. Trong quá trình cài đặt, hãy chắc chắn chọn các tùy chọn phù hợp, bao gồm cả Add Python to PATH (Thêm Python vào PATH) để có thể sử dụng Python từ bất cứ vị trí nào trên hệ thống.

 3. Kiểm tra cài đặt

Sau khi cài đặt hoàn tất, bạn có thể kiểm tra xem Python đã được cài đặt chính xác hay chưa. Mở Command Prompt (Windows) hoặc Terminal (macOS/Linux) và chạy lệnh sau:

```bash
python --version
```
Nếu phiên bản Python hiển thị, điều đó có nghĩa là Python đã được cài đặt thành công.

###  Cài đặt các thư viện Python cần thiết

* **Sounddevice**

Thư viện sounddevice là một thư viện Python dùng để thao tác với âm thanh trong quá trình xử lý tín hiệu âm thanh thời gian thực. Nó cung cấp các chức năng cho phép ghi và phát âm thanh từ và đến các thiết bị âm thanh trên máy tính.

Để cài đặt thư viện sounddevice chạy lệnh sau.
```bash
pip install sounddevice
```
Lưu ý: Nếu bạn đang sử dụng môi trường ảo (virtual environment), hãy đảm bảo rằng bạn đã kích hoạt môi trường ảo trước khi chạy lệnh cài đặt.

* **Soundfile**

Thư viện soundfile là một thư viện Python được sử dụng để đọc và ghi các file âm thanh (ví dụ: WAV, FLAC) trong mã Python.

Để cài đặt thư viện soundfile chạy lệnh sau.
```bash
pip install soundfile
```

* **Numpy**

Numpy là một thư viện Python phổ biến được sử dụng cho tính toán số học và xử lý mảng nhiều chiều. Thư viện soundfile yêu cầu thư viện numpy để hoạt động.
Để cài đặt thư viện numpy chạy lệnh sau.
```bash
pip install numpy
```

* **PyInstaller**

PyInstaller là một công cụ được sử dụng để đóng gói ứng dụng Python thành các file thực thi độc lập, không cần có môi trường Python cài đặt trên máy tính đích. Nó cho phép bạn tạo ra các file thực thi chạy trên nền tảng tương ứng (Windows, macOS, Linux) mà không cần cài đặt Python hoặc các thư viện Python liên quan trên máy tính sử dụng.

Để cài đặt PyInstaller hãy chạy lệnh sau.
```bash
pip install pyinstaller
```

## Sử dụng
1. Khởi động máy chủ bằng cách chạy server.py
```bash
python.py server2.py
```
2. Client có thể kết nối với máy chủ bằng cách chạy client.py
```bash
python client3.py
```
3. Nhập tên và bắt đầu gửi tin nhắn cho các client khác.

## Đóng gói thành file .exe

1. Trước khi đóng gói, hãy đảm bảo rằng mã nguồn không có lỗi và chạy đúng trên máy tính của mình trước khi tiến hành nén thành file .exe.

2. Sau khi cài đặt PyInstaller và chuẩn bị file Python của mình, ta có thể sử dụng lệnh sau để tạo file .exe.

```bash
pyinstaller --onefile tên_file.py
```

Trong đó:
* --onefile: Chỉ định rằng bạn muốn tạo một file .exe đơn lẻ. Nếu bạn muốn tạo một thư mục chứa nhiều file, bạn có thể bỏ qua tùy chọn này.
* tên_file.py: Là tên file Python muốn đóng gói.

3. Sau khi PyInstaller hoàn tất quá trình, ta sẽ tìm thấy file .exe đã được tạo trong thư mục **dist**. File .exe này có thể được sao chép và chạy trên bất kỳ máy tính nào mà không cần cài đặt Python.