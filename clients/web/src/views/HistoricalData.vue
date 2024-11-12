<template>
    <div class="btc">

        <div class="home">
            <button @click="goToB">
                <span class="material-symbols-outlined"> home </span>
                <h2>主頁</h2>
            </button>

            <!-- 增加一個容器來包裹 LogoutComponent，並限制容器的大小 -->

            <LogoutComponent />

        </div>


        <div class="button_list">

            <!-- 新增區域選擇的下拉選單 -->
            <div class="px_1920">
                <label for="">站點 : </label>
                <div class="select-wrapper">
                    <select class="pan" v-model="station" @change="updateStation">
                        <option v-for="(item, index) in stations" :key="index" :value="item.uuid">
                            {{ item.id }}
                        </option>
                    </select>
                </div>
                <input class="pan vk" type="date" lang="en" v-model="startTime" required>
                <input class="pan vk" type="date" lang="en" v-model="endTime" required>
                <div class="select-wrapper">
                    <select class="pan" v-model="interval">
                        <option>5 分鐘</option>
                        <option>10 分鐘</option>
                    </select>
                </div>
            </div>


            <div class="px_920">
                <button class="pan search" type="submit" @click="searchTimeSeriesByStation()">
                    <span class="material-symbols-outlined"> search </span>
                    <h2>搜尋</h2>
                </button>
                <Vue3JsonExcel :json-data="tableData" :fields="json_fields" :name="`Historical_${currentStationName}.xlsx`">
                    <button class="pan kk">
                        <span class="material-symbols-outlined"> exit_to_app </span>
                        <h2>匯出</h2>
                    </button>
                </Vue3JsonExcel>
            </div>

            <div class="table-wrapper">
                <table class="fl-table">
                    <thead>
                        <tr>
                            <th v-for="(item, index) in tableHead" :key="index">
                                {{ item.full_name }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(tr_item, tr_index) in tableData" :key="tr_index">
                            <td v-for="(td_item, td_index) in tr_item" :key="td_index">
                                {{ td_item }}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="title" >
                <!-- 顯示當前站點名稱 -->
                <h2>當前站點: {{ currentStationName }}</h2>
            </div>
    </div>


</template>

<script setup>
import router from '@/router/router';


const goToB = () => {

    router.push('/MainApp');
}
// import axios from 'axios';
// import router from '@/router'; 
// import router from '@/router/router';


// const goToC = () => {

//     router.push('/LogIn');
//     console.log('ssss')
// }
// // 從 Vue 庫中引入 ref 和 onMounted 函數
import { ref, onMounted, watch } from 'vue';
// 從 axios 庫中引入 axios 物件，用於發送 HTTP 請求
import axios from 'axios'
// 從 vue3-json-excel 庫中引入 Vue3JsonExcel 元件，用於 Excel 匯出
import { Vue3JsonExcel } from 'vue3-json-excel';
// 從自定義模組中引入 formatDateTime 和 formatToLocalDateTime 函數，用於日期格式化
import { formatDateTime, formatToLocalDateTime } from '@/assets/js/formatDateTime';
import LogoutComponent from "@/components/LogoutComponent.vue";

// 獲取當前日期
const date = new Date();
// 獲取當前日，並格式化為兩位數
const day = ("0" + date.getDate()).slice(-2);
// 獲取當前月，並格式化為兩位數
const month = ("0" + (date.getMonth() + 1)).slice(-2);
// 獲取今天的日期，格式為 yyyy-MM-dd
const today = date.getFullYear() + "-" + month + "-" + day;
// 定義 stations 的 ref，初始值為空數組，用於存放站點數據
const stations = ref([])
// 定義 station 的 ref，初始值為空字符串，用於存放選定的站點
const station = ref("")
const currentStationName = ref('');

// 定義 startTime 的 ref，初始值為今天，用於存放開始時間
const startTime = ref(today)
// 定義 endTime 的 ref，初始值為今天，用於存放結束時間
const endTime = ref(today)
// 定義 interval 的 ref，初始值為 "5m"，用於存放時間間隔
const interval = ref("5 分鐘")
// 定義 tableHead 的 ref，未初始化，用於存放表格標題
const tableHead = ref();
// 定義 tableData 的 ref，未初始化，用於存放表格數據
const tableData = ref();
// 定義 json_fields 的 ref，未初始化，用於存放 JSON 欄位
const json_fields = ref({})
// 監控 startTime 和 endTime 的變化
watch([startTime, endTime], ([newStartTime, newEndTime]) => {
    // 檢查兩個日期之間的天數差異
    const calculateDateDifference = (start, end) => {
        const startDate = new Date(start);
        const endDate = new Date(end);

        // 檢查兩個日期是否有效
        if (isNaN(startDate) || isNaN(endDate)) {
            return 0;
        }

        // 計算日期差異（以天為單位）
        const timeDifference = endDate - startDate;
        return timeDifference / (1000 * 3600 * 24);  // 轉換為天數
    };
    const dateDiff = calculateDateDifference(newStartTime, newEndTime);
    // 如果日期範圍超過 180 天，顯示錯誤
    if (dateDiff > 180) {
        alert("日期選取範圍不可大於180天")
        startTime.value = today;
        endTime.value = today;
    }
    // 檢查 startTime 是否大於 endTime
    if (newStartTime && newEndTime && newStartTime > newEndTime) {
        alert("開始時間必需小於結束時間");



        // 當 startTime > endTime 時，將 startTime 重置為今天的日期
        startTime.value = today;
        endTime.value = today;
    }
});
// 定義 getAllStation 函數，用於獲取所有站點數
const getAllStation = async () => {
    await axios({
        method: "Get",
        url: "/api/v1/Station"
    }).then((response) => {
        stations.value = response.data.data;

        station.value = response.data.data[0].uuid;
        updateStationName();
    })
        .catch(function (error) {
            console.log(error);
        });
}

const updateStationName = () => {
    const selected = stations.value.find(s => s.uuid === station.value);
    if (selected) {
        currentStationName.value = selected.name;
    }
};
// 定義 searchTimeSeriesByStation 函數，用於根據站點搜尋時間序列數據
const searchTimeSeriesByStation = async () => {
    const formattedInterval = interval.value === "5 分鐘" ? "5m" : interval.value === "10 分鐘" ? "10m" : interval.value;
    await axios({
        method: "POST",
        url: "/api/v1/TimeSeries/Station",
        data: {
            station_uuid: station.value,
            start_time: formatToLocalDateTime(startTime.value),
            end_time: endTime.value === today ? date : formatToLocalDateTime(endTime.value).replace('00:00:00', '23:59:59'),
            interval: formattedInterval,
            reverse: true,
        }
    }).then((response) => {

        response.data.data.columns.forEach((element, index) => {
            if (element.full_name === "pH") {
                element.full_name = "酸鹼值"; // 將 ph 改為 酸鹼值
            } else if (element.full_name === "time") {
                element.full_name = "時間"; // 將 time 改為 時間
            }
            json_fields.value[element.full_name] = index.toString()
        });
        tableHead.value = response.data.data.columns
        response.data.data.data.forEach(element => {
            let newTime = formatDateTime(element[0])
            element[0] = newTime.slice(0, 16)
            updateStationName();

        })
        tableData.value = response.data.data.data
    })
        .catch(function (error) {
            console.log(error);
        });
}

onMounted(async () => {
    await getAllStation()
    await searchTimeSeriesByStation()
})
</script>

<style scoped>
* {
    box-sizing: border-box;
}

.title{
    width: 80%;
    margin: auto;
    font-weight: bold;
}
.title h2{
    margin-top: 20px;
}
label {
    display: flex;
    flex-wrap: nowrap;
    font-size: clamp(16px, 2vw, 24px);
    white-space: nowrap;

}

button {
    /* display: flex; */
    /* align-items: center; */
    /* margin-right: 3rem; */
    color: #11aa00;
    background: inherit;
    cursor: pointer;
    font-size: clamp(14px, 2.5vw, 28px);
    /* 根據畫面大小調整字體 */
    padding: clamp(8px, 1.3%, 16px);
    /* 使用相對單位調整內距 */
    margin: auto;
    transition: background-color 0.3s ease, transform 0.3s ease;
    /* 過渡效果 */
    /* position: stinky; */
    margin: unset;
    margin-left: auto;

}

button:hover {
    background-color: #c4fcc635;
    /* 懸停時背景顏色 */
    transform: scale(1.05);
    /* 懸停時縮放效果 */
}

.search,
.kk {
    font-size: clamp(16px, 2vw, 24px);
    padding: clamp(8px, 1.3%, 16px);
    /* 使用相對單位調整內距 */
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}

.search span,
.kk span {
    font-size: clamp(16px, 2vw, 24px);


}

.material-symbols-outlined {
    font-variation-settings:
        'FILL' 1,
        'wght' 700,
        'GRAD' 0,
        'opsz' 48;
}

/* .button_list {
    text-align: center;
} */


.pan {
    /* margin: 0 0.5rem 0.5rem 0; */
    margin: clamp(-16px, -0.573vw, -11px) clamp(2px, 0.521vw, 10px);
    border-radius: 20px;
    text-align: center;


}

.pan:last-child {
    /* margin-right: 0; */
}

.px_1920 input[type="date"]::-webkit-calendar-picker-indicator {
    position: absolute;
    padding-left: 100%;
    right: 1rem;
}

.px_1920 input[type="date"]::-webkit-calendar-picker-indicator:hover {
    filter: invert(1);
}

input,
select {
    pointer-events: auto;
    cursor: pointer;
    border: none;
    padding: clamp(8px, 1.3%, 16px);
    /* 使用相對單位調整內距 */
    margin: 0;
    font-size: clamp(16px, 2vw, 24px);
    font-family: inherit;
    position: relative;
    display: inline-block;
    z-index: 1;
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    position: relative;

}

select {
    appearance: none;
    /* 去除默认样式 */
    background: url('data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"%3E%3Cpath d="M4.293 5.293a1 1 0 0 1 1.414 0L8 7.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z" fill="%23333"%3E%3C/path%3E%3C/svg%3E') no-repeat right center;
    background-size: 16px 16px;
    /* 调整箭头图标大小 */
    background-position: calc(100% - 10px) center;
    /* 给箭头留出 padding */
    padding-right: 30px;
    /* 给右侧留出空间放置图标 */
}

.pan::before {
    content: "";
    background: #BEBEBE;
    transition: transform 0.3s cubic-bezier(0.7, 0, 0.2, 1);
    z-index: -1;
}

.pan:hover::before {
    transform: translate3d(0, -100%, 0);
}

.material-symbols-outlined {
    font-variation-settings:
        'FILL' 1,
        'wght' 700,
        'GRAD' 0,
        'opsz' 48;
}

/* .material-symbols-outlined:hover {
    color: white;
} */
/* #app {
     display: flex;
     flex-direction: column;
     align-items: center;
 } */
.px_920 {
    display: flex;
    align-items: center;

}

.button_list {
    position: relative;
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
    text-align: center;
    width: 80%;
    height: auto;
    display: flex;
    /* justify-content: space-between; */
    margin: 20px auto;
    /* padding: 1px 1px; */

}

.px_1920 {
    display: flex;
    justify-content: center;
    align-items: center;
}

.button_list span {
    display: flex;
}

.table-container {
    position: relative;
    /* 或者使用 absolute 根据需要 */
    width: 100%;
    height: 10vh;
    /* 确保容器高度 */
}

.table-wrapper {
    position: absolute;
    top: 300%;
    left: 50%;
    /* height: 69.9vh; */
    width: 100%;
    transform: translateX(-50%);
    box-shadow: 0px 35px 50px rgba(0, 0, 0, 0.2);
    /* overflow: auto; */
}


.fl-table {
    margin: 0 auto;
    border-radius: 5px;
    font-size: 15px;
    font-weight: normal;
    border: none;
    border-collapse: collapse;
    width: 100%;
    max-width: 100%;
    background-color: white;
    table-layout: fixed;
}

.fl-table td,
.fl-table th {
    text-align: center;
    padding: 8px;
}

.fl-table th {
    position: sticky;
    top: 0;
    color: #ffffff;
    background: #1BB9EE;

    font-size: 1rem;
}

.fl-table td {
    border-right: 1px solid #f8f8f8;
    font-size: 0.8rem;
}

.fl-table td:last-child {
    border-right: none;
}

.fl-table thead th:nth-child(odd) {
    color: #ffffff;
    background: #00803E;

}

.fl-table tr:nth-child(even) {
    background: #F8F8F8;
}

/* Responsive */
@media (max-width: 1024px) {
    .fl-table th {
        word-wrap: break-word;
        /* 允许 <th> 元素的内容换行 */
    }

    .fl-table td {
        white-space: break-spaces;
        /* 禁止 <td> 元素的内容换行 */
    }
}

;

@media (max-width: 920px) {
    .button_list {
        flex-direction: column;
        margin-top: 20px;
    }

    .px_920 {
        justify-content: center;
        margin-top: 30px;
    }

    .table-wrapper {
        top: 180%
    }
}

@media (max-width: 720px) {

    .px_1920{
    flex-wrap: wrap;
    margin: 10px 0 10px 0;
}
.px_1920>div,
.px_1920>input{
    margin-top: 10px; /* 調整此值來控制上下間距 */
    margin-bottom: 10px;
}
    .fl-table {
        display: block;
        width: 100%;
    }

    .table-wrapper:before {
        content: "";
        display: block;
        text-align: right;
        font-size: 11px;
        color: white;
        padding: 0 0 10px;
    }

    .fl-table thead,
    .fl-table tbody,
    .fl-table thead th {
        display: block;
    }

    .fl-table thead th:last-child {
        border-bottom: none;
    }

    .fl-table thead {
        float: left;
    }

    .fl-table tbody {
        width: auto;
        position: relative;
        overflow-y: auto;
    }

    .fl-table td,
    .fl-table th {
        padding: 20px .625em .625em .625em;
        height: 60px;
        vertical-align: middle;
        box-sizing: border-box;
        overflow-x: hidden;
        overflow-y: auto;
        width: 120px;
        font-size: 13px;
        text-overflow: ellipsis;

    }

    .fl-table thead th {
        text-align: center;
        border-bottom: 1px solid #f7f7f9;
    }

    .fl-table tbody tr {
        display: table-cell;
    }

    .fl-table tbody tr:nth-child(odd) {
        background: none;
    }

    .fl-table tr:nth-child(even) {
        background: transparent;
    }

    .fl-table tr td:nth-child(odd) {
        background: #F8F8F8;
        border-right: 1px solid #E6E4E4;
    }

    .fl-table tr td:nth-child(even) {
        border-right: 1px solid #E6E4E4;
    }

    .fl-table tbody td {
        display: block;
        text-align: center;
    }
}

.home {
    display: flex;
    width: 80%;
    margin: auto;
    align-items: center;

}

.home button {
    margin-left: auto;

}

.vk {
    padding-top: clamp(8px, 1.3%, 16px);
    padding-left: clamp(8px, 1.3%, 16px);
    padding-right: clamp(25px, 1.8vw, 40px);
    padding-bottom: clamp(8px, 1.3%, 16px);
}
</style>