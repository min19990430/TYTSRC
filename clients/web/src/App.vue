<template>
  <div  id="app" >
    
<div class="header" :class="bgClass_header"></div>
<router-view></router-view>

    <div class="footer" :class="bgClass_footer"></div>
  </div>
</template>

<script setup>
import { computed} from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();


const bgClass_header = computed(() => {
  switch (route.path) {
    case '/login':
      return 'background-class-1_header';
    case '/MainApp':
      return 'background-class-2_header';
    case '/HistoricalData':
      return 'background-class-3';
    default:
      return 'default-background-class';
  }
});

const bgClass_footer = computed(() => {
  switch (route.path) {
    case '/login':
      return 'background-class-1_footer';
    case '/MainApp':
      return 'background-class-2_footer';

    default:
      return 'default-background-class';
  }
});
</script>

<style >
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
   reset css !!!
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}

.background-class-1_header {
  background-image: url('./assets/img/桃園永續館_城市造景示範案廠環境監測_header.png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  background-size: cover; /* 填滿容器且保持比例 */
  background-position: center; /* 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio: 50 / 1.5; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}

.background-class-2_header {
  background-image: url('./assets/img/Rectangle_header.png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  background-size: cover; /* 填滿容器且保持比例 */
  background-position: top; /* 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio:8.4 / 1; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}

.background-class-3 {
  background-image: url('./assets/img/Rectangle_header.png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  /* -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-attachment: scroll;
  background-position: center;
  background-size: 100% 100%;
  background-repeat: no-repeat;
  height: 100vh; */
  /* 或者根據需要設置高度 */
  /* width: 100%; */
  /* 設置寬度為100%，填滿父容器 */
  /* margin: 0%; */
  background-size: cover; /* 填滿容器且保持比例 */
  background-position: top; /* 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio:8.4 / 1; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}

.background-class-1_footer {
  background-image: url('./assets/img/桃園永續館_城市造景示範案廠環境監測_footer.png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  background-size: cover; /* 填滿容器且保持比例 */
  /* background-position: bottom; 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio: 18 / 1.5; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}
.background-class-2_footer {
  background-image: url('./assets/img/Rectangle_footer.png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  background-size: cover; /* 填滿容器且保持比例 */
  background-position: center; /* 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio: 4 / 1; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}
.background-class-3_footer {
  background-image: url('./assets/img/Rectangle(filter).png'), linear-gradient(to right, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  background-size: cover; /* 填滿容器且保持比例 */
  background-position: center; /* 置中圖片 */
  background-repeat: no-repeat;
  aspect-ratio: 4 / 1; /* 設定比例，這裡假設圖片是 16:9 */
  width: 100%;
  max-height: 100vh; /* 確保背景不超出視口高度 */
  margin: 0;
}

.default-background-class {
  background-color: rgb(255, 255, 255);
}

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400&display=swap');

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

button {
  background-color: #c4fcc6;
  display: flex;
  align-items: center;
  color: #11aa00;
  white-space: nowrap;
  background: inherit;
  cursor: pointer;
  font-size: 20px;
  padding: 1.3%;
  transition: background-color 0.3s ease, transform 0.3s ease;
  position: stinky;
  border-radius: 20px;
}

button:hover {
  background-color: #c4fcc635;
  transform: scale(1.05);
}

.material-symbols-outlined {
  line-height: 0;
  margin-right: 0.3rem;
  font-size: 30px;
}

.container {
  width: 5%;
  height: auto;
  display: flex;
  justify-content: space-between;
  margin: 10px 10px;
}

.A {
  color: rgb(2, 158, 201);
  padding: 10px 50px;
  background-color: rgba(215, 215, 215, 0.23);
  margin: 10px 0px;
}

.material-symbols-outlined {
  font-variation-settings:
    'FILL' 1,
    'wght' 700,
    'GRAD' 0,
    'opsz' 48;
}
</style>
