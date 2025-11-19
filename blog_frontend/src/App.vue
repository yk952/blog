<script setup lang="ts">
import Navbar from './components/Navbar.vue'
import axios from 'axios';

axios.get("/api/article/1").then((response) => {
  console.log(response.data);
}).catch((error) => {
  console.log(error);
});


</script>

<template>
  <div id ="app">
    <Navbar />
    <router-view />
  </div>
</template>

<style>
:root {
  --yk-white: #fff;
  --yk-white-op: rgba(255, 255, 255, 0.15);
  --yk-black: #000;
  --yk-black-op: rgba(0, 0, 0, 0.15);
  --yk-none: #00000000;
  --yk-gray-op: #9999992b;
  --yk-gray-op-deep: #99999996;
  --yk-vip: #e5a80d;
  --yk-theme: #42b983; 
  --yk-theme-op: rgba(66, 185, 131, 0.15);
  --yk-theme-op-deep: rgba(66, 185, 131, 0.8);
  --yk-theme-op-light: rgba(66, 185, 131, 0.05);
  --yk-theme-none: rgba(66, 185, 131, 0);
  --yk-main: var(--yk-theme);
  --yk-main-op: var(--yk-theme-op);
  --yk-main-op-deep: var(--yk-theme-op-deep);
  --yk-main-op-light: var(--yk-theme-op-light);
  --yk-main-none: var(--yk-theme-none);
  --yk-shadow-theme: 0 8px 12px -3px var(--yk-theme-op);
  --yk-shadow-blackdeep: 0 2px 16px -3px rgba(0, 0, 0, .15);
  --yk-shadow-main: 0 8px 12px -3px var(--yk-main-op);
  --yk-shadow-nav: 0 5px 20px 0px rgba(28, 28, 28, 0.4);
  --yk-fontcolor: #333;
  --yk-background: #f5f5f5;
  --yk-reverse: #fff;
  --yk-maskbg: rgba(0, 0, 0, 0.6);
  --yk-maskbgdeep: rgba(0, 0, 0, 0.85);
  --yk-hovertext: #42b983;
  --yk-ahoverbg: #fff;
  --yk-lighttext: var(--yk-theme);
  --yk-secondtext: #666;
  --yk-scrollbar: rgba(200, 200, 223, 0.4);
  --yk-card-btn-bg: #f0f0f0;
  --yk-post-blockquote-bg: #f9f9f9;
  --yk-post-tabs-bg: #f5f5f5;
  --yk-secondbg: #eee;
  --yk-card-bg: #fff;
  --yk-card-bg-op: var(--yk-black-op);
  --yk-card-bg-op-deep: #00000045;
  --yk-card-bg-none: #1d1b2600;
  --yk-card-border: #eee;
  --yk-shadow-border: 0 8px 16px -4px #00000050;
  --style-border: 1px solid var(--yk-card-border);
  --style-border-always: 1px solid var(--yk-card-border);
  --style-border-hover: 1px solid var(--yk-lighttext);
  --style-border-hover-always: 1px solid var(--yk-lighttext);
  --style-border-dashed: 1px dashed var(--yk-theme-op);
  --style-border-forever: 2px solid var(--yk-lighttext);
  --yk-card-box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.06);
  --yk-card-hover-box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.15);
  --yk-snackbar-time: 3000ms;
  --postchat-main: #3e86f6;
  --postchat-main-op: #3e86f624;
  --postchat-fill: #FFFFFF;
  --offset: 0px;
  --hl-color: #eff;
  --hl-bg: #212121;
  --hltools-bg: #1c1c1c;
  --hltools-color: rgba(238, 255, 255, 0.8);
  --hlnumber-bg: #212121;
  --hlnumber-color: rgba(238, 255, 255, 0.5);
  --hlscrollbar-bg: #121212;
  --hlexpand-bg: linear-gradient(180deg, rgba(33, 33, 33, 0.6), rgba(33, 33, 33, 0.9));
  --global-bg: #fff;
  --hr-border: #97bcfb;
  --hr-before-color: #6ea2f9;
  --search-bg: #f6f8fa;
  --search-input-color: var(--yk-fontcolor);
  --search-result-title: #4c4948;
  --preloader-bg: #37474f;
  --preloader-color: #fff;
  --tab-border-color: #f0f0f0;
  --tab-botton-bg: #f0f0f0;
  --tab-botton-color: #1f2d3d;
  --tab-button-hover-bg: #dcdcdc;
  --tab-button-active-bg: #fff;
  --sidebar-bg: #f6f8fa;
  --btn-hover-color: #ff7242;
  --btn-color: #fff;
  --btn-bg: var(--yk-main);
  --text-bg-hover: var(--yk-main);
  --light-grey: #eee;
  --text-highlight-color: #1f2d3d;
  --blockquote-color: #6a737d;
  --blockquote-bg: rgba(73, 177, 245, 0.1);
  --reward-pop: #f5f5f5;
  --toc-link-color: #666261;
}

[data-theme=dark] {
  --yk-theme: #ffc848;
  --yk-theme-op: #f2b94b23;
  --yk-theme-op-deep: #f2b94bdd;
  --yk-theme-none: #f2b94b00;
  --yk-blue: #0084FF;
  --yk-red: #FF3842;
  --yk-red-op: #ff38421a;
  --yk-red-op-deep: #ff38426e;
  --yk-pink: #d44040;
  --yk-green: #3e9f50;
  --yk-green-op: #3e9f501a;
  --yk-green-op-deep: #3e9f506e;
  --yk-purple: #7a60d2;
  --yk-yellow: #ffc93e;
  --yk-yellow-op: #ffc93e30;
  --yk-orange: #ff953e;
  --yk-fontcolor: #F7F7FA;
  --yk-background: #18171d;
  --yk-reverse: #fff;
  --yk-maskbg: rgba(0, 0, 0, 0.6);
  --yk-maskbgdeep: rgba(0, 0, 0, 0.85);
  --yk-hovertext: #0A84FF;
  --yk-ahoverbg: #fff;
  --yk-lighttext: var(--yk-theme);
  --yk-secondtext: #a1a2b8;
  --yk-scrollbar: rgba(200, 200, 223, 0.4);
  --yk-card-btn-bg: #30343f;
  --yk-post-blockquote-bg: #000;
  --yk-post-tabs-bg: #121212;
  --yk-secondbg: #21232a;
  --yk-shadow-nav: 0 5px 20px 0px rgba(28, 28, 28, 0.4);
  --yk-card-bg: #1b1c20;
  --yk-card-bg-op: var(--yk-black-op);
  --yk-card-bg-op-deep: #00000045;
  --yk-card-bg-none: #1d1b2600;
  --yk-shadow-lightblack: 0 5px 12px -5px rgba(102, 68, 68, 0.0);
  --yk-shadow-light2black: 0 5px 12px -5px rgba(102, 68, 68, 0.0);
  --yk-card-border: #3d3d3f;
  --yk-shadow-border: 0 8px 16px -4px #00000050;
  --style-border: 1px solid var(--yk-card-border);
  --style-border-always: 1px solid var(--yk-card-border);
  --style-border-hover: 1px solid var(--yk-lighttext);
  --style-border-hover-always: 1px solid var(--yk-lighttext);
  --style-border-dashed: 1px dashed var(--yk-theme-op);
  --style-border-forever: 2px solid var(--yk-lighttext);
}

@media screen and (max-width: 768px) {
  :root {
    --style-border: 1px solid var(--yk-none);
    --style-border-hover: 1px solid var(--yk-none);
  }
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  position: relative;
  min-height: 100%;
  background: var(--yk-background);
  color: var(--yk-fontcolor);
  font-size: 16px;
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei";
  line-height: 2;
  -webkit-tap-highlight-color: transparent;
}

html {
  height: 100%;
  font-size: 20px;
  overflow-x: hidden;
  line-height: 1.15;
  text-size-adjust: 100%;
  -webkit-tap-highlight-color: transparent;
}

::-webkit-scrollbar {
  width: 12px;
  height: 6px;
}
::-webkit-scrollbar-thumb {
  background: var(--yk-card-border);
  opacity: 0.5;
  border-radius: 8px;
  cursor: pointer;
  border: 2px solid var(--yk-background);
}
::-webkit-scrollbar-track {
  background-color: var(--yk-background);
}

::selection {
  background: var(--yk-fontcolor);
  color: var(--yk-background);
}
</style>
