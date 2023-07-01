<template>
  <head>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Kosugi+Maru&display=swap" rel="stylesheet">
  </head>
  <nav :style="navStyle">
    <img src="./assets/NMNH.jpg" alt="G_name" width="210" height="30">
    <div class="route">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/chart">Chart</router-link>
    </div>
  </nav>
  <router-view/>
</template>

<script>
export default {
  computed: {
    navStyle() {
      return {
        backgroundColor: '#f6d247',
        padding: '20px',
        fontSize: '20px'
      };
    }
  }
}
</script>

<style>
html {
  margin: -8px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #c52920;
  font-family: 'Kosugi Maru', sans-serif;
}

.route{
  text-align: center;
  padding-right:200px;
}

img{
  float: left;
}
nav{
  background-color: #f6d247;
  padding: 20px;
  font-size: 20px;
}
</style>
