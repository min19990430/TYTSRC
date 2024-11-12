<template>
    <div class="time-container">
      <h1>即時時間</h1>
  
      <div class="timezone-selector">
        <label for="timezone">選擇時區:</label>
        <select v-model="selectedTimezone" @change="updateTime" class="timezone-dropdown area" >
          <option v-for="timezone in timezones" :key="timezone" :value="timezone">{{ timezone }}</option>
        </select>
      </div>
  
      <div class="time-display">
        <p>當前時間：{{ formattedTime }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedTimezone: "UTC",
        timezones: ["UTC", "Asia/Taipei", "America/New_York", "Europe/London", "Asia/Tokyo"],
        currentTime: new Date(),
        formattedTime: "",
      };
    },
    methods: {
      updateTime() {
        const formatter = new Intl.DateTimeFormat("zh-TW", {
          timeZone: this.selectedTimezone,
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        });
        this.formattedTime = formatter.format(this.currentTime);
      },
    },
    mounted() {
      setInterval(() => {
        this.currentTime = new Date();
        this.updateTime();
      }, 1000);
    },
  };
  </script>
  
  <style scoped>
  /* 主要容器樣式 */
  .time-container {
    font-family: 'Arial', sans-serif;
    text-align: center;
    padding: 20px;
    background-color: #f0f8ff;
    border-radius: 8px;
    width: 300px;
    margin: 50px auto;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    position: fixed;
    right: -17%;
    bottom: 0;
    opacity: .5;
    transition: 1s;
    z-index: 2;
  }

  .time-container::before{
    content: "<";
    position: absolute;
    top: 50%;
    left: 1%;
  }


.time-container:hover{
    right: 0;
    opacity: 1;
}

.time-container:hover::before {
  content: ""; /* 在 hover 時隱藏 < */
}
  
  /* 標題樣式 */
  h1 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
  }
  
  /* 時區選擇容器樣式 */
  .timezone-selector {
    margin-bottom: 20px;
  }
  
  /* 時區下拉選單樣式 */
  .timezone-dropdown {
    padding: 8px;
    font-size: 16px;
    border-radius: 4px;
    border: 1px solid #ccc;
    width: 100%;
    text-align:center;
  }
  
  /* 顯示時間的容器樣式 */
  .time-display p {
    font-size: 18px;
    color: #333;
    font-weight: bold;
  }
  </style>
  