<template>
  <head>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Kosugi+Maru&display=swap" rel="stylesheet">
  </head>
  <nav :style="navStyle">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/chart">Chart</router-link>
  </nav>
  <router-view/>
</template>

<script>
export default {
  computed: {
    navStyle() {
      if (this.$route.path === '/chart') {
        return {
          backgroundColor: '#f6d247',
          padding: '20px',
          fontSize: '20px'
        };
      } else {
        return {
          backgroundColor: '#fff',
          padding: '20px',
          fontSize: '20px'
        };
      }
    }
  }
};
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
  color: #2c3e50;
  font-family: 'Kosugi Maru', sans-serif;
}
</style>
