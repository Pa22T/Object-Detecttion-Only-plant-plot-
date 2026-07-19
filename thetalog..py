import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv('theta_real_dist_log.csv')

# สร้างกราฟ
plt.figure(figsize=(10, 5))
plt.plot(df['frame'], df['theta_deg'], color='blue', linewidth=1)

# --- ส่วนที่เพิ่ม/แก้ไข ---
plt.ylim(-10, 10) # กำหนดช่วงของแกน Y ให้เป็น -10 ถึง 10
# -----------------------

# กำหนดชื่อแกนและชื่อกราฟ
plt.xlabel('Frame')
plt.ylabel('Theta (degrees)')
plt.title('Theta/Frame')
plt.grid(True)

# แสดงผลกราฟ
plt.show()