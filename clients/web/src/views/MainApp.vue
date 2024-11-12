<template>
    <div class="btc">
<div class="home">
        <button @click="goToB">
            <span class="material-symbols-outlined"> manage_search </span>
            <h2>歷史資料</h2>
        </button>

    <LogoutComponent/>
        </div>

        <div>
            <Suspense>
                <template #default>
                    <div class="container">
                        <div class="A">
                            <b class="b1"> A</b>
                            <b class="b2"> 區</b>
                            <div class="c_flex">
                                <div class="C1">
                                    <img src="../assets/img//blue/ph.png" alt="" class="mini_it">
                                    <b class="c1"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;酸鹼值 </b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.ph.val }}</b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.ph.unit_name }}</b>
                                </div>
                                <div class="C2">
                                    <img src="../assets/img//blue/level.png" alt="" class="mini_it">
                                    <b class="c2"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水位 </b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.water_level.val }}</b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.water_level.unit_name }}</b>
                                </div>
                                <div class="C3">
                                    <img src="../assets/img//blue/c.png" alt="" class="mini_it">
                                    <b class="c3"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;溫度 </b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.temp.val }}</b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ A.temp.unit_name }}</b>
                                </div>
                            </div>
                        </div>
                        <div class="B">
                            <b class="b1"> B</b>
                            <b class="b2"> 區</b>
                            <br>
                            <div class="c_flex">
                                <div class="C1">
                                    <img src="../assets/img//green/ph.png" alt="" class="mini_it">
                                    <b class="c1"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;酸鹼值 </b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.ph.val }}</b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.ph.unit_name }}</b>
                                </div>
                                <div class="C2">
                                    <img src="../assets/img//green/level.png" alt="" class="mini_it">
                                    <b class="c2"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水位 </b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.water_level.val }}</b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.water_level.unit_name }}</b>
                                </div>
                                <div class="C3">
                                    <img src="../assets/img//green/c.png" alt="" class="mini_it">
                                    <b class="c3"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;溫度 </b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.temp.val }}</b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ B.temp.unit_name }}</b>
                                </div>
                            </div>

                        </div>
                        <div class="C">
                            <b class="b1"> C</b>
                            <b class="b2"> 區</b>
                            <div class="c_flex">
                                <div class="C1">
                                    <img src="../assets/img//yellow/ph.png" alt="" class="mini_it">
                                    <b class="c1"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;酸鹼值 </b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.ph.val }}</b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.ph.unit_name }}</b>
                                </div>
                                <div class="C2">
                                    <img src="../assets/img//yellow/level.png" alt="" class="mini_it">
                                    <b class="c2"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水位 </b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.water_level.val }}</b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.water_level.unit_name }}</b>
                                </div>
                                <div class="C3">
                                    <img src="../assets/img//yellow/c.png" alt="" class="mini_it">
                                    <b class="c3"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;溫度 </b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.temp.val }}</b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ C.temp.unit_name }}</b>
                                </div>
                            </div>
                        </div>
                        <div class="D">
                            <b class=" b1"> D</b>
                            <b class="b2"> 區</b>
                            <div class="c_flex">
                                <div class="C1">
                                    <img src="../assets/img/grey/ph.png" alt="" class="mini_it">
                                    <b class="c1"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;酸鹼值 </b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.ph.val }}</b>
                                    <b class="c1">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.ph.unit_name }}</b>
                                </div>
                                <div class="C2">
                                    <img src="../assets/img/grey/level.png" alt="" class="mini_it">
                                    <b class="c2"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水位 </b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.water_level.val }}</b>
                                    <b class="c2">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.water_level.unit_name }}</b>
                                </div>
                                <div class="C3">
                                    <img src="../assets/img/grey/c.png" alt="" class="mini_it">
                                    <b class="c3"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;溫度 </b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.temp.val }}</b>
                                    <b class="c3">&nbsp;&nbsp;&nbsp;&nbsp;{{ D.temp.unit_name }}</b>
                                </div>
                            </div>

                        </div>
                        <!-- <div class="B">
            <span class="material-symbols-outlined"> B區</span><br><br>
            <span class="material-symbols-outlined"> water_ph酸鹼值000 </span><br><br>
            <span class="material-symbols-outlined"> water水位 </span><br><br>
            <span class="material-symbols-outlined"> dew_point溫度000 </span><br>
          </div>
          <div class="C">
            <span class="material-symbols-outlined"> C區</span><br><br>
            <span class="material-symbols-outlined"> water_ph酸鹼值000 </span><br><br>
            <span class="material-symbols-outlined"> water水位 </span><br><br>
            <span class="material-symbols-outlined"> dew_point溫度 </span><br>
          </div>
          <div class="D">
            <span class="material-symbols-outlined"> D區</span><br><br>
            <span class="material-symbols-outlined"> water_ph酸鹼值000 </span><br><br>
            <span class="material-symbols-outlined"> water水位 </span><br><br>
            <span class="material-symbols-outlined"> dew_point溫度 </span><br>
          </div> -->
                    </div>
                </template>
                <template #fallback>
                    <div>Loading...</div>
                </template>
            </Suspense>

        </div>
    </div>

</template>

<script setup>

import { ref, onMounted } from 'vue';
import axios from 'axios';
// import router from '@/router'; 
import router from '@/router/router';
import LogoutComponent from "@/components/LogoutComponent.vue";

const goToB = () => {

    router.push('/HistoricalData');
}

const A = ref({
    id: '',
    update_time: '',
    coordinate: { lng: 0, lat: 0 },
    ph: {
        unit_name: '',
        val: 0,
    },
    temp: {
        unit_name: '',
        val: 0,
    },
    water_level: {
        unit_name: '',
        val: 0,
    },
});
const B = ref({
    id: '',
    update_time: '',
    coordinate: { lng: 0, lat: 0 },
    ph: {
        unit_name: '',
        val: 0,
    },
    temp: {
        unit_name: '',
        val: 0,
    },
    water_level: {
        unit_name: '',
        val: 0,
    },
});
const C = ref({
    id: '',
    update_time: '',
    coordinate: { lng: 0, lat: 0 },
    ph: {
        unit_name: '',
        val: 0,
    },
    temp: {
        unit_name: '',
        val: 0,
    },
    water_level: {
        unit_name: '',
        val: 0,
    },
});

const D = ref({
    id: '',
    update_time: '',
    coordinate: { lng: 0, lat: 0 },
    ph: {
        unit_name: '',
        val: 0,
    },
    temp: {
        unit_name: '',
        val: 0,
    },
    water_level: {
        unit_name: '',
        val: 0,
    },
});

// 異步加載數據
const fetchData = async () => {
    try {
        const response = await axios({
            method: 'GET',
            url: '/api/v1/Last/Station',
            params: {
                uuid: 'ece798f0-8aa5-4327-8ae3-28d9f3590fdb',
            },
        });

        response.data.data.last.forEach(element => {
            switch (element.station.uuid) {
                case 'ece798f0-8aa5-4327-8ae3-28d9f3590fdb': {
                    element.physical_quantities.forEach(ele => {
                        switch (ele.uuid) {
                            case '819f0b87-7252-4e18-9a0f-4bfc3257935c': {
                                A.value.ph.val = ele.value;
                                A.value.ph.unit_name = ele.si_unit;
                                break;
                            }
                            case 'cf8bf85a-2252-4d24-8572-49dde1c004ad': {
                                A.value.temp.val = ele.value;
                                A.value.temp.unit_name = ele.si_unit;

                                break;
                            }
                            case '5530bb22-524b-40a2-8e75-5651e711c303': {
                                A.value.water_level.val = ele.value;
                                A.value.water_level.unit_name = ele.si_unit;
                                break;
                            }
                            // 添加其他 case 處理
                            default:
                                break;
                        }
                    });
                    break;
                }
                case '574fa3ea-48ca-4495-92e5-083fef5091bb': {
                    element.physical_quantities.forEach(ele => {
                        switch (ele.uuid) {
                            case '4ccc917a-d8e0-4e5a-bfdd-5d17040df7c8': {
                                B.value.ph.val = ele.value;
                                B.value.ph.unit_name = ele.si_unit;
                                break;
                            }
                            case '716ce488-a740-465c-a666-94f283fa6d49': {
                                B.value.temp.val = ele.value;
                                B.value.temp.unit_name = ele.si_unit;

                                break;
                            }
                            case '55618f11-6235-448d-92a9-855bb183bb19': {
                                B.value.water_level.val = ele.value;
                                B.value.water_level.unit_name = ele.si_unit;
                                break;
                            }
                            // 添加其他 case 處理
                            default:
                                break;
                        }
                    });
                    break;
                }
                case 'e7c941f7-cc42-4e86-a269-306eb6904fa2': {
                    element.physical_quantities.forEach(ele => {
                        switch (ele.uuid) {
                            case 'a59968ec-0c1e-4f18-9164-d1a8460610ac': {
                                C.value.ph.val = ele.value;
                                C.value.ph.unit_name = ele.si_unit;
                                break;
                            }
                            case 'e2330a7c-ceb0-4e27-98da-59c2b8d88c04': {
                                C.value.temp.val = ele.value;
                                C.value.temp.unit_name = ele.si_unit;

                                break;
                            }
                            case '4792f601-87c1-4d7d-9fd7-2a24aaae2929': {
                                C.value.water_level.val = ele.value;
                                C.value.water_level.unit_name = ele.si_unit;
                                break;
                            }
                            // 添加其他 case 處理
                            default:
                                break;
                        }
                    });
                    break;
                }
                case 'eeac082d-76e0-4066-a163-73e27a7d54f4': {
                    element.physical_quantities.forEach(ele => {
                        switch (ele.uuid) {
                            case '9501e630-56af-42a9-a143-15c6fb6b066f': {
                                D.value.ph.val = ele.value;
                                D.value.ph.unit_name = ele.si_unit;
                                break;
                            }
                            case 'b17aaa51-959d-4b10-8901-0f474a457fe8': {
                                D.value.temp.val = ele.value;
                                D.value.temp.unit_name = ele.si_unit;
                                break;
                            }
                            case '241518bb-5870-4c0c-a932-efcdbb4244c4': {
                                D.value.water_level.val = ele.value;
                                D.value.water_level.unit_name = ele.si_unit;
                                break;
                            }
                            // 添加其他 case 處理
                            default:
                                break;
                        }
                    });
                    break;
                }
                default:
                    break;
            }
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

onMounted(fetchData);
</script>

<style >
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400&display=swap');
/* .phicon::before {
    content: url('path/to/your/icon.png');
    line-height: 0;
    margin-right: 0.3rem;
    font-size: 50px;
}

.waterlavelicon::before {
    content: url('path/to/your/icon.png');
    line-height: 0;
    margin-right: 0.3rem;
    font-size: 50px;
}

.tempicon::before {
    content: url('path/to/your/icon.png');
    line-height: 0;
    margin-right: 0.3rem;
    font-size: 50px;
} */

* {
    margin: 0;
    padding: 0;
    outline: 0;
    appearance: none;
    border: 0;
    text-decoration: none;
    list-style-type: none;
    /* box-sizing: border-box; */
    font-family: 'Noto Sans TC', sans-serif;
}


main {
    width: 85%;
    height: auto;
    padding: 1rem 0 1rem 0;
    margin: 0 auto;
}
.home {
    display: flex;
    align-items: center;
    width: 80%;
    margin:auto ;
}
.home span{
    font-size: 30px;
}
.home h2{
    margin-left:auto;
    font-size: clamp(16px,2vw ,28px);
}

@media screen and (max-width: 1440px) {
    main {
        width: 95%;

    }
}


button {
    display: flex;
    align-items: center;
    /* margin-right: 3rem; */
    color: #11aa00;
    white-space: nowrap;
    background: inherit;
    cursor: pointer;
    /* font-size: 20px; */
    /* padding: 10%; */
    transition: background-color 0.3s ease, transform 0.3s ease;
    /* 過渡效果 */
    /* position: stinky; */
    margin: unset;
    border-radius: 20px;
    margin-left: auto;
    font-size: clamp(16px, 1.05vw, 100px);

}

button:hover {
    background-color: #c4fcc635;
    /* 懸停時背景顏色 */
    transform: scale(1.05);
    /* 懸停時縮放效果 */
}

.material-symbols-outlined {
    line-height: 0;
    margin-right: 0.3rem;


}

.container {
    width: 100%;
    /* height: 470px; */
    display: flex;
    justify-content: space-evenly;
    margin: auto;
    flex-wrap: wrap;
    gap: 10px;
}

.mini_it {
    width: clamp(20px, 2.083vw, 60px);
    height: auto;
    vertical-align: bottom;
    /* padding: 10px 0px; */
    /* position: relative; */
    /* top: -60px; */
}


.b1,
.b2,
.b3 {
    margin-top: 5px;
    /* 将顶部外边距设置为 5px */
}

.c1,
.c2,
.c3 {
    /* margin-top: 5px; */
    font-size: 35px;
    font-size: clamp(16px, 1.823vw, 35px);
    /* margin-top: ; */
    /* 将顶部外边距设置为 5px */
}

.b1 {
    font-size: clamp(40px, 7.8125vw, 150px);
    /* position: relative; */
    top: -50px;
    left: -20px;
    /* 向上移动 5px */
}

.b2 {
    font-size: clamp(20px, 3.90625vw, 75px);
    /* position: relative; */
    top: -50px;
    left: -30px;
}

.A,
.B,
.C,
.D {
    padding: 1.5% 1.5%;
    background-color: rgba(215, 215, 215, 0.23);
    margin: 0px 0px 100px;
    border-radius: 20px;
}

.A {
    color: rgb(4, 175, 214);
}

.B {
    color: rgb(3, 151, 22);
}

.C {
    color: rgb(245, 211, 42);
}

.D {
    color: rgb(116, 119, 116);
}

.material-symbols-outlined {
    font-variation-settings:
        'FILL' 1,
        'wght' 700,
        'GRAD' 0,
        'opsz' 48;
}

.c_flex {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: clamp(5px, 1.042vw, 20px);
}

@media screen and (max-width: 768px) {
    .container {
        max-width: 600px;

    }
    .A,
.B,
.C,
.D {
    padding: 2.5% 10%;
    margin: 0px 0px 0px;

}
}
</style>
