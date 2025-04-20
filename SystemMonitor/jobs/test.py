import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def run():
    print("🚀 Hệ thống phát hiện bất thường bằng ARIMA đã sẵn sàng!")
    # Tạo dữ liệu thật từ 1 đến 50
    y_values = np.arange(1, 51)
    time_index = pd.date_range(start="2025-04-01", periods=len(y_values), freq="T")
    df = pd.DataFrame({"y": y_values}, index=time_index)
    df.index.freq = 'T'
     # Lấy giá trị gần nhất
    last_time = df.index[-1]
    last_value = df["y"].iloc[-1]
    # Dự đoán bước tiếp theo
    model = ARIMA(df["y"], order=(3, 1, 3))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=1)
    forecast_value = forecast[0]
    # Xác định chiều dự đoán
    trend = "🔼 TĂNG" if forecast_value > last_value else "🔽 GIẢM"
    # Nhập giá trị mới từ người dùng
    user_input = 70
    new_value = float(user_input)

    # So sánh sai số
    error = abs(new_value - forecast_value)
    threshold = 2 * df["y"].std()
    is_anomaly = error > threshold

    # Thêm giá trị mới vào chuỗi thời gian
    new_time = last_time + pd.Timedelta(minutes=1)
    df.loc[new_time] = new_value

    # 🖨️ In kết quả
    print("\n🧾 KẾT QUẢ PHÂN TÍCH")
    print(f"⏱️  Thời điểm gần nhất: {last_time} → Giá trị: {last_value:.2f}")
    print(f"📈  Dự đoán tiếp theo : {forecast_value:.2f} ({trend})")
    print(f"📌  Giá trị mới nhập  : {new_value:.2f}")
    print(f"{'🔴 BẤT THƯỜNG' if is_anomaly else '🟢 BÌNH THƯỜNG'} (|sai số| = {error:.2f}, ngưỡng = {threshold:.2f})")

    # 📊 Vẽ biểu đồ
    plt.figure(figsize=(12, 6))
    plt.plot(df.index[-50:], df['y'].iloc[-50:], label='Dữ liệu thực tế (cuối)', color='blue')
    plt.scatter(new_time, new_value, color='red', label='Giá trị bạn nhập', zorder=5)
    plt.scatter(new_time, forecast_value, color='green', label='Dự đoán ARIMA', zorder=5)
    plt.axhline(y=last_value, color='gray', linestyle='--', alpha=0.5, label=f"Giá trị gần nhất: {last_value:.2f}")

    plt.title('So sánh Dự đoán ARIMA & Giá trị mới', fontsize=14)
    plt.xlabel('Thời gian')
    plt.ylabel('Số lượng Request')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
   

