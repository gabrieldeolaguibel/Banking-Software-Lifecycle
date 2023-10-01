<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/skull">Skull</router-link> |
      <router-link to="/accounts">Accounts</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  display: flex;
  justify-content: center;
  gap: 15px;
  background-color: #ecf0f1;
  padding: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

nav a {
  text-decoration: none;
  color: #2c3e50;
  transition: color 0.3s;
}

nav a:hover {
  color: #3498db;
}
</style>
