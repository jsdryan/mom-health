# mom-health

媽媽的減脂飲食紀錄：https://jsdryan.github.io/mom-health/

- 每日目標依 2026.10.25 XOFIT 身體組成報告設定：1,300 大卡、蛋白質 80 公克、碳水 150 公克、脂肪 42 公克。
- 餐點資料在 `data.json`，每天新增一筆 `days`；`index.html` 載入時讀取。
- 網址加上 `#demo` 會顯示 14 天的示範資料，用來預覽多日畫面，不影響真實紀錄。
- 體重自動更新：iPhone 捷徑呼叫 GitHub Actions 的「新增體重」流程（`.github/workflows/weight.yml`），把最新體重寫進 `data.json`。
