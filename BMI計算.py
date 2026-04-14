# A114510313 江惠宇

raw_input = input("請輸入 性別(M/F), 年齡, 身高(cm), 體重(kg)，以逗號隔開：")
parts = raw_input.split(',')
gender = parts[0].strip().upper()
age = int(parts[1])
h = float(parts[2])
w = float(parts[3])

bmi = w / (h / 100) ** 2
print("-" * 30)
print(f"您的 BMI 為：{bmi:.2f}")

# --- 1. 計算 BMR (基礎代謝率) ---
if gender == "M":
    bmr = 10 * w + 6.25 * h - 5 * age + 5
else:
    bmr = 10 * w + 6.25 * h - 5 * age - 161

print(f"您的基礎代謝率 (BMR) 為：{bmr:.0f} 大卡")

# --- 2. 詢問活動量並計算 TDEE ---
print("\n請選擇您的活動量：")
print("1. 久坐 (辦公室工作、沒運動)")
print("2. 輕度 (每週運動 1-3 天)")
print("3. 中度 (每週運動 3-5 天)")
activity_level = input("請輸入數字 (1-3)：")

if activity_level == "1":
    tdee = bmr * 1.2
elif activity_level == "2":
    tdee = bmr * 1.375
else:
    tdee = bmr * 1.55

print(f"您的每日總消耗熱量 (TDEE) 為：{tdee:.0f} 大卡")

# --- 3. 結合 BMI 給出人性化飲食建議 ---
print("-" * 30)
if bmi > 24:
    print(f"【減重建議】")
    print(f"為了安全減重，建議每日攝取約 {tdee - 300:.0f} ~ {tdee - 500:.0f} 大卡。")
    print("搭配原型食物與規律運動，效果會更好喔！")
elif bmi < 18.5:
    print(f"【增重建議】")
    print(f"建議每日攝取約 {tdee + 300:.0f} 大卡，並加強重量訓練來增加肌肉。")
else:
    print(f"【維持建議】")
    print(f"每日攝取 {tdee:.0f} 大卡即可維持現狀，請繼續保持均衡飲食！")