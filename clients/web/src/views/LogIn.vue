<template>
    <div class="wrapper">

        <div class="logo_pic">
            <img src="../assets/img/桃園永續館_LOGO.png" alt="" class="logo_T">
        </div>
        <div class="login">
            <div>
                <img src="../assets/img/Logo.png" alt="" class="logo">
            </div>

            <div>
                <input v-model="userName" type="text" @keyup.enter="login" placeholder="Account" ref="userNameInput" />
            </div>
            <div>
                <input v-model="password" type="password" @keyup.enter="login" placeholder="Password"
                    ref="passwordInput" />
            </div>
            <div>
                <input v-model="captcha" type="text" @keyup.enter="login" placeholder="Captcha" />
            </div>
            <img class="captchaImg" :src="captchaImg" />
            <button class="pan" type="button" @click="login()" :disabled="isButtonDisabled">
                登入
            </button>
        </div>
        <TimeZone/>

    </div>
</template>

<script setup>
// 從 Vue 庫中引入 ref 和 onMounted 函數
import { ref, onMounted, computed } from 'vue';
// 從 axios 庫中引入 axios 物件，用於發送 HTTP 請求
import axios from 'axios';
// 從路由中引入 router，用於導航
import router from '@/router/router';

import TimeZone from '.././components/TimeZone.vue'  // 引入組件

const userNameInput = ref(null);
const passwordInput = ref(null);
const captchaInput = ref(null);
// 定義 userName 的 ref，用於存放用戶名
const userName = ref()
// 定義 password 的 ref，用於存放密碼
const password = ref()
// 定義 captcha 的 ref，用於存放驗證碼
const captcha = ref('')
// 定義 captcha_id 的 ref，用於存放驗證碼 ID
const captcha_id = ref()
// 定義 captchaImg 的 ref，用於存放驗證碼圖片
const captchaImg = ref('')
// const store = useStore(); （此行被註解掉，可能是因為沒有用到 Vuex）

// 計算屬性，判斷登入按鈕是否禁用
const isButtonDisabled = computed(() => {
    return !userName.value || !password.value || !captcha.value; // 若有欄位未填則禁用
});

// 定義 login 函數，用於處理登入操作
const login = () => {
    // 發送 POST 請求到指定 URL，傳遞用戶名、密碼、驗證碼和驗證碼 ID
    axios({
        method: "POST",
        url: "/api/v1/Login",
        data: {
            username: userName.value,
            password: password.value,
            captcha: captcha.value,
            captcha_id: captcha_id.value,
        },
    }).then((response) => {
        // 請求成功後處理返回的數據
        let token = response.data.data;
        // 將 token 存入 sessionStorage
        sessionStorage.setItem("token", token)
        // 彈出提示訊息
        // alert(response.data.message)
        // 導航至指定路由 '/WaterMonitoring'
        router.push('/MainApp')
    }).catch(function (error) {
        // 請求處理失敗時的處理
        if (error.data.message === "captcha not found") {
            // 假設如果有 "captcha not found" 訊息，表示是驗證碼錯誤
            alert("驗證碼錯誤，請重新輸入驗證碼");
            captcha.value = "";  // 清除當前的驗證碼輸入框
            getCaptcha(); // 重新取得新的驗證碼
            captchaInput.value.style.borderColor = "red";
            captchaInput.value.style.backgroundColor = "#f8d7da"; // 淺紅色背景
        } else if (error.data.message === "login fail" || error.data.message === "param error") {

            alert("您輸入的使用者名稱或密碼不正確。請再試一次");
            captcha.value = "";  // 清除當前的驗證碼輸入框
            getCaptcha(); // 重新取得新的驗證碼

            // 設定帳號和密碼輸入框的錯誤樣式
            // 直接使用 ref 訪問 DOM 元素
            userNameInput.value.style.borderColor = "red";
            userNameInput.value.style.backgroundColor = "#f8d7da"; // 淺紅色背景
            userNameInput.value.focus();
            passwordInput.value.style.borderColor = "red";
            passwordInput.value.style.backgroundColor = "#f8d7da"; // 淺紅色背景

        }
        else {

            // 如果沒有錯誤回應，顯示通用錯誤訊息
            alert("驗證碼錯誤，請重新輸入驗證碼");
            captcha.value = "";  // 清除當前的驗證碼輸入框
            getCaptcha(); // 重新取得新的驗證碼
        }

        // 重新載入當前頁面
        // router.go(0);
    });
};

const getCaptcha = async () => {
    // 獲取驗證碼
    await axios
        .get("/api/v1/Captcha")
        .then((response) => {
            // 請求成功後處理返回的數據
            console.log(response);
            // 將返回的驗證碼 ID 賦值給 captcha_id
            captcha_id.value = response.data.data.captcha_id
            // 將返回的驗證碼圖片資料賦值給 captchaImg
            captchaImg.value = response.data.data.captcha_data
        })
        .catch(function (error) {
            // 請求處理失敗時的處理
            console.log(error);
        });
}
// 組件掛載完成後執行的函數
onMounted(async () => {
    // 獲取驗證碼
    await getCaptcha()
})
</script>

<style scoped>
section{
    padding: 3%;
}
/* 資料沒有填完整前禁用登入按鈕 */

button:disabled {
    background: #b8b8b8;
    /* 淺灰色背景 */
    color: #cccccc;
    /* 淺灰色文字 */
    cursor: not-allowed;
    /* 改為禁止點擊的游標 */
}

button:disabled:hover {
    background: #b8b8b8;
    /* 禁用時取消 hover 背景變化 */
    transform: none;
    /* 禁用時取消放大效果 */
}

.wrapper {
    /* height: 100vh; */
max-width: 1200px;
    /* background: rgb(255 255 255 / 60%); */
    margin: auto;
}


.logo {
    width: 200px;
    /* Set the width to 300px */
    height: auto;
    /* Maintain aspect ratio */
}

.logo_pic{
    max-width: 600px;
    margin: auto ;
    
}
.logo_T {
    /* margin: auto; */
    margin-top: 50px ;

    width: 100%;
    /* Set the width to 300px */
    /* height: auto; */
    /* Maintain aspect ratio */
    /* position: relative; */
    /* top: 100px; */
    /* left: 32.5%; */
}

.logo_Test {
    width: 20px;
    /* Set the width to 300px */
    height: auto;
    /* Maintain aspect ratio */
    position: relative;
    top: 100px;
    left: 620px;
}

.login {
    width: 18rem;
    height: 25rem;
    padding: 1.3rem;
    text-align: center;
    background: rgb(255 255 255 / 60%);
    margin: 20px auto;
    border-radius: 1.5rem;
    border: 2px solid rgba(0, 128, 0, 0.284);

}

.login p {
    font-size: 1.3rem;
    color: #0071BB;
}

input {
    width: 100%;
    height: 2.25rem;
    margin-top: 1rem;
    background: rgb(0 0 0 / 20%);
    text-align: center;
    border-radius: 0.5rem;
}

::placeholder {
    font-size: 1rem;
    text-align: center;
    color: #666666;
}

.captchaImg {
    width: 100%;
    margin: 0.5rem 0;
}


button {
    width: 100%;
    pointer-events: auto;
    cursor: pointer;
    background: #07630050;
    border: none;
    padding: 0.5rem 1.5rem;
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    position: relative;
    display: inline-block;
    z-index: 1;
}

button::before,
button::after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.pan {
    font-family: aktiv-grotesk-extended, sans-serif;
    font-weight: 700;
    border-radius: 0.5rem;
    overflow: hidden;
    color: rgb(0, 0, 0);
}

.pan::before {
    content: "";
    background: #b8b8b8d5;
    transition: transform 0.3s cubic-bezier(0.7, 0, 0.2, 1);
    z-index: -1;
}

.pan:hover::before {
    transform: translate3d(0, -100%, 0);
}
</style>